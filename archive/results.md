# Data Analysis Results

*Preliminary discussion of findings from analysis performed on the data gathered from Physionet studies.*

## Hypothesis 1
**Less than 50% of datasets on PhysioNet report demographics.**

## Hypothesis 2
**Studies that report race and ethnicity report other demographic information (i.e. age and gender) at a higher frequency than those that don’t.**

To investigate this hypothesis, we performed chi-squared tests on several permutations of 2 variables chosen from race, ethnicity, age, and gender information presence. We isolated the variable reporting counts for each study to create contingency tables of race vs. age, race vs. gender, ethnicity vs. age, ethnicity vs. gender, race vs. ethnicity, and age vs. gender. Assumptions for a chi-squared test include random samples, indepdence of observations, cells in the contingency tables must be mutually exclusive, and 80% of frequencies in the contingency tables >5 and no frequencies <1. Our null hypothesis for each permutation was that the two variables being examined were reported independently. The alternate hypothesis was that the reporting for the two variables in each test were not reported independently. Independence of observations was (?) violated as several studies reported in Physionet and that are included in preliminary analysis are based on the same overarching database. However, random sampling, mutually exclusive contingency table cells, and minimum expected value conditions are met by our data. 

With an alpha (&alpha;) = .05, we found that the p-values for ace vs. age, race vs. gender, ethnicity vs. age, and ethnicity vs. gender were all significantly greater than &alpha; = .05. Thus, we fail to reject our null hypotheses that these combinations of two variables were reported independently. Looking at race vs. ethnicity and age vs. gender, the p-value for these chi-squared tests were significantly smaller than &alpha; = .05 -- several magnitudes of 10 smaller. From these results, we reject our null hypothesis that race and ethnicity and age and gender are reported independently. Thus, we can conclude that race-ethnicity and age-gender (as a pair) are not reported independently in the studies available from the Physionet database. 


## Hypothesis 3
**Age reporting in these studies is biased.**

## Hypothesis 4
**The proportion of studies that report race and ethnicity information is significantly lower than the proportion of studies that report age and gender.**

## Hypothesis 5
**Studies with larger/smaller sample sizes are more likely to provide more detailed demographic data.**

## Hypothesis 6
**Gender breakdown in studies not focused on a single sex is skewed.**

## Hypothesis 7
**The reporting of demographic data is correlated/associated with location of the study conducted.**

## Hypothesis 8 
**Studies focused on XYZ condition are more likely to provide race/ethnicity/gender/age data.**