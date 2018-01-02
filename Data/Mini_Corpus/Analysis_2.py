from nltk.corpus import wordnet as wn
import nltk
import itertools
import operator

# Class Features:
#    Objective: Deeper analyis of the identified text range in between each of the documents and assigning score to each match.

#    ===>       Class Constructor       ====>  input:  query_data: data containing all text range between each of the documents with possible similarity
#                                              token_data: tokenized text from all documents

#    ===>       get_rawtext()           ====>  To get the original text from the tokenized list of the document.

#    ===>       compare()               ====>  Takes all words within the matched ranges for both documents as input and calculates the maximum direct match
#                                              score and part of speech score for each word in the document with greater length.                                 

#    ===>       getscore                ====>  Calculates the final score between two matches by giving weightages to match score and pos score and also
#                                              takes into account the weightage given to different parts of speeches.



def checksim(synset1,synset2):
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

def getweight(pos):
    weightlist = {"NN":0.77, "JJ":0.88, "RB": 0.76, "VB":0.90, "PR":0.30, "IN":0.30,"CC":0.30}
    if "NNP" in pos:
        return(1.0)
    elif pos[:2] in list(weightlist.keys()):
        return(weightlist[pos[:2]])
    else:
        return(0.1)
    
def scoregen(text1,text2):
     
    available_1 = text1
    available_2 = text2
    scores = []
    pairs = []
    for word in text1:
        max_score = 0
        for word2 in text2:
            try:
                score = checksim(wn.synsets(word[0]),wn.synsets(word2[0]))
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
                
        scores.append((max_score,getweight(word[1]),word))
    return(scores)
                
def getscore(text1,text2):
    score_data = scoregen(text1,text2)
#    print(score_data)
#    input()
    scores = list(map(lambda term: term[0]*term[1], score_data))
    weightlist = list(map(lambda term: term[1],score_data))
    return(round(sum(scores)/sum(weightlist),2))
        
    
    
            


def tokenize(sent):
    pos = nltk.word_tokenize(sent)
    tokenized_text = nltk.pos_tag(pos)
    return(tokenized_text)

tokensdata = []
f = open("Data_0_90.txt","r")
textdata = []
while True:
    data = []
    tdata = []
    sent = f.readline()
    if "END" in sent:
        break
    if len(sent) < 5:
        continue
    if "." in sent[:7]:
        sent = sent[4:]
        sent1 = f.readline()
        sent2 = f.readline()
        sent3 = f.readline()
        tdata.append(tokenize(sent))
        tdata.append(tokenize(sent1))
        tdata.append(tokenize(sent2))
        tdata.append(tokenize(sent3))

        data.append(sent)
        data.append(sent1)
        data.append(sent2)
        data.append(sent3)
    tokensdata.append(tdata)
    textdata.append(data)
pos_val = 0.4
word_val = 0.6
for i, sent in enumerate(tokensdata):
    print(textdata[i][0])
    print(textdata[i][1],"\t",getscore(sent[0],sent[1]) )
    print(textdata[i][2],"\t",getscore(sent[0],sent[2]) )
    print(textdata[i][3],"\t",getscore(sent[0],sent[3]) )
    input()
    print("\n\n")