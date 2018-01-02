import PlagueX_DisplayText
import PlagueX_Input
import PlagueX_token
import PlagueX_match
import PlagueX_outdata


import unittest

class TestStringMethods(unittest.TestCase):
    """This class contains various test methods that manually process data and
       assert it with the output processed by respective PlagueX function"""
    

   
    
    def test_Token_sentsplit(self):
        """Tests the method that splits a text into sentences.
        A raw text is defined within the function;
        It is processed by the Sentence Splitting methods of the Tokenize Class;
        The output list is further joined to a string on the basis of a <space> character
        and is checked if it remained the same as the original text"""
        text = "How are you? I am fine"
        self.sents = PlagueX_token.Tokenize(text).sentsplit
        print(self.sents)
        self.assertEqual((" ").join(self.sents()),text)

        


    
    def test_Match_sentmatch(self):
        """This function checks the overall working of the Plagiarism detection algorithm;
        Four sample texts of one sentence each are defined within the function such that:
            it is clearly evident to say which of the two texts mean the same and also
            how close their meanings are.
        Further, these texts are subjected to the same process:
            (POS_tag => Tokenize => TextPairs => Comparision => Score Calculation) as any texts would be
            and the output results (EXTREME , HIGH, or POSSIBLE match) are asserted with the expected results."""

        sample_text1 = "Yesterday,the policemen kept my money in the bank."
        sample_text2 = "My money was kept in the bank by the cops yesterday"
        sample_text3 = "Policemen will keep my money in the bank"
        sample_text4 = "Policemen will keep my donuts in the bank"
        #Expected detection
        #0:1,2: EXTREME
        #1:1,3: HIGH/Possible
        #2:1,4: Possible/No
        #3:2,1: EXTREME
        #4:2,3: possible/no
        #5:2,4: NO/possible
        #6:3,1: EXTREME/HIGH
        #7:3,2: HIGH/possible
        #8:3,4: HIGH/possible
        #9:4,1: POSSIBLE/no
        #10:4,2: POSSIBLE/no
        #11:4,3: High/possible
        expected_data = [["EXTREME"],["HIGH","POSSIBLE MATCH" ],["POSSIBLE MATCH",0 ],["EXTREME"],["POSSIBLE MATCH",0 ],
                         ["POSSIBLE MATCH",0 ],["HIGH","EXTREME" ],["HIGH","POSSIBLE MATCH" ],["HIGH","POSSIBLE MATCH" ],["POSSIBLE MATCH",0 ],["POSSIBLE MATCH",0 ],["HIGH","POSSIBLE MATCH" ]]
        cdata= []
        
        token_text1 = PlagueX_token.Tokenize(sample_text1)
        sents1 = token_text1.sentsplit()
        tokens1 = token_text1.token_split(sents1)

        token_text2 = PlagueX_token.Tokenize(sample_text2)
        sents2 = token_text2.sentsplit()
        tokens2 = token_text2.token_split(sents2)

        token_text3 = PlagueX_token.Tokenize(sample_text3)
        sents3 = token_text3.sentsplit()
        tokens3 = token_text3.token_split(sents3)

        token_text4 = PlagueX_token.Tokenize(sample_text4)
        sents4 = token_text4.sentsplit()
        tokens4 = token_text4.token_split(sents4)
        
        cdata.append(token_text1.tokenized_text())
        cdata.append(token_text2.tokenized_text())
        cdata.append(token_text3.tokenized_text())
        cdata.append(token_text4.tokenized_text())
        Analyze = PlagueX_match.MatchX(cdata,["a","b","c","d"])
        matchdata = Analyze.compare_prime(concurrency = False)
        A = PlagueX_outdata.Outdata(0,0,0,0)
        testdata = []
        for i in range(len(matchdata)):
            if matchdata[i]==0:
                testdata.append(0)
            else:
                x = matchdata[i][0]
                testdata.append(A.score_calc(x)[0])



        for i in range(len(testdata)):
            self.assertTrue(testdata[i] in expected_data[i])





    sample_sentence = ["Considering the fact that our intuition is a consequence of years of conditioning by societal and personal events, it is fair to say that the premise is not only subjective but it is also incorrect in that she does not, in fact, learn something new."]
    token_text = PlagueX_token.Tokenize(sample_sentence)
    tokens = token_text.token_split(sample_sentence)
    A = PlagueX_outdata.Outdata([sample_sentence],0,tokens,0)

    
    def test_Outdata_info_features(self):
        """The following function checks generation of the information about each text from the raw text data i.e:
            Character Count, Word Count, Sent Count, Average Sentence Length, Maximum Sentence length.
        A single sample sentence defined outside the class is taken.
        It is clearly evident that the number of sentences is 1,
        and the Total number of words = Average sentence length = Maximum sentence length = Number of spaces
        Therefore, the results which are easily obtained manually are asserted with the return values of the info_features method from the Outdata class"""
        a = len(self.sample_sentence[0])
        b = 0
        for i in self.sample_sentence[0]:
            if i== " ":
                b+=1
        # a = total number of characters since there is only one sentence.
        # b = total number of words because there is only one sentence.
        # b = average sentence length and also maximum sentence length
        # number of sentences = 1
        test_info = self.A.info_features(0)
        self.assertEqual(test_info, (a,b,1,b,b))
        
        


    def test_Outdata_main_concepts(self):
        """The following function tests the generation of "Most common terms" in each text:
            The sample text is tokenized and further passed into the function "main_concepts" of outdata class.
            This function returns the three most used terms in the text. (terms => nouns, foriegn word)

        The same text is manually filtered and
        only the tokens that are nouns (any type) and foriegn words are isolated;

        Now, we check if the return values of the initial function are
        repeated the most number of times by using the count() method."""
        
        terms = self.tokens
        terms = terms[0]
        filtered_terms = []
        for i in terms:
            if i[1][0]=="N" or  i[1][0]=="F":
                filtered_terms.append(i[0])
        terms = filtered_terms
        test_concepts = self.A.main_concepts()
        a_word = test_concepts[0]
        b_word = test_concepts[1]
        c_word = test_concepts[2]
        for i in range(len(terms)):
            self.assertTrue(terms.count(a_word)>=terms.count(terms[i]))
            
        for i in range(len(terms)):
            if terms[i]==a_word:
                continue
            self.assertTrue(terms.count(b_word)>=terms.count(terms[i]))

        for i in range(len(terms)):
            if terms[i]==a_word or terms[i]==b_word:
                continue
            self.assertTrue(terms.count(c_word)>=terms.count(terms[i]))




    Dtest = PlagueX_DisplayText.DisplayText()
    def test_DisplayText(self):
        """Because the methods of the DisplayText class have no arguments
        most of the times and are called multiple times to "ONLY" print data,
        they are checked to make sure they don't return anything"""
        self.assertEqual(self.Dtest.title(),None)
        self.assertEqual(self.Dtest.linebreak(),None)
        self.assertEqual(self.Dtest.file_prompt([]),None)
        self.assertEqual(self.Dtest.file_load(),None)
        self.assertEqual(self.Dtest.analysis(),None)
        self.assertEqual(self.Dtest.post_analysis(0),None)
        self.assertEqual(self.Dtest.MainOutput_Analysis("testfile",["a","b","c","d","e"],[0]),None)
        self.assertEqual(self.Dtest.MainOutput_Detections("testfile",[[0,"This is a sample test",2,3,"This is a sample text",5]]),None)
        
        
        
    def test_fileinput(self):
        """The following function checks the file processing methods of the fileinput class.
        The class' docxtract(), pdfxtract() methods are checked if their outputs are of type: String

        Further, the refined text(which is ideally a single line of text)
        is also checked if it has any linebreaks and tabspaces."""
        Ftest = PlagueX_Input.fileinput("D:\PlagueX\Test_File.docx")
        self.assertEqual(Ftest.name,"D:\PlagueX\Test_File.docx")
        self.assertTrue(isinstance(Ftest.docxtract(), str))
        Ftest = PlagueX_Input.fileinput("D:\PlagueX\Test_File.pdf")
        
        self.assertTrue(isinstance(Ftest.pdfxtract(), str))
        text = Ftest.textrefine()
        self.assertTrue("\n" not in text)
        self.assertTrue("\t" not in text)
        
    


if __name__ == '__main__':
    unittest.main()





        

        
        
            
        
        
    
