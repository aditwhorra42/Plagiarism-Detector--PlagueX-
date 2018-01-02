import concurrent.futures
import imp


os0=imp.load_module('os0', *imp.find_module('nltk'))
os1=imp.load_module('os1', *imp.find_module('nltk'))
os2=imp.load_module('os2', *imp.find_module('nltk'))
os3=imp.load_module('os3', *imp.find_module('nltk'))
os4=imp.load_module('os4', *imp.find_module('nltk'))
os5=imp.load_module('os5', *imp.find_module('nltk'))
os6=imp.load_module('os6', *imp.find_module('nltk'))




class MatchX:
    """The purpose of this class is to execute the main detection algorithms to
    output any instances of Plagiarism"""
    
    def __init__(self,datab,filenames):
        """This class is initiated with the tokenized data and
        the list of all filenames being processed

        Further, the tokenized data is split into all possible pairs
        depending on which text it comes from"""
    
        self.datab = datab
        self.filenames = filenames
        self.primelist = []
        self.pairlist = []
        for a in range(len(datab)):
            for b in range(len(datab)):
                if a==b:
                    continue
                else:
                    self.primelist.append((datab[a],datab[b],a,b))
                    self.pairlist.append((a,b))
                    
        
    def compare(self,text,lsx):
        """Takes the tokenized data of two texts,
        Compares each token of each sentence to the other,
        Calculates a score denoting how similar two word senses are, based on the shortest path that connects the senses
        and the maximum depth of the taxonomy in which the senses occur."""
        if lsx == 0:
            from os0.corpus import wordnet as wn
        elif lsx == 1:
            from os1.corpus import wordnet as wn
        elif lsx == 2:
            from os2.corpus import wordnet as wn
        elif lsx == 3:
            from os3.corpus import wordnet as wn
        elif lsx == 4:
            from os4.corpus import wordnet as wn
        elif lsx == 5:
            from os5.corpus import wordnet as wn
        elif lsx == 6:
            from os6.corpus import wordnet as wn
        else:
            print("Max workers set to 6")
            from os6.corpus import wordnet as wn
        
        T1 = text[0]
        T2= text[1]
        ind_T1 = text[2]
        ind_T2 = text[3]
        matchdata = []
        print(" Searching for matches between '"+self.filenames[ind_T1]+"' and '"+self.filenames[ind_T2]+"'....", end = " ")
        for a in range(len(T1)):
            S1 = T1[a]
            for b in range(len(T2)):
                S2 = T2[b]
                res = abs(len(S1)-len(S2))
                if res > len(S1) or res > len(S2):
                    continue
                sentrating = 0
                for W1 in range(len(S1)):
                    wrdrating = 0
                    for W2 in range(len(S2)):
                        if str(S1[W1])[-1] == ")" and str(S2[W2])[-1] == ")" and (str(S1[W1])[-6] == str(S2[W2])[-6]):
                            try:
                                temprating = wn.lch_similarity(S1[W1], S2[W2])
                            except:
                                continue
                                
                                                                                
                                                                                
                            try:
                                if temprating > wrdrating:
                                    wrdrating = temprating
                            except TypeError:
                                continue

                        elif str(S1[W1]) == str(S2[W2]):
                            wrdrating = 4
                            break
                    sentrating += wrdrating
                sentrating = sentrating/len(S1)
                if sentrating > 2.5:
                    
                    matchdata.append((sentrating,ind_T1,ind_T2,a,b,len(S1),len(S2)))
        print("*Done*")
        if matchdata == []:
            return(0)
        return(matchdata)


    
        
    def use_future(self,workers,primelist):
        """Takes the list containing all pairs of tokenized data and assigns each pair to a
        concurrent thread depending on the number of worker threads stated in the arguments.

        Further, a thread pool maps one text to all other texts using the COMPARE function and shares the load between threads accordingly"""
        lst= []
        for i in range(len(primelist)):
            lst.append(i%workers)
        print(lst)
        pool_02 = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
        resultsx = pool_02.map(self.compare,primelist,lst)
        return(list(resultsx))
        
        

    def run_normal(self,primelist):
        """Takes the list containing all pairs of tokenized data and further
          maps one text to all other texts using the COMPARE function"""
        lst= []
        for i in range(len(primelist)):
            lst.append(0)
            
        return(list(map(self.compare,primelist,lst)))
        
        
    def compare_prime(self, concurrency = False):
        

        
        
        if concurrency == False:
            return(self.run_normal(self.primelist))
        else:
            return(self.use_future(2,self.primelist))
        

        
    
        
                




                                      
                




                                      
                




                                      
                





                                      
                





                                      
                
