# Fundamentals of statistical learning: Expectation Maximization to classify document data from 2 datasets, 20Newsgroup and Reuters-21578.

Following experiments have been conducted:

1) Traditional Naive Bayes: Initially, assume each news article belongs to a single class (one to one correspondence between the mixture model and the class label) and build a simple Naive Bayes classifier and train it on a portion of labeled data and report its performance. This is the baseline.

2) Expectation-Maximization with labeled and Unlabeled data: You will use samples from the unlabeled data and repeat the experiment using Expectation-Maximization along with a Naive Bayes classifier under the assumption that there is a one-to-one correspondence between the mixture model and the class label.

3) Multiple Mixture components using labeled data: You will relax the assumption made in the first 2 experiments. You will consider that a single news article can belong to several subtopics and experiment with a Naive Bayes classifier using multiple mixture components on the labeled dataset.

4) Multiple Mixture components using labeled and unlabeled data: You will repeat experiment 2 with the relaxed assumption and use Expectation-Maximization to determine the parameters.

 
