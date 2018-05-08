import bot.GreetingClassifier
import bot.ChunkDetect

#class Base_Classifier:
    #
    # gclassifier_obj= bot.GreetingClassifier.GreetingClassifier ()
    # gclassifier= gclassifier_obj.greeting_classifier ()
    #cdo= bot.ChunkDetect.Chunk_Detector ()

    #
    # line= []
    # def __init__(self, line):
    #
    #     self.line= line
    #
    # def get_line (self):
    #
    #     return self.line
    #
    # def set_line (self, line):
    #
    #     self.line= line
    #
    # def classify (self):
    #
    #     if self.gclassifier.classify (self.gclassifier_obj.greeting_features (self.line [0]))== 'greeting' :
    #         return 'greeting'
    #
    #     elif (self.cdo.need_chunk1 (self.line) or self.cdo.need_chunk2 (self.line)) and (self.cdo.has_keyword (self.line)):
    #         return 'requirement'
