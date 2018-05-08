"""
written by: harshit C
"""

import nltk
import random
import bot.BOT
import bot.genderClassification
import bot.GreetingClassifier
import bot.ChunkDetect
import bot.Classification

"""
global variables 
"""
keywords= ["balance", "transactions"]
greeting_response= ["hi, how may I help?", "hello, nice to meet you!", "hey, I am Chatter..how may I help you?", "hey! What can I do for you?"]
chatter= bot.BOT.The_BOT ()
gClassifierObj= bot.GreetingClassifier.GreetingClassifier ()
gClassifier= gClassifierObj.greeting_classifier ()
gClassifier.show_most_informative_features (15)
cdo= bot.ChunkDetect.Chunk_Detector (keywords)

"""

wake up
"""
chatter.wake_up ()

"""
loops through user input
"""
for i in xrange (0, 100, 1):

    inp= raw_input ()
    if not (chatter.get_state ()== "greeted"):

        """
        classifies the first input into 'greeting' or 'not a greeting' 
        """
        if gClassifier.classify (gClassifierObj.greeting_features (inp.split () [0])) == "greeting":

            """
            picks a random response for the greeting
            """
            print greeting_response [random.randint (0, len (greeting_response) - 1)]
        else:
            print "Hi, was that a greeting?"

    """
    checks for chunks that may indicate that it is a requirement
    """
    inp= raw_input ()
    if cdo.has_keyword (inp):

        #chatter.set_state ("requirement_asked")
        if (cdo.need_chunk_present (inp)) or (len (nltk.word_tokenize (inp))== 2):

            print "Your balance is 77777.77$"
        else:
            print "Didn't understand ur requirement"

