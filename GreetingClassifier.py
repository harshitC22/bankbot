"""
written by: harshit C
"""

import nltk
import random

"""
classifies words into greetings or not greetings
"""
class GreetingClassifier:

    feature_set= None

    """
    give the speech tag of the word (Ex: NN for noun)
    """
    def get_tag (self, word):
        return nltk.pos_tag (word)

    """
    defines the features which will define a greeting
    """
    def greeting_features (self, word):

        """
        :type word: basestring
        """
        return { 'first letter': word [0], 'last letter': word [-1], 'last two letters': word[-2:], 'tag': ( (list ((self.get_tag ([word])) [0])) [1] ) }

    """
    classifies words
    """
    def greeting_classifier (self):

        f = open ("greetings", "r")
        f1 = open ("not_greetings", "r")

        text = ""
        for line in f:
            text += line
        greeting = nltk.word_tokenize (text)

        text = ""
        for line in f1:
            text += line
        not_greeting = nltk.word_tokenize (text)

        labels = ( [ (word, 'greeting') for word in greeting] + [ (word, 'not a greeting') for word in not_greeting])
        #print labels
        random.shuffle (labels)

        feature_set = ( [ (self.greeting_features(w), check) for (w, check) in labels])
        print len (feature_set)
        print feature_set
        train_set= feature_set [:]
        test_set= feature_set [:40]
        greeting_classifier = nltk.NaiveBayesClassifier.train (train_set)
        print (nltk.classify.accuracy (greeting_classifier, test_set))

        assert isinstance (greeting_classifier, nltk.NaiveBayesClassifier)
        return greeting_classifier