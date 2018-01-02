from nltk.corpus import wordnet as wn
import itertools


# Class Features:
#    Objective: Deeper analyis of the identified text range in between each of the documents and assigning score to each match.

#    ===>       Class Constructor       ====>  input:  query_data: data containing all text range between each of the documents with possible similarity
#                                              token_data: tokenized text from all documents

#    ===>       get_rawtext()           ====>  To get the original text from the tokenized list of the document.

#    ===>       compare()               ====>  Takes all words within the matched ranges for both documents as input and calculates the maximum direct match
#                                              score and part of speech score for each word in the document with greater length.                                 

#    ===>       getscore                ====>  Calculates the final score between two matches by giving weightages to match score and pos score and also
#                                              takes into account the weightage given to different parts of speeches.



class Sem_Eval:
    def __init__(self, query_data, token_data):
        
        self.score_data = []
        
        self.doc_combs = list(itertools.combinations(range(len(token_data)), 2))
        for index, comb  in enumerate(query_data):
            comb_scores = []
            for match in comb:
                try:
                    text1 = token_data[self.doc_combs[index][0]][match[0][0]:match[0][1]+1]
                except:
                    text1 = token_data[self.doc_combs[index][0]][match[0][0]:match[0][1]]
                try:
                    text2 = token_data[self.doc_combs[index][1]][match[1][0]:match[1][1]+1]
                except:
                    text2 = token_data[self.doc_combs[index][1]][match[1][0]:match[1][1]]
                
                if len(text1) < 4 or len(text2) < 4:
                    continue
                if len(text1) > len(text2):
                    text1,text2 = text2,text1
                score = self.getscore(text1,text2)
                if score > 0:
                    comb_scores.append((self.get_rawtext(text1),self.get_rawtext(text2),self.getscore(text1,text2)))
            self.score_data.append(comb_scores)
    def get_rawtext(self,text):
        return(" ".join(list(map(lambda token: token[0],text))))
    
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

    def getweight(self,pos):
        weightlist = {"NN":0.77, "JJ":0.88, "RB": 0.76, "VB":0.90, "PR":0.30, "IN":0.30,"CC":0.30}
        if "NNP" in pos:
            return(1.0)
        elif pos[:2] in list(weightlist.keys()):
            return(weightlist[pos[:2]])
        else:
            return(0.1)

    def scoregen(self,text1,text2):
        

        available_1 = text1
        available_2 = text2
        scores = []
        pairs = []
        for word in text1:
            max_score = 0
            for word2 in text2:
                try:
                    score = self.checksim(wn.synsets(word[0]),wn.synsets(word2[0]))
                    score = score/3.63
                    if score > 1:
                        score = 1
                except:
                    if word == word2:
                        score = 1
                    else:
                        score = 0
                if score == 0 and word == word2:
                    score = 1
                if score > max_score:
                    max_score = score

            scores.append((max_score,self.getweight(word[1]),word))
        return(scores)

    def getscore(self,text1,text2):
        score_data = self.scoregen(text1,text2)
    #    print(score_data)
    #    input()
        scores = list(map(lambda term: term[0]*term[1], score_data))
        weightlist = list(map(lambda term: term[1],score_data))
        text2_weight = sum(map(lambda pos: self.getweight(pos), list(map(lambda term: term[1],text2))))
        text1_weight = sum(weightlist)
        weight = (text2_weight+text1_weight)/2
            
        
        return(round(sum(scores)/weight,2))


