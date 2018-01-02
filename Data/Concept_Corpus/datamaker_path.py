
f=open("PlagueX_SynAnts.txt", 'r')
raw_text = f.read()
raw_text.strip("-")
import nltk
from nltk.corpus import wordnet as wn
pos = nltk.word_tokenize(raw_text)
import datetime
import random
syn = {}
ant = {}

act = 0
temp = []
main = ""
syn[main] = ""
ant[main] = ""
for i in range(len(pos)):
    if i == 0:
        continue
    if act == 0:
        if pos[i-1] == "." and pos [i+1] == "." and pos[i] != "ANT":
            act = 1

            main = pos[i]
            continue
    if act == 1 or act ==2:
        if (pos[i-1] == "." or pos[i-1] == ",") and (pos[i+1] == "," or pos[i+1] == ".") and pos[i] != "ANT":
            term = pos[i]
            temp.append(term)
            if pos[i+1] == ".":
                if act == 2:
                    ant[main] = temp
                    act = 0
                    temp = []
                else:
                    syn[main] = temp
                    act = 2
                    temp = []
                    
                    
def checksim(synset1,synset2):
    score = 0
    for syn1 in synset1:
        for syn2 in synset2:
            ns = wn.path_similarity(syn1,syn2)
#            ns = wn.lch_similarity(syn1,syn2)
#            ns = wn.wup_similarity(syn1,syn2)
            if isinstance(ns, float):
                if ns > score:
                    score = ns

    
    return(score)

numb = 0
x = datetime.datetime.now()

f = open('path.txt', 'w')
for term in syn.keys():
    testset = list(random.sample(range(1, len(syn)), 300))
    print(term)
    for synx in syn[term]:
        f.write("1,"+","+str(round(checksim(wn.synsets(term),wn.synsets(synx)), 2))+"\n")
    for indexx in testset:
        f.write("0,"+","+str(round(checksim(wn.synsets(term),wn.synsets(list(syn.keys())[indexx])), 2))+"\n")
f.close()
