import textwrap
import time
from threading import Timer
import sys







class DisplayText:
    """The purpose of this class is to print appropriate text to the user window whenever called by the PlagueX Class """
            
    def title(self):
        """Prints Title in ASCII Art"""
        self.linebreak()
        
        
        print("""                                                                                                                    
8 888888888o   8 8888                  .8.           ,o888888o.    8 8888      88 8 8888888888   `8.`8888.      ,8' 
8 8888    `88. 8 8888                 .888.         8888     `88.  8 8888      88 8 8888          `8.`8888.    ,8'  
8 8888     `88 8 8888                :88888.     ,8 8888       `8. 8 8888      88 8 8888           `8.`8888.  ,8'   
8 8888     ,88 8 8888               . `88888.    88 8888           8 8888      88 8 8888            `8.`8888.,8'    
8 8888.   ,88' 8 8888              .8. `88888.   88 8888           8 8888      88 8 888888888888     `8.`88888'     
8 888888888P'  8 8888             .8`8. `88888.  88 8888           8 8888      88 8 8888             .88.`8888.     
8 8888         8 8888            .8' `8. `88888. 88 8888   8888888 8 8888      88 8 8888            .8'`8.`8888.    
8 8888         8 8888           .8'   `8. `88888.`8 8888       .8' ` 8888     ,8P 8 8888           .8'  `8.`8888.   
8 8888         8 8888          .888888888. `88888.  8888     ,88'    8888   ,d8P  8 8888          .8'    `8.`8888.  
8 8888         8 888888888888 .8'       `8. `88888.  `8888888P'       `Y88888P'   8 888888888888 .8'      `8.`8888. """)

        print("\n\n")
        self.linebreak()
        return(None)

    def linebreak(self):
        """Prints line break in ASCII art"""
        print("="*115)
        return(None)
    def file_prompt(self,filenames):
        """Prints information on files in the directory"""
        print("PlagueX has detected %s supported\ntext files in the program directory:" % (str(len(filenames))))
        if filenames != []:
            for i in range(len(filenames)):
                print(str(i+1)+".) "+filenames[i],end = ", ")
            print("\n")
        return(None)
        
    def done(self):
        """Marks the completion of a process"""
        print("*Done*\n")
        return(None)
    def file_load(self):
        """Marks the initiation of file processing"""
        print("\n Processing files.....",end = " ")
        return(None)
    def analysis(self):
        """Marks the initiation of text analysis"""
        print("\n Analysing files......")
        return(None)
    def post_analysis(self,duration):
        """Marks the completion of the analysis and prints the total time taken"""
        print("~Analysis Completed~")
        print(" Time taken :",int(duration),"seconds")
        print("Press Enter to display results..\n")
        return(None)
        
    def MainOutput_Analysis(self,filename,info,terms):
        """Organizes results of Independent Analysis and prints them"""
        self.linebreak()
        print("\n    \t  "+"="*30+ "ANALYSIS: "+str(filename).upper()+"="*30)
        print("\n")
        print("\n")
        print("\t\t\t\t\t Total Characters:\t",info[0])
        print("\t\t\t\t\t Total words     :\t",info[1])          
        print("\t\t\t\t\t Total Sentences :\t",info[2])
        print("\t\t\t\t\t Average \n\t\t\t\t\t Sentence Length :\t",info[4],"words")
        print("\t\t\t\t\t Maximum \n\t\t\t\t\t Sentence Length :\t",info[3],"words")
        print("\t\t\t\t\t Most used terms :\t",end = " ")
        for t in terms:
            print(t,end = ", ")
        print("\n")
        print("\n")
        return(None)
    
    def MainOutput_Detections(self,filename,matches):
        self.linebreak()
        """Organizes results of Plagiarsm Matches and prints them"""
        print("\n    \t  "+"="*30+ "PLAGIARISM DETECTIONS: "+str(filename).upper()+"="*30)
        print("\n")
        print("\n")
        for match in matches:
            print("\tPriority : ",match[-2],"\n")
            print("\t"+str(match[0])+"(Sentence No. "+str(match[2])+"):")
            
            try:
                print("\t",str(match[1]))
            except UnicodeEncodeError:
                print("\t",str(match[1].encode('utf-8')))
            print("\n")
            print("\t"+str(match[3])+"(Sentence No. "+str(match[5])+"):")
            try:
                print("\t",str(match[1]))
            except UnicodeEncodeError:
                print("\t",str(match[4].encode('utf-8')))
            print("~"*95,"\n\n")

        return(None)
            
              
              
              
              
        
            
        
        
        
        
        
        
    
        


