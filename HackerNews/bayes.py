from collections import Counter
import math
import csv
import string


class NaiveBayesClassifier:

    def __init__(self, alpha):
        self.alpha = alpha
        self.label_prediction = {}
        self.word_prediction = {}

    def fit(self, X, y):
        """ Fit Naive Bayes classifier according to X, y. """

        #{'ham': 0.8669230769230769, 'spam': 0.13307692307692306}
        labels_amount = dict(Counter(y))
        for label in labels_amount:
            probability = labels_amount[label]/len(y)
            self.label_prediction.update({label: probability})

        tbl = []
        all_words = []
        self.words_with_labels = dict.fromkeys(labels_amount, 0)
        for message, label in zip(X, y):
            words = message.split()
            for word in words:
                tbl.append((word, label))
                all_words.append(word)
                self.words_with_labels[label] += 1

        self.word_label = dict(Counter(tbl))
        words_amount = dict(Counter(all_words))

        self.word_prediction.fromkeys(words_amount)

        for word in words_amount:
            current = dict.fromkeys(labels_amount)

            for label in labels_amount:
                nc = self.words_with_labels[label]
                nic = self.word_label.get((word, label), 0)
                d = len(words_amount)
                alpha = self.alpha
                current[label] = (nic + alpha) / (nc + alpha * d)

            self.word_prediction[word] = current

    def predict(self, X):
        """ Perform classification on an array of test vectors X. """
        predict_list = []

        for sentence in X:
            words = sentence.split()
            likely_labels = []

            for cur_label in self.label_prediction:

                amount = self.label_prediction[cur_label]

                # Calculating lnP(C)
                total_amount = math.log(amount, math.e)

                for word in words:
                    word_dict = self.word_prediction.get(word, None)

                    if word_dict:
                        # Calcuting the sum of lnP(wi|C)
                        total_amount += math.log(word_dict[cur_label], math.e)

                likely_labels.append((total_amount, cur_label))

            # Maximum value between lnP(label|D)
            _, answer = max(likely_labels)
            predict_list.append(answer)
        return predict_list

    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        correct = 0
        for i, answer in enumerate(self.predict(X_test)):
            if answer == y_test[i]:
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