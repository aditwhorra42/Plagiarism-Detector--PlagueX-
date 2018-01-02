import nltk
class Tokenize:
    """The purpose of this class is to analyse the content of the refined text and"""
    """and return data that is further used for plagiarism detection"""

    sentx =[]
    

    
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    req_pos = ['FW','NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ']
    be_verb = ['have','is','are','am','be','were','been','have','had','do','did','done','say','said','said','tell','told','ask','asked','go',  'ok','see','saw','seen','use','used','find','found','give','gave','given','tell','tells','was','told','need','needed','become','became','leave','left','put','mean','meant','keep','kept','let','know']

    def __init__(self,input_text):
        """The init method of the class Tokenize takes the refined text as an argument"""
        """and initializes the attribute self.rawtext"""
        self.rawtext = input_text
        
                  

    def sentsplit(self):
        """Splits the refined text into sentences and returns a list containing"""
        """all the sentences in a text"""
        sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
        return(sent_tokenizer.tokenize(self.rawtext))

    def token_split(self,sents):
        """Takes the the list of all sentences for a file as input and returns"""
        """a list of tuples with each word and its part of speech"""
        tksents = []
        for sent in sents:
            pos = nltk.word_tokenize(sent)
            pos_sent = nltk.pos_tag(pos)
            tksents.append(pos_sent)
        return(tksents)
        

    def pos_split(self,pos_sent):
        """Takes a sentence containing word-POStag pairs, filters according to the required parts of"""
        """speech and also filters out the commonly used verbs so that they"""
        """are not checked for plagiarism and returns a sentence containing all the"""
        """synsets of each filtered word"""
        tempsent = []
        req_pos = ['FW','NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ']
        be_verb = ['have','is','are','am','be','were','been','have','had','do','did','done','say','said','said','tell','told','ask','asked','go',  'ok','see','saw','seen','use','used','find','found','give','gave','given','tell','tells','was','told','need','needed','become','became','leave','left','put','mean','meant','keep','kept','let','know']

        
        from nltk.corpus import wordnet as wn
        for x in pos_sent:
            if x[1] in req_pos and (x[0] not in be_verb):
                if x[1][0] == "N":
                    syn = wn.synsets(x[0],pos=wn.NOUN)
                    if syn == [] and x[0].istitle():
                        tempsent.append(x[0])
                    elif syn != []:
                        tempsent.append(syn[0])
                elif x[1][0] == "V":
                    syn = wn.synsets(x[0],pos=wn.VERB)
                    if syn == [] and x[0].istitle():
                        tempsent.append(x[0])
                    
                    elif syn != []:
                        tempsent.append(syn[0])
                else:
                    tempsent.append(x[0])
        return(tempsent)


    def tokenized_text(self):
        """Returns a list of all the synsets of all the required words of all the sentences"""
        sents = self.sentsplit()
        pos_sent = self.token_split(sents)
        return(list(map(self.pos_split,pos_sent)))
        
        



