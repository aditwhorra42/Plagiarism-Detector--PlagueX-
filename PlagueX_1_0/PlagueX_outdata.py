import concurrent.futures
import operator

class Outdata:
    """The purpose of this class is to filter and organize the raw data of a particular text,obtained
       from various methods involving Plagiarism Detections and Text Analysis"""
    
    def __init__(self, textdata, matchdata, tokendata, filenames):
        """The class is initiated by various chunks of data in respective nested lists"""
        self.textdata = textdata
        self.matchdata = matchdata
        self.tokendata = tokendata
        self.filenames = filenames

    def score_output(self):
        """Takes the raw matchdata of a particular text"""
        """Passes it to score_calc() to get a user-friendly score"""
        """Sorts the match data from from EXTREME Plagiarism to POSSIBLE Plagiarsm"""
        score_list = []
        for filepair in self.matchdata:
            if filepair == 0:
                continue
            for match in filepair:
                score = self.score_calc(match)
                score_raw = score[1]
                score_string = score[0]
                T1 = self.filenames[match[1]]
                T2 = self.filenames[match[2]]
                S1 = self.textdata[match[1]][match[3]]
                S2 = self.textdata[match[2]][match[4]]
                score_list.append((T1,S1,match[3],T2,S2,match[4],score_string,score_raw))
        score_list = sorted(score_list, key=operator.itemgetter(7), reverse=True)
        
        return(score_list)
            
            
            
            
            
    def score_calc(self,match):
        """Takes a specific match string and subjects it to
            different operations that handle instances like lenth_error
            and tags the matchstring with a keyword: EXTREME, HIGH or POSSIBLE"""
        if match == 0:
            return(0)
        score_scale = ["EXTREME","HIGH","POSSIBLE MATCH"]
        length_error = ((abs(match[-1]-match[-2]))/match[-2])
        score = match[0]-length_error
        score_string = ""
        if score > 3.3:
            score_string = score_scale[0]
        elif score > 2.7:
            score_string = score_scale[1]
        else:
            score_string = score_scale[2]

        return((score_string,score))

    def info_features(self,i):
        """Takes rawtext of a single file and
        outputs the following information:
            Number of Characters
            Number of words
            Number of sentences
            Maximum sentence length
            average sentence length"""
            
        
        rawtext = self.textdata[i]
        charcount = 0
        wordcount = 0
        sentcount = 0
        sentlengths = []

        sentcount = len(rawtext)
        for sent in rawtext:
            tempwc = 0
            for x in sent:
                if x== " ":
                    tempwc +=1
            charcount += len(sent)
            wordcount += tempwc
            sentlengths.append(tempwc)
        maxsentlength = max(sentlengths)
        avgsentlength = int(sum(sentlengths)/sentcount)
        

        return((charcount,wordcount,sentcount,maxsentlength,avgsentlength))

    def main_concepts(self):
        """Takes the tokendata of a particular text and
        outputs the most commonly used terms throughout the text"""
        text = self.tokendata
        tokenslist = []
        tokenscount = []
        for sent in text:
            for token in sent:
                if token[0] in tokenslist:
                    tokenscount[tokenslist.index(token[0])]+=1
                elif token[1][0]== "N" or token[1][0]== "F":
                    tokenslist.append(token[0])
                    tokenscount.append(1)

        sortedlist = [x for (y,x) in sorted(zip(tokenscount,tokenslist), reverse = True)]
        if len(sortedlist) <4:
            return(sortedlist)

        else:
            return(sortedlist[:4])

        
                    
                    
                
        
        
            
                
            
        
        
        
        
        
            

        
        
        
        
