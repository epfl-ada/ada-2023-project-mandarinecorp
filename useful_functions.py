import numpy as np
import matplotlib as plt 
import requests
import re
import pandas as pd 
from urllib.parse import unquote, urlsplit 
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels as sm


def get_url_list(target_languages, page_titles):
    api_url = "https://en.wikipedia.org/w/api.php"
    language_links = []

    for page in page_titles : 

    # Make separate requests for each language
        for lang in target_languages:
            params = {
                'action': 'query',
                'titles': page,
                'prop': 'langlinks',
                'llprop': 'url',
                'format': 'json',
                'lllang': lang,
            }

            # Make the API request
            response = requests.get(api_url, params=params)
            data = response.json()

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract language links from the API response
                pages = data['query']['pages']
                page_id = next(iter(pages))
                langlinks = pages[page_id].get('langlinks', [])
                for link in langlinks:
                    language_links.append( [link['url'],page])
            else:
                print(f"Error for language {lang}: {response.status_code}")
    return language_links
        

def get_page_views_by_languages(links,page_titles):
    philo_views=pd.DataFrame()

    for link in links:
        # Define a user agent to have acces to the API 
        user_agent = 'MandarineCorp (clementine.naim@epfl.ch)'
        # Specify the headers with the user agent
        headers = {
            'User-Agent': user_agent,
            'accept': 'application/json'
        
        }
        # Find country code:
        code = urlsplit(link[0]).hostname.split('.')[0]

        path = unquote(urlsplit(link[0]).path)
        # Use a regular expression to find the title part
        match = re.search(r'/wiki/(.+)', path)
        title = match.group(1)
        subject=link[1]

        #print(link,title,code,subject)
        url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{code}.wikipedia.org/all-access/all-agents/{title}/daily/2019010100/2022010100'
        # Making a GET request
        response_views = requests.get(url,headers=headers)

        # Check if the request was successful (status code 200)
        if response_views.status_code == 200:
            # Print the response content
            data = response_views.json()
            # Extract the 'items' list from the data
            items_list = data['items']
            #print(items_list)
            # Create a DataFrame
            df = pd.DataFrame(items_list)
            df["subject"]=subject
            df["code"] =code
            #print(df)
            philo_views = pd.concat([philo_views,df])
        else:
            #Print an error message if the request was unsuccessful
            print(f"Error: {response_views.status_code}")
            print(title)


        #i+=1
        #if i==11 :
        #    index_subject+=1
        #    i=0
    return philo_views
        
def diff_percentage(x1,x2):
    return (np.abs(x2)-np.abs(x1))/np.abs(x1)*100
        
def plot_regression_on_segments(df,article,segments,threshold,showplot =True):
    
    # Example data
    decompose_result = seasonal_decompose(df[article],period=52)
    trend = decompose_result.trend
    trend_series = pd.Series(trend)
    if showplot== True :
        plt.plot(trend_series.index[segments[0][0]:segments[2][1]], trend_series[segments[0][0]:segments[2][1]], label='Original Trend',linewidth=0.5)


    # Define the segments and change points
    timepoints = [segments[0][1], segments[1][1]]
    change_indices=[]

    slopes =[]
    intercepts=[]
    diff_slope = []
    diff_intercept=[]
    type_diff = []
    # Fit segmented regression models and plot the segmented regression lines
    j=0
    for start, end in segments:
        X_segment = sm.add_constant(np.arange(start, end))
        model_segment = sm.OLS(trend_series[start:end], X_segment)
        results_segment = model_segment.fit()
        slopes.append(results_segment.params.iloc[1])
        intercepts.append(results_segment.params.iloc[0])
        # Plot the segmented regression lines
        if showplot == True :
            plt.plot(trend_series.index[start:end], results_segment.predict(X_segment), label=f'Segment period {j}',linestyle='--',linewidth=1.5)
        j+=1
   
    #Compare the slopes 
    for i in [0,1]:
        diff= diff_percentage(slopes[i],slopes[i+1])
        diff_intercept.append(intercepts[i]-intercepts[i+1])
        if slopes[i+1]*slopes[i]>0 and diff>0:
            type_diff.append('acceleration')
            if slopes[i]<0:
                diff= -diff
        elif slopes[i+1]*slopes[i]>0 and diff<0 :
            type_diff.append('deceleration')
            if slopes[i]>0:
                diff=-diff
        
        elif slopes[i+1]*slopes[i]<0 :
            type_diff.append('direction change')
            if slopes[i]>0 : 
                diff = -np.abs(diff)
            else :
                diff = np.abs(diff)

        if diff >threshold or diff<-threshold : 
            #print('Significant change in trend between period ',i,' and period ',i+1)
            change_indices.append(timepoints[i])
        #else :
           # print('No significant change in trend between period ',i,' and period ',i+1)
        diff_slope.append(diff)

    print(type_diff)  
    
    same_indices = list(set(timepoints)-set(change_indices))
    # Mark the change points
    if showplot==True : 
        plt.scatter(trend_series.index[change_indices], trend_series.iloc[change_indices], color='red', marker='o', label='Change')
        plt.scatter(trend_series.index[same_indices], trend_series.iloc[same_indices], color='black', marker='x', label='No change')
        plt.title(article)
        plt.xticks(rotation=45)
        plt.legend()
        plt.show()
    return diff_slope,diff_intercept, type_diff


        
# Select the top 5 and bottom 5 values
def plot_biggest_change(ax, df, col_to_sort):
    df_sorted = df.sort_values(by=col_to_sort, ascending=False)
    top_5 = df_sorted.head(5)
    bottom_5 = df_sorted.tail(5)

    # Plot the bar chart on the specified Axes object
    ax.bar(top_5.index, top_5[col_to_sort], color='green', label='Positive trend')
    ax.bar(bottom_5.index, bottom_5[col_to_sort], color='red', label='Negative trend')

    # Add labels and legend
    ax.set_xlabel('Philosophies')
    if col_to_sort.__contains__('Intercept') : 
        ax.set_xlabel('Change')
    else :    
        ax.set_ylabel('Percentage change in trend')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    ax.legend()

