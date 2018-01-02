"""This module contains the main class "PlagueX" that imports other required classes and
    combines their functionalities to get the final analysis."""
    
import os
import sys
import PlagueX_DisplayText
import PlagueX_Input
import PlagueX_token
import PlagueX_match
import PlagueX_outdata
import time
import pydoc                                                                                                                     


class PlagueX:
    """The purpose of this class is to import other required classes and
    combine their functionalities to get the final analysis"""
    
    filenames = []
    """Contains all filenames of the text files in the program directory."""
    sentdata = []
    """A Nested list containing the sentences of each textfile"""
    tokendata = []
    """A nested list containing tuples of each word with it's respective
       part of speech for each sentence of each text."""
    comparedata = []
    """A nested list containing Synsets of words with required POS from each sentence of each text"""
    matchdata = []
    """A nested list containing all the possible sentence combinations between each text.
       Every element of the sublist is a tuple containing 7 elements:
       1. Index of Text-1
       2. Index of Text-2
       3. Index of Sentence-1 in Text-1
       4. Index of Sentence-2 in Text-2
       5. Length of Sentence-1
       6. Length of Sentence-2
       7. Average_Similarity_Index between Sentence-1 and Sentence-2"""
       
    pairlist = []
    """Contains all possible binary combinations between files:
       Eg: Number of files: 3  => T1 , T2, T3
       pairlist contains T1-T2, T1-T3, T2-T1, T2-T3, T3-T1, T3-T2"""
    
    filecount = 0
    """ len(filenames): stores value of the number of files"""
    
    def __init__(self):
        """The PlagueX class does not take any arguments but instead initializes classes from other modules and combines the functionalities."""
        """The init class has no return value """
        self.display = PlagueX_DisplayText.DisplayText()
        """Initializes the DisplayText class"""
        self.display.title()
        """Prints the title on program window"""
        self.Process_Files()
        """Runs Process_Files function"""
        self.Analyze_Files()
        """Runs Analyze_Files function"""
        self.Get_Analysis()
        """Runs Get_Analysis function"""
        



    def Process_Files(self):
        """The following function extracts the text from the text files in the program directory, refines them, splits them into sentences, tokenizes them
           and appends the data to respective pre-defined lists."""
        
        for file in os.listdir():
            """Iterate through a list of all files in the program directory"""
            if (file.endswith(".docx") or file.endswith(".pdf")) and not file.startswith("~"):
                self.filenames.append(file)
                """Adds the names of valid and supported text-files the list containing all filenames"""
                
        self.display.file_prompt(self.filenames)
        if len(self.filenames)<2:
            print("Insufficient Input Files:\nPlease place more than one text files (.pdf or .docx) in the program directory.")
            input()
            sys.exit()
            """Check if there are atleast 2 valid and supported text files in the current directory. Exception Raise exits the program"""
            
        self.display.file_load()
        
                
        for file in self.filenames:
            try:
                input_text = PlagueX_Input.fileinput(file)
                if input_text.fileconvert() == 0 or len(input_text.fileconvert()) < 25:
                    print("\n file: "+file+" is either corrupted or too short for PlagueX to apply the detection algorithm.")
                    input(sys.exit())
                """Raw-text is obtained by initializing class "Fileinput" from module "PlagueX_Input" and using the fileconvert() method"""
                """Check if the obtained text is corrupted or too small for comparision. Exception Raise exits the program"""
                
            except:
                print("\n file: "+file+" is either corrupted or too short for PlagueX to apply the detection algorithm.")
                input(sys.exit())
                
            refined_text = input_text.textrefine()
            """Gets all text of a single-textfile in a single-line without headers,footers,pagenumbers,titles,headings,and any invalid strings"""
            token_text = PlagueX_token.Tokenize(refined_text)
            """Initializes the class "Tokenize" from module "PlagueX_token" with the refined_text as Argument"""
            sents = token_text.sentsplit()
            """Splits the refined_text into sentences"""
            tokens = token_text.token_split(sents)
            """converts each word into a tuple-pair with the word and it's respective POS-tag"""
            self.sentdata.append(sents)
            """appends sentences-list of each file to the predefined list: sentdata"""
            self.tokendata.append(tokens)
            """appends (word,pos)-list of each file to the predefined list: tokensdata"""
            self.comparedata.append(token_text.tokenized_text())
            """appends tokenized-sentences-list of each file to the predefined list: comparedata"""
        self.filecount = len(self.filenames)
        """Update the value for the number of files being compared"""
        
        
        self.display.done()
        return(None)
        

    def Analyze_Files(self):
        """The following function executes the main Plagiarism detection iterations"""
        start = time.time()
        self.display.analysis()
        Analyze = PlagueX_match.MatchX(self.comparedata,self.filenames)
        """Initializes the class "MatchX" from module "PlagueX_match" """
            
        self.matchdata = Analyze.compare_prime(concurrency = False)
        """Executes the main comparision function which returns data containing
        the adressess of respective sentences, their lengths and their Similarity Index"""
        self.pairlist = Analyze.pairlist
        duration = time.time()-start
        self.display.post_analysis(duration)
        return(None)
        
        
    def Get_Analysis(self):
        """This function takes the data that is stored in the pre-defined lists as a result of the execution of previous functions
         and processes it to get user-displayable results"""

        
        for i in range(len(self.filenames)):
            Analysis = PlagueX_outdata.Outdata(self.sentdata,self.matchdata[i*(self.filecount-1):(i+1)*(self.filecount-1)],self.tokendata[i],self.filenames)
            TextInfo = Analysis.info_features(i)
            TermsUsed = Analysis.main_concepts()
            self.display.MainOutput_Analysis(self.filenames[i],TextInfo,TermsUsed)
        for i in range(len(self.filenames)):
            Analysis = PlagueX_outdata.Outdata(self.sentdata,self.matchdata[i*(self.filecount-1):(i+1)*(self.filecount-1)],self.tokendata[i],self.filenames)
            PlagMatches = Analysis.score_output()
            self.display.MainOutput_Detections(self.filenames[i],PlagMatches)
        return(None)
            

            
            
            
            
            
        

        
        
                
                
                
                
                
                

                
                
