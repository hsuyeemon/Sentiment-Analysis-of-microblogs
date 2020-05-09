# Sentiment-Analysis-of-TwitterData

This implementation is to identify polarity that is expressed in a given tweet.
- developed a classifier for sentiment analysis by machine learning using SVM
Two subtasks:
(1) two class classification (i.e. Positive or Negative),
(2) five class classification (i.e.2, 1, 0,-1,-2).

There are two cases with topics in building the classifier. They are:
(i) topics in the test data also appear in the training data,
(ii)topics in the test data never appear in the training data

According to these result, the accuracy of the first case is better than the second case both classification tasks.

The accuracy was improved if we put weights to the opinion words.
In case of calculating weights for opinion words,we use SentiwordNet to get the opinion words and their scores.

****
Data
Dataset of SemEval-2016 Task 4 is used.
There are two files:
Topic.2class.txt: a collection of tweets annotated with two classes
Topic.5class.txt: a collection of tweets annotated with five classes
The format of each line is:
	tweet_id<tab> topic <tab> class <tab> tweets



Steps
Preprocessing
Feature Extraction
Partition of data
Machine Learning
Evaluation

