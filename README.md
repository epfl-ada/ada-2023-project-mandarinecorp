# Abstract

From the basis of Prof. West's analysis, we observed that Wikipedia views and usage were affected by COVID-19. We think that this change of behavior in Wikipedia users can be linked to the social and societal changes happening during COVID-19. Therefore, we can argue that sudden changes in social habits induced inner questions in the population. In other words, the population will be able to compare their life before and after these changes and regarding their perception of life in general. Our perception of life is mainly influenced by timeless principles such as our philosophical and religious knowledge. Therefore, we want to see if we can observe this phenomenon in the data using the views on philosophy and religion pages on Wikipedia.

## Research Questions

1. Do Wikipedia's philosophy and religion page views provide insights into how individuals perceive life amid the unprecedented social conditions of COVID-19?
2. How do these perceptions vary across countries, and do cultural differences in main cultural philosophical currents influence philosophical and religious shifts?
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

Clementine : 
Louis : 
Karl : 
Hippolyte : Defining philosophy clusters and build correlation heatmaps per period. Methodology for trend changes study along with Clementine.