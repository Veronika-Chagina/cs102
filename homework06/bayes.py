# type: ignore
import csv
import string
from collections import defaultdict

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


class NaiveBayesClassifier:
    def __init__(self, alpha=0):
        self.class_freq = defaultdict(lambda: 0)
        self.feat_freq = defaultdict(lambda: 0)

    def fit(self, X, y):
        for feature, label in zip(X, y):
            self.class_freq[label] += 1
            for value in feature:
                self.feat_freq[(value, label)] += 1

        num_samples = len(X)
        for k in self.class_freq:
            self.class_freq[k] /= num_samples

        for value, label in self.feat_freq:
            self.feat_freq[(value, label)] /= self.class_freq[label]

        return self

    def predict(self, X):
        return [
            max(self.class_freq.keys(), key=lambda c: self.calculate_class_freq(x, c)) for x in X
        ]

    def calculate_class_freq(self, X, clss):
        freq = -np.log(self.class_freq[clss])

        for feat in X:
            freq += -np.log(self.feat_freq.get((feat, clss), 10 ** (-7)))
        return freq

    def score(self, X_test, y_test):
        predictions = self.predict(X_test)
        print("pred", predictions)
        return accuracy_score(predictions, y_test)

