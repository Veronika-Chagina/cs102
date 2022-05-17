import math
import re
from collections import Counter

from sklearn.metrics import accuracy_score  # type: ignore


class NaiveBayesClassifier:
    def __init__(self, alpha=1):
        self.word_count = Counter({})
        self.class_count = {}
        self.alpha = alpha

    def norm(self, string):
        no_punc_no_space = re.sub(r"[^\w\s\d+]", "", string.lower()).strip()
        return [no_punc_no_space][0].split()

    def fit(self, x, y):
        """Fit Naive Bayes classifier according to X, y."""
        self.class_count = dict.fromkeys(set(y), 0)
        d = 0
        for i in range(len(x)):
            mes, lb = x[i], y[i]
            lst_mes = self.norm(mes)
            for word in lst_mes:
                self.class_count[lb] += 1
                if word not in self.word_count:
                    d += 1
                    self.word_count[word] = Counter(dict.fromkeys(set(y), 0))
                self.word_count[word][lb] += 1

        for w in self.word_count:
            for c in self.word_count[w]:
                self.word_count[w][c] = (self.word_count[w][c] + self.alpha) / (
                    self.class_count[c] + self.alpha * d
                )

    def predict(self, X):
        prediction = []
        for x in X:
            last_x = self.norm(x)
            mx = float("-inf")
            expect = 0
            for lb in self.class_count:
                m = sum(
                    [
                        math.log(self.word_count[wrd][lb]) if self.word_count[wrd] else 0
                        for wrd in last_x
                    ]
                )
                if m > mx:
                    mx = m
                    expect = lb
            prediction.append(expect)
        return prediction

    def score(self, x_test, y_test):
        """Returns the mean accuracy on the given test data and labels."""
        pr = self.predict(x_test)
        return accuracy_score(pr, y_test)
