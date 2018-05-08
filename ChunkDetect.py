import nltk

"""
detects chunks for understanding the sentence
"""
class Chunk_Detector:

    keywords= []
    chunkGrams= []


    """
    initializes list of chunks
    """
    def __init__(self, keywords):

        self.keywords= keywords
        self.chunkGrams.append (r"""Chunk: {<VB.?>+<PRP.?>*}""")
        self.chunkGrams.append (r"""Chunk: {<PRP.?>+<VB.?>*<TO><VB.?>}""")
        self.chunkGrams.append (r"""Chunk: {<WP><DT>*<VB.?>*<PRP.?>+}""")

    """
    checks for chunks which indicate user's requirement
    """
    def need_chunk_present (self, line):

        present= False
        words = nltk.word_tokenize (line)
        tagged = nltk.pos_tag (words)
        for chunkGram in self.chunkGrams:

            chunkParser = nltk.RegexpParser (chunkGram)
            chunked = chunkParser.parse (tagged)
            for subtree in chunked.subtrees ():

                if subtree.label () == 'Chunk':
                    present= present or True

        return present

    """
    checks if user input contains the domain word
    """
    def has_keyword (self, line):

        words= nltk.word_tokenize(line)
        for word in words:

            for x in self.keywords:

                if word== x:
                    return True
        return False

    # def need_chunk2 (self, line):
    #
    #     words = nltk.word_tokenize (line)
    #     tagged = nltk.pos_tag (words)
    #
    #     #chunkGram = r"""Chunk: {<PRP.?>+<VB.?>*<TO><VB.?>}"""
    #     chunkParser = nltk.RegexpParser (self.chunkGrams[1])
    #     chunked = chunkParser.parse (tagged)
    #
    #     for subtree in chunked.subtrees ():
    #
    #         if subtree.label () == 'Chunk': return True
    #     return False
    #
    # def need_chunk3 (self, line):
    #
    #     words = nltk.word_tokenize (line)
    #     tagged = nltk.pos_tag (words)
    #
    #     #chunkGram = r"""Chunk: {<WP><DT>*<VB.?>*<PRP.?>+}"""
    #     chunkParser = nltk.RegexpParser (self.chunkGrams [2])
    #     chunked = chunkParser.parse (tagged)
    #     chunked.draw()
    #     for subtree in chunked.subtrees ():
    #
    #         if subtree.label () == 'Chunk': return True
    #     return False
    #
    #  def need_classifier (self):
    #
    #    f = open ("requirement.txt", "r")
    #    f1 = open ("not_requirements.txt", "r")
    #    requirement= []
    #    not_requirement= []
    #
    #    text = ""
    #    for line in f:
    #
    #         text += line
    #         requirement = nltk.sent_tokenize (text)
    #
    #    text = ""
    #    for line in f1:
    #
    #       text += line
    #       not_requirement = nltk.sent_tokenize (text)
    #
    #    labels = ([ (line, 'req') for line in requirement] + [ (line, 'not req') for line in not_requirement])
    #    random.shuffle (labels)
    #
    #    feature_set = ( [ (self.need_features1 (l), check) for (l, check) in labels])
    #    print len (feature_set)
    #    print feature_set
    #
    #    train_set= feature_set [20:]
    #    test_set= feature_set [:20]
    #    need_classifier = nltk.NaiveBayesClassifier.train (train_set)
    #    print "need classifier accuracy:"
    #    print nltk.classify.accuracy (need_classifier, test_set)
    #
    #    assert isinstance(need_classifier, nltk.NaiveBayesClassifier)
    #    return need_classifier
