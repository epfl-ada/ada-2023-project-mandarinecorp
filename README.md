# Abstract

From the basis of Prof. West's analysis, we observed that Wikipedia views and usage were affected by COVID-19. We think that this change of behavior in Wikipedia users can be linked to the social and societal changes happening during COVID-19. Therefore, we can argue that sudden changes in social habits induced inner questions in the population. In other words, the population will be able to compare their life before and after these changes and regarding their perception of life in general. Our perception of life is mainly influenced by timeless principles such as our philosophical and religious knowledge. Therefore, we want to see if we can observe this phenomenon in the data using the views on philosophy and religion pages on Wikipedia.

## Research Questions

1. Do Wikipedia's philosophy and religion page views provide insights into how individuals perceive life amid the unprecedented social conditions of COVID-19?
2. How do these perceptions vary across countries, and do cultural differences in main cultural philosophical currents influence philosophical and religious shifts?
3. Can we identify groups of cultures exhibiting similar philosophical and religious reactions to the changes induced by COVID-19?

## Proposed additional datasets
Views of philosophical and religious current pages retrieved from the Wikipedia API: "https://en.wikipedia.org/w/api.php"
We use the API in three different ways : 
+ to retrieve the names of the philosophies from the english page "List of philosophies" by retrieving the content of the page and cleaning it to obtain the right format
+ to obtain the views from a page between two dates
+ to obtain the pages in other languages, from the english url

## Methods

The goal will be first to look at general trends and try to highlight them by plotting a time series of page logs for philosophy as a whole. We could then try to identify regime switches in the data and compare with proposed breakpoints dates. This could be achieved by fitting our whole philosophy time series to a Markov Switching Autoregressive Models (MS-AR) and comparing switching times with dates, we would define an upward trending and downward trading regime. Additionally, something that could be interesting is to see if any external effect could cause seasonality effects in the trends that should then not be attributed to COVID related behavior, this could be achieved looking at PACF/ACF of the time series and may avoid some biased and incorrect conclusions.

To further enhance the analysis, the next stage involves constructing a classification system for philosophies, grouping them into broader topics and subcategories. This will enable more precise and robust categorizations. We allow ourselves to be able to perform the analysis described below at different levels, using broader topics or using subcategories or even individual philosophies if it proves to be relevant. We used ChatGPT to help us during the classification task.

### Example of classification

- Class 4: Political and Social Ideologies
  - Subclass 4.1: Political Systems
    - Anarchism (including Anarcho-capitalism)
    - Authoritarianism
    - Liberalism
  - Subclass 4.2: Social Philosophies
    - Communism
    - Socialism
    - Conservatism

Next part of the analysis would then focus on determining in the global philosophical domain, what are the broader topics, subcategories or individual philosophies themselves that explain most of the variance of the global pagelog data. One tool we may use would be Lasso regression to perform feature selection or ANOVA analysis (feature would here be broader philosophical topics, subcategories or individual philosophies themselves), we would then select for each period and each country a subset of fixed size of the total number of features. Intuition about this analysis could be visualized by building a bar plot displaying selection frequency for each feature.

It would then be really interesting to compare across periods and countries which features are selected, and based on which features are selected and the %of variance they explain about the global trend we may be able to perform clustering. By mapping each Country to the space of selected features with corresponding %of explained variance (all of that per period), we may end up seeing clusters across countries that would be a nice evidence of similarities in culture/mindset reaction to COVID-19.

A major difficulty and limit of this idea and procedure is that results will be mainly driven by the most globally popular philosophy topics, while indeed, smaller portions of the philosophy global interest and more singular topics are more subject to bigger relative increase or decrease, that is one one hand interesting and on the other hand more noisy as could be just random effects or isolated/transient and not relevant trends unrelated to COVID.

## Proposed timeline

- Week 10: End of the classification uniformized for English and all languages. End of the preprocessing (uniformization), and implementation of a deeper EDA for all languages (except English).

- Week 11: Implementation of Analysis tools described previously for the first part of the project (Using only English pages) and interpretation of results. Start of the implementation for all languages in order to see if our data is preprocessed enough. Resolve issues otherwise for the last part.

- Week 12: Implementation of Analysis tools described previously for the second part of the project (Using all languages pages) and interpretation of results. Start of the redaction of the report.

- Week 13: Implementation of the Analysis for the third part (Clustering languages) and interpretation of results. Start cleaning and commenting on the code properly.

- Week 14: End of the cleaning and commenting on the code properly. End of the redaction of the report.

## Organization within the team

- Data cleaning/ processing: Karl and Clementine.
- Defining analysis tools and methods: Hippolyte and Louis.

### Hippo version

Looking at outputs, all the team contributes to interpreting results and develop conclusion or going back to new hypothesis or methodology proposals.

### Louis version

Interpretation of the results: All the team together, and if we don’t agree on conclusions we provide further analysis sharing the work using the previously described organization.

## Questions for TAs

- Do you have any advice/intuition about whether our analysis methodology could be too ambitious or would probably fail for some reasons and if it is the case to what alternative approaches we may want to look into? Many thanks for your precious feedback.
