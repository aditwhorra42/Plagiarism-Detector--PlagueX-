import itertools
import PlagueX_2_0_tokenizer
import PlagueX_2_0_concept_corpus

# Class Features:
#    Objective: Identifies a text range in between each of the documents that share similar concepts for deeper analysis.

#    ===>       Class Constructor     ====> input:  doc_data: documents listed by their concept_codes
#                                                   noun_index: identify positions of specific nouns in the document

#    ===>       match_detect()        ====> identifies the positions at which any two documents use the same concept keyword

#    ===>       match_range()         ====> uses the position given by match_detect() to recursively generate a possible range of texts in each
#                                            of the documents that might be similar.

#    ===>       mini_queries          ====> Use the outputs of match_range() to locate the corresponding query in each of the two documents
#                                            that might be declared plagiarised upon further analysis.





class Mini_Corpus:
    def __init__(self, doc_data, noun_index):
        self.noun_index = noun_index
        self.doc_data = doc_data
        self.doc_combs = list(itertools.combinations(range(len(self.doc_data)), 2))
        self.match_data = self.match_detect()
        self.query_data = self.mini_queries(self.match_data)
        
    def match_detect(self):
        
        match_data = []
        for comb in self.doc_combs:
            matches = []
            for index_x, code_x  in enumerate(self.doc_data[comb[0]]):
                for index_y , code_y in enumerate(self.doc_data[comb[1]]):
                    if code_x == code_y:
                        matches.append((index_x, index_y))
            match_data.append(self.match_range(matches))
        return(match_data)
    
    
    def match_range(self,match_data):
        self.used = [[],[]]
#        self.used = []
        match_ranges = []    
        def range_gen(elmx,match_data):
            int_elmx = elmx
            for match in match_data:
                
                if match[0] not in self.used[0] or match[1] not in self.used[1]:
#                if match not in self.used:
                    if match[0]-elmx[-1][0] > 0 and match[0]-elmx[-1][0] < 3 and match[1]-elmx[-1][1] > 0 and match[1]-elmx[-1][1] < 3:
                        elmx.append(match)
                        self.used[0].append(match[0])
                        self.used[1].append(match[1])
#                        self.used.append(match)
                        return(range_gen(elmx,match_data))
            return(elmx)
        for element in match_data:
            if element[0] not in self.used[0] or element[1] not in self.used[1]:
#            if element not in self.used:
                elmx = []
#                self.used.append(element)
                self.used[0].append(element[0])
                self.used[1].append(element[1])
                elmx.append(element)
                rangex = range_gen(elmx,match_data)
                if len(rangex) >1:
                    match_ranges.append((rangex[0],rangex[-1]))
        return(match_ranges)
    
    
    def mini_queries(self,match_data):
        query_data = []
        for i in range(len(match_data)):
            comb_queries = []
            comb = match_data[i]
            d1 = self.doc_combs[i][0]
            d2 = self.doc_combs[i][1]
            for rangex in comb:
                if rangex[0][0] != 0:
                    r1 = int(rangex[0][0]) - 1
                else:
                    r1 = rangex[0][0]
                if rangex[0][1] != 0:
                    r3 = int(rangex[0][1]) - 1
                else:
                    r3 = rangex[0][1]
                if rangex[1][0] < len(self.noun_index[d1])-1:
                    r2 = int(rangex[1][0]) + 1
                else:
                    r2 = rangex[1][0]
                if rangex[1][1] < len(self.noun_index[d2])-1:
                    r4 = int(rangex[1][1]) + 1
                else:
                    r4 = rangex[1][1]

                try:
                    newrange = ((self.noun_index[d1][r1],self.noun_index[d1][r2]),(self.noun_index[d2][r3],self.noun_index[d2][r4]))
                except:
                    print(d1,"\n",d2)
                comb_queries.append(newrange)
            query_data.append(comb_queries)
        return(query_data)
            
            
            
        
        

#Un-comment below text to check code-integrity   
#Raw_Text = "Along with the degradation of labor, Gandhi believes that capitalism imbues greediness in every human being. The introduction of machinery makes man a limitless consumer of commodities leading to the multiplication of wants and desires. This further leads to unhealthy competition which ultimately results in violence. Therefore, he believes that violence is inherently embedded in the western civilization which promotes capitalism and hence considers capitalism to be immoral, driven only by comforts and bodily welfare"
#
#
#Raw_Text2 = "According to Gandhi's beliefs, alongside degradation of labor, capitalism also permeates greediness in all humans. Induction to machinery makes humans boundless users of commodities which results in growth of needs and desires. Further, this results in unhealthy competition which eventually leads to brutality. Thus, he concludes that capitalism is unethical and is driven just by comfort and personal well being as violence is innately implanted in western ideologies which promotes capitalism "
#
#
#text1 = PlagueX_2_0_tokenizer.Tokenizer(Raw_Text)
#text2 = PlagueX_2_0_tokenizer.Tokenizer(Raw_Text2)
#
#a1 = text1.tokenized_text
#a2 = text2.tokenized_text
#x = PlagueX_2_0_concept_corpus.Concept_Corpus([text1.nounset,text2.nounset])
#
#y = Mini_Corpus(x.doc_data,[text1.noun_index,text2.noun_index]) 
#print(y.match_data)
#print("hey")
#print(y.query_data)
#

