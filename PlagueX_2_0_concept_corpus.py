

# Class Features:
#    Objective: Creates a corpus of all the concepts used in all the documents and reduce the number of dimensions

#    ===>       Class Constructor     ====> input: multiple dictionaries each containing all unique nouns in each of the documents
#                                     ====> self.n_corpus      ==> List containing all unique nouns from all doucments.

#    ===>       reduced_corpus        ====> clusters similar nouns together in different lists 

#    ===>       doc_datagen           ====> generates a variant of each document containing only its concepts



import itertools
import random
from nltk.corpus import wordnet as wn
import PlagueX_2_0_tokenizer
class Concept_Corpus:
    def __init__(self,nfile):
        self.nfiles = nfile
        n_corpus = []
        for file in nfile:
            n_corpus+=file
        #Extract keys from each of the dictionaries and add them to a single list
        
        self.n_corpus = list(set(n_corpus))
        self.y_corpus = []
        self.x_corpus = {}
        for term in self.n_corpus:
            synset = wn.synsets(term)
            if synset == []:
                self.y_corpus.append([term])
            else:
                self.x_corpus[term]=synset
        #Removes repeated terms
        self.n_reduced = self.reduced_corpus()+self.y_corpus
        self.con_code = list(range(len(self.n_reduced)))
        self.doc_data = self.doc_datagen()
        
    def checksim(self,synset1,synset2):
        score = 0
        for syn1 in synset1:
            for syn2 in synset2:
                try:
                    ns = wn.lch_similarity(syn1,syn2)
                except:
                    ns = 0
    #            ns = wn.wup_similarity(syn1,syn2)
                if isinstance(ns, float):
                    if ns > score:
                        score = ns

    
        return(score)
    def reduced_corpus(self):
        n_reduced = []
        threshold = 2.029
        for key in self.x_corpus.keys():
            cflag = 0
            if n_reduced == []:
                n_reduced.append([key])
            else:
                for c, concept in enumerate(n_reduced):
                    eflag = 1
                    for term in concept:
                        if self.checksim(self.x_corpus[key],self.x_corpus[term]) < threshold:
                            eflag = 0
                    if eflag ==1:
                        current_concept = n_reduced[c]
                        current_concept.append(key)
                        n_reduced[c] = current_concept
                        cflag = 1
                        break
                if cflag == 0:
                    n_reduced.append([key])
                            
        return(n_reduced)
    def doc_datagen(self):
        doc_data = []
        for file in self.nfiles:
            noun_order = []
            for term in file:
                for i in range(len(self.n_reduced)):
                    if term in self.n_reduced[i]:
                        noun_order.append(self.con_code[i])
                        continue
            doc_data.append(noun_order)
        return(doc_data)
                    
                    
            
        
                        

#Raw_Text = "The ducks swim in the lake close to my home. There is a pond near my house, where the ducks swim. There is a lake close to my house, where the ducks swim."
#text1 = PlagueX_2_0_tokenizer.Tokenizer(Raw_Text)
#x = Concept_Corpus([text1.nounset,text1.nounset])
#print(x.n_reduced)
#print(x.con_code)
#print(x.doc_data)

