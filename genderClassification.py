import nltk
import random
from nltk.corpus import names

class GenderClassify:

    #   __init__
    def __init__(self):
        labeled_names= []

    #  sets basic metric to classify gender
    def gender_features (self, word):
        return { 'last letter': word [-1] }

    def naive_bayes (self, person_name):

        labeled_names = ([(name, 'male') for name in names.words("male.txt")] + [(name, 'female') for name in names.words("female.txt")])
        random.shuffle (labeled_names)

        feature_set = ( [ (self.gender_features (n), gender) for (n, gender) in labeled_names])
        train_set = feature_set [500:]
        test_set = feature_set [:500]

        gender_classifier = nltk.NaiveBayesClassifier.train (train_set)
        return gender_classifier.classify (self.gender_features (person_name))
