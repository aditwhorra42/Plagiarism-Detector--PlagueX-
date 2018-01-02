data = []
import statistics
import math
import numpy
import nltk
from nltk.corpus import wordnet as wn
f = open("Data_0_90.txt","r")
while True:
    sent = f.readline()
    if "END" in sent:
        break
    if len(sent) < 5:
        continue
    if sent[3]== " ":
        sent = sent[4:]
        data.append(sent)

print(data)

tokendata = []
for sent in data:
    pos = nltk.word_tokenize(sent)
    tokenized_text = nltk.pos_tag(pos)
    tokendata.append(tokenized_text)
    
    
corpus = []
for sent in tokendata:
    for token in sent:
        if token not in corpus:
            corpus.append(token)
idf = []           
for token in corpus:
    docs = 0
    for sent in tokendata:
        if token in sent:
            docs += 1
    idf.append(float(len(data)/docs))

    
nouns = []
pnouns = []
adjectives = []
adverbs = []
verbs = []
others = []
preps = []
conjs = []
for i, token in enumerate(corpus):
    if "NNP" in token[1]:
        pnouns.append(idf[i])
    elif "NN" in token[1] and token[1][0] == "N":
        nouns.append(idf[i])
    elif "RB" in token[1]:
        adverbs.append(idf[i])
    elif "JJ" in token[1]:
        adjectives.append(idf[i])
    elif "VB" in token[1]:
        verbs.append(idf[i])
    elif "PR" in token[1] or "IN" in token[1] or "CC" in token[1]:
        preps.append(idf[i])
        
def idf_gen(poslist):
    avg = sum(poslist)/len(poslist)
    sd = numpy.std(poslist)
    newlist = []
    for token in poslist:
        if abs(token-avg) < 2*sd:
            newlist.append(token)
    avg = sum(newlist)/len(newlist)
            
    return(avg)

noun_idf = idf_gen(nouns)
pnoun_idf = idf_gen(pnouns)
adjectives_idf = idf_gen(adjectives)
adverbs_idf = idf_gen(adverbs)
verbs_idf = idf_gen(verbs)
preps_idf = idf_gen(preps)


#median
#noun_idf = statistics.median(nouns)
#pnoun_idf = statistics.median(pnouns)
#adjectives_idf =statistics.median(adjectives)
#adverbs_idf =statistics.median(adverbs)
#verbs_idf = statistics.median(verbs)
#preps_idf = statistics.median(preps)
#
idf_list = [noun_idf,pnoun_idf,adjectives_idf,adverbs_idf,verbs_idf,preps_idf]
idf_list = list(map(lambda idfterm: ((idfterm - min(idf_list))/(max(idf_list)-min(idf_list))*0.7)+0.3,idf_list))


#print(noun_idf)
#print(pnoun_idf)
#print(adjectives_idf)
#print(adverbs_idf)
#print(verbs_idf)
#print(preps_idf)

print(idf_list)