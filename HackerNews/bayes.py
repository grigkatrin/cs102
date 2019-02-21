from collections import Counter
import csv
import string
import math


class NaiveBayesClassifier:

    def __init__(self, alpha):
        self.alpha = alpha

    def fit(self, X, y):
        """ Fit Naive Bayes classifier according to X, y. """
        working_data = []
        all_words = []
        self.all_labels = list(set(y))
        self.label_list = dict.fromkeys(self.all_labels, 0)

        for message, label in zip(X, y):
            words = message.split()
            for word in words:
                working_data.append((word, label))
                all_words.append(word)
                self.label_list[label] += 1

        self.word_list = Counter(working_data)
        self.all_words = list(set(all_words))

        self.word_probability = dict.fromkeys(self.all_words, dict.fromkeys(self.label_list))

        for word in self.all_words:
            for label in self.all_labels:
                nic = self.word_list[(word, label)]
                nc = self.label_list[label]
                d = len(self.all_words)
                self.word_probability[word][label] = (nic + self.alpha)/(nc + d * self.alpha)

        self.label_probability = dict.fromkeys(self.all_labels)
        message_labels = Counter(y)
        for label in self.all_labels:
            self.label_probability[label] = message_labels[label]/len(y)

    def predict(self, X):
        """ Perform classification on an array of test vectors X. """
        predict_list = []
        for message in X:
            predict_labels = []
            words = message.split()

            for label in self.label_list:
                current = self.label_probability[label]

                for word in words:
                    score = self.word_probability.get(word, None)
                    if score:
                        current += score[label]

                predict_labels.append((current, label))

            _, ans = max(predict_labels)
            predict_list.append(ans)

        return predict_list

    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        prediction = self.predict(X_test)
        correct = 0
        for i in range(len(y_test)):
            if prediction[i] == y_test[i]:
                correct += 1

        return correct/len(y_test)



with open("SMSSpamCollection") as f:
    data = list(csv.reader(f, delimiter="\t"))

    def clean(s):
        translator = str.maketrans("", "", string.punctuation)
        return s.translate(translator)

X, y = [], []
for target, msg in data:
    X.append(msg)
    y.append(target)

X = [clean(x).lower() for x in X]
X_train, y_train, X_test, y_test = X[:3900], y[:3900], X[3900:], y[3900:]

model = NaiveBayesClassifier(1)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
