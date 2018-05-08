#   imports   #
import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import wordnet

#   variables   #
text = ""
text2= ""
umm = "umm"
uh = "uh"
filtered_sentence = ""
tokens = []
token2= []
filtered_list= []
synonyms= []
antonyms= []
f = open ("test.txt", "r")
f2= open ("trainingSet.txt", "r")
stop_words = set (stopwords.words ('english'))

stop_words.add (umm)
stop_words.add (uh)

#   tokenize file   #
for line in f:
    text += line
tokens = nltk.word_tokenize (text)

for l in f2:
    text2+= l
tokens= nltk.word_tokenize (text2)

custom_sent_tokenizer = PunktSentenceTokenizer (text)

#   filter Stop Words   #
print 'Filtered Text: \n'
for w in tokens:
    if w not in stop_words:
        filtered_sentence += " " + w

print filtered_sentence + '\n'

filtered_list = nltk.word_tokenize(filtered_sentence)
tokenized = custom_sent_tokenizer.tokenize (text)

#   speech tagging   #
print 'Tags generated :\n'
try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize (i)
            tagged = nltk.pos_tag (words)
            print (tagged)

            #   chunks   #
            # chunkGram = r"""Chunk: {<NNP>+<JJ.?>*}""" #
            chunkGram = r"""Chunk: {<NNP>+<VB.?|DT|RB.?>*<JJ.?>*}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()

        #for i in tokenized[5:]:
            #words = nltk.word_tokenize(i)
            #tagged = nltk.pos_tag(words)

            #chinkGram = r"""Chunk: {<.*>+}}<VB.?|IN|DT|TO>+{"""

            #chinkParser = nltk.RegexpParser(chinkGram)
            #chinked = chinkParser.parse(tagged)
            #chinked.draw()

except Exception as e:
        print (str (e))

for syn in wordnet.synsets ("good"):
    for l in syn.lemmas ():
        synonyms.append (l.name ())
        if l.antonyms ():
            antonyms.append (l.antonyms () [0].name ())

print '\nSynonyms:\n'
print synonyms
print '\nAntonyms:\n'
print antonyms

##//////////////////////////////////
##
##Frequency Distribution
##
##///////////////////////////////////

all_words = nltk.word_tokenize (text)
all_words = nltk.FreqDist (all_words)
word_features = list (all_words.keys ()) [:10]

print '\nFrequent Words used:\n'
print word_features

all_words = nltk.word_tokenize (filtered_sentence)
all_words = nltk.FreqDist (all_words)
word_features = list (all_words.keys ()) [:10]

print '\nFrequent Words used in filtered text:\n'
print word_features

##//////////////////////////////////
##
##NAIVE BAYES CLASSIFIER
##
##//////////////////////////////////

trainingSet= token2
testingSet= tokens

classifier= nltk.NaiveBayesClassifier.train (trainingSet)
print("Classifier accuracy percent:", (nltk.classify.accuracy (classifier, testingSet))*100)
classifier.show_most_informative_features (15)
