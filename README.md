# Relevant website for this project : https://kl4rkus.github.io/ada-template-website/

# Abstract

From the basis of Prof. West's analysis, we observed that Wikipedia views and usage were affected by COVID-19. We think that this change of behavior in Wikipedia users can be linked to the social and societal changes happening during COVID-19. Therefore, we can argue that sudden changes in social habits induced inner questions in the population. In other words, the population will be able to compare their life before and after these changes and regarding their perception of life in general. Our perception of life is mainly influenced by timeless principles such as our philosophical and religious knowledge. Therefore, we want to see if we can observe this phenomenon in the data using the views on philosophy and religion pages on Wikipedia.

## Research Questions

1. What are the differents categories of philosophies and how do they interact with each other during Covid ? 
2. How do the interests for philosophies vary around Covid timepoint and can it give insights on how people dealt with this pandemic? 
3. Can we identify groups of languages exhibiting similar philosophical and religious reactions to the changes induced by COVID-19?

## Proposed additional datasets
Views of philosophical and religious current pages retrieved from the Wikipedia API: "https://en.wikipedia.org/w/api.php"
We use the API in three different ways : 
+ to retrieve the names of the philosophies from the english page "List of philosophies" by retrieving the content of the page and cleaning it to obtain the right format
+ to obtain the views from a page between two dates
+ to obtain the pages in other languages, from the english url

## Methods

Our initial focus is on examining the differences in page view behavior across various philosophy topics during significant COVID-19 dates. This analysis aims to provide insights into people's interests in this particular domain and offer a glimpse into global thinking within the English language.
To simplify this analysis, we have grouped philosophies into broader topics clustering philosophy's by more general domains. We will then try to get insights by computing correlations between each of these domains across the time periods and try to interpret results.

Once we have gathered initial insights from this approach, we will proceed with a more rigorous and specific time series decomposition analysis. The objective here is to understand whether important COVID-19 dates have influenced changes in attention across philosophy pages. We will also investigate trends changes and jumps in interest per philosophy with statistical rigor.

Finally, we will explore how attention to philosophy topics varies across languages. We will examine whether we can identify linguistic regions that share similar behavioral patterns and assess whether these similarities remain stable throughout the COVID-19 pandemic or undergo modifications due to this event.

## Organization within the team

Clementine : Get all the data from wikipedia, in all languages.  Create and clean the dataframes used across the various parts. Methodology to study trends with Hippolyte. Study of the trends and interpretation. 

Louis : Studied and interpret changes across languages. Defined the project goals with the others. Methodoloy to observe the behavior of our data in other language (all but english). 

Karl : Sort by languages, made the website, helped where possible and needed

Hippolyte : Defining philosophy clusters and build correlation heatmaps per period. Methodology for trend changes study along with Clementine.
