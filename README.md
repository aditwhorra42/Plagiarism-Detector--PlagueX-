# CS309-IR-Monsoon-2017-Brogrammers
Siddhant Bhargava, Adit Whorra, Koushik Varma 


PLAGUEX 2.0

Dependecies: 
Python 3.0 or above, NLTK 3.2.5, WordNet 3.1

Installation Instructions: 
1. Clone current repository
2. Installing NLTK:
    a) with Python installed, open CMD in Windows or Terminal in MAC
    b) execute the following command "pip install nltk"
3. Installing WordNet: 
    a) With Python terminal opened on CMD/Terminal/external_IDE
    b) "import nltk"
    c) "nltk.download()"
    d) choose WordNet from list of NLTK libraries
4. Detecting Plagiarism in a custom set of documents:
    a) Place any number of documents in the "Test Cases" folder
    b) Execution may take longer durations of time for more than 30 documents.
5. Execute "main.py" from CMD/Terminal/External_IDE


   Objectives:
   
   Compare two or more documents for Plagiarism in language, thoughts, ideas or expressions.
   
        1. Generate a match-score on variable query size (starting from phrase-level to document level) between two documents
        
            a . Generate a match-score between two queries:
          
              SUB GOALS:
              
              i. Process Text ................ DONE
              
              ii. Create Corpus............... DONE (Local Corpus needs to be created)
              
              iii. Determine weights...........DONE
              
              iv. implement a distance algorithm.
              Secondary Goals: Try to access WordNet without NLTK as it can save us a lot of computational time.......SOLVED
              
            b. Create an algorithm to grow the query size upon matching of the smallest query set............TREE_ALGORITHM CREATED
            
        2. Determine the threshold match-score for the query to be classified as Plagiarised........TO BE DONE USING DATASET AND CLASSIFICATION

    
    