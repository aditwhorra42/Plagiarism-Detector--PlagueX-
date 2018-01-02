import os
import glob
import PlagueX_2_0_tokenizer
import PlagueX_2_0_concept_corpus
import PlagueX_2_0_mini_corpus
import PlagueX_2_0_sem_eval
import itertools
import sys
raw_text = []
filenames = []

def main(*texts):
    sys.stdout.write("1/4: \tTokenizing Data..... \r" )
    for i, text in enumerate(texts):
            filenames.append("text %d" % i)
            raw_text.append(text)
    file_combs =            list(itertools.combinations(range(len(raw_text)), 2))
    tokenized_objects =     list(map(lambda text: PlagueX_2_0_tokenizer.Tokenizer(text),raw_text))


    token_data =            list(map(lambda token_object: token_object.tokenized_text, tokenized_objects ))
    nounset_list =          list(map(lambda token_object: token_object.nounset, tokenized_objects ))

    sys.stdout.flush()
    print("1/4: \tTokenizing Data..... DONE \r" )
    sys.stdout.write("2/4: \tGenerating Concept Corpus..... \r" )

    noun_indices =          list(map(lambda token_object: token_object.noun_index, tokenized_objects ))
    primary_corpus = PlagueX_2_0_concept_corpus.Concept_Corpus(nounset_list)
    sys.stdout.flush()
    print("2/4: \tGenerating Concept Corpus..... DONE \r" )
    sys.stdout.write("3/4: \tGenerating Queries..... \r" )

    secodary_corpus = PlagueX_2_0_mini_corpus.Mini_Corpus(primary_corpus.doc_data,noun_indices)
    sys.stdout.flush()
    print("3/4: \tGenerating Queries..... DONE \r" )
    sys.stdout.write("4/4: \tSemantic Evalutation..... \r" )

    semantic_evaluation = PlagueX_2_0_sem_eval.Sem_Eval(secodary_corpus.query_data,token_data)
    final_scores = semantic_evaluation.score_data
    






    f = open('output.txt', 'w')

    for index, comb in enumerate(file_combs):
        f.write("="*100)
        f.write("\n")
        f.write("Detections between '%s' and '%s':" % (filenames[comb[0]],filenames[comb[1]]))
        f.write("\n")
        f.write("="*100)
        f.write("\n")
        f.write("\n")
        if final_scores[index] == []:
            f.write("\t\tNo Detections")
            f.write("\n")
        for match in final_scores[index]:
            f.write("\tA: \t'%s'" % match[0])
            f.write("\n")
            f.write("\tB: \t'%s'" % match[1])
            f.write("\n")
            f.write("\tScore:\t%r" % match[2])
            f.write("\n")
            f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")

    f.close()

    sys.stdout.flush()
    print("4/4: \tSemantic Evalutation..... DONE \r" )
    
    return([token_data,primary_corpus.n_corpus,primary_corpus.n_reduced,final_scores])




