# encoding: utf-8
import csv
import os
import sys
import SeSG

from transformers import BertTokenizer, BertForMaskedLM


def main():
    """Main function."""

    global author

    levenshtein_distance = 4
    lda_iterations = 5000

    min_df_list = [0.1, 0.2, 0.3, 0.4]
    number_topics_list = [1, 2, 3, 4, 5]
    number_words_list = [5, 6, 7, 8, 9, 10]
    enrichment_list = [0, 1, 2, 3]

    author = 'hosseini'
    pub_year_one = 2016  # 0 = disable pub_year
    pub_year_two = 0  # 0 = disable pub_year
    qgs_size = 15
    gs_size = 46

    qgs_txt = 'files-qgs/%s-review/qgs-txt/metadata' % author

    # Running CERMINE (Change the path to the .jar file and to the input folder)
    # All the articles in .pdf format were hidden due to their publication restrictions.
    # print("Loading CERMINE...\n")
    # cermine = "java -cp cermine-impl-1.14-20180204.213009-17-jar-with-dependencies.jar " \
    #          "pl.edu.icm.cermine.ContentExtractor -path " \
    #          "/home/fuchs/Documentos/SeSG/files-qgs/%s-review/gs-pdf/ -outputs text" % author
    # os.system(cermine)

    print("Randomize QGS...\n")
    SeSG.randomize_qgs(qgs_size, gs_size, author)

    print("Doing Snowballing...\n")
    title_list, adjacency_matrix, final_edges = SeSG.snowballing(author)

    print("Loading BERT...\n")
    # Load pre-trained model tokenizer (vocabulary).
    bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Load pre-trained model (weights).
    bert_model = BertForMaskedLM.from_pretrained('bert-base-uncased')
    bert_model.eval()

    with open(os.path.join(sys.path[0], 'exits/%s-result.csv' % author), mode='w') as file_output:

        file_writer = csv.writer(file_output, delimiter=',')

        file_writer.writerow(['min_df', 'Topics', 'Words', 'Similar Words', 'No. Results',
                              'No. QGS', 'No. GS', 'No. Total'])

        for min_df in min_df_list:
            for number_topics in number_topics_list:
                for number_words in number_words_list:

                    print("Test with " + str(number_topics) + " topics and " + str(number_words) + " words in " + str(
                        min_df) + " min_df:")
                    print("\n")

                    dic, tf = SeSG.bag_of_words(min_df, qgs_txt)
                    lda = SeSG.lda_algorithm(tf, lda_iterations, number_topics)

                    for enrichment in enrichment_list:
                        string = SeSG.string_formulation(lda, dic, number_words, number_topics, enrichment,
                                                         levenshtein_distance, pub_year_one, pub_year_two,
                                                         bert_model, bert_tokenizer, author)

                        scopus_number_results = SeSG.scopus_search(string)

                        qgs, gs, result_name_list, manual_comparation = SeSG.open_necessary_files(author)
                        counter_one = SeSG.similarity_score_qgs(qgs, result_name_list, manual_comparation, author)
                        counter_two, list_graph = SeSG.similarity_score_gs(gs, result_name_list, manual_comparation,
                                                                           author)

                        counter_total = SeSG.graph(list_graph, title_list, adjacency_matrix, final_edges,
                                                   min_df, number_topics, number_words, enrichment)

                        file_writer.writerow(
                            [min_df, number_topics, number_words, enrichment, scopus_number_results, counter_one,
                             counter_two, counter_total])

                        print("String with " + str(enrichment) + " similar words: " + str(string))
                        print("Generating " + str(scopus_number_results) + " results with " +
                              str(counter_one) + " of the QGS articles, " + str(counter_two) +
                              " of the GS articles (without snowballing) and " + str(counter_total) +
                              " of the GS articles (with snowballing).")
                        print("\n")

    file_output.close()


if __name__ == "__main__":
    main()
