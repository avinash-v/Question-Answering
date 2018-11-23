import numpy as np
import collections
import string
import time

#Removing punctiation . we avoid using stopword removal as it may alter the articles too much , and performing the answer 
#similarity on them may turn out to be useless.(as we have answers with length 2-3 words too)

def stripPunc(txt):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    return txt.translate(table)

# Cosine Smilarity - as a benchmark test
def cosineSimilarity(txt_tokens_1, txt_tokens_2):
    # Count words and store them as a dictionary
    word_counts = collections.defaultdict(lambda: [0, 0])
    for word in txt_tokens_1:
        word_counts[word][0] += 1
    for word in txt_tokens_2:
        word_counts[word][1] += 1
    # Make vectors out of word count dictionary , for finding dot product
    v1 = []
    v2 = []
    #these vectors shall be a union of all the words present in both text segments (dimension = n1 + n2)
    for key in word_counts:
        v1.append(word_counts[key][0])
        v2.append(word_counts[key][1])

    # Return inner product of those word-vectors(cosine similarity formulae)
    return np.inner(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))



#the main function whiich determines if the answer is present in text 
def getAnswer(txt, question):
    txt = stripPunc(txt)          #
    question = stripPunc(question)# for removing punctuations from text and questions 
    tokenized_txt = txt.split(' ')      #
    tokenized_ques = question.split(' ')# Tokenizing both questions and answers
    Context_window = 5  # Contextwindow is used to to determine how many words we should pick up at once for cosine_sim  
    window_size = len(tokenized_ques) + Context_window
    max_sim = 0
    answer = None
    for i in range(len(tokenized_txt) - window_size):
        sim = cosineSimilarity(tokenized_ques, tokenized_txt[i:i + window_size])
        if sim > max_sim:
            max_sim = sim
            answer = tokenized_txt[i:i + window_size]
    
    return answer
#therefore the 'answer' string which is returned is of length (len(tokenized_ques) + Context_window) , and we 
#choose the best sequence of strings which might contain the answer we want . We are assuming that the answer shall 
#be present in the vicinity of where the question was picked from the text . Therefore we return the best possible string
# 'answer' from the text.















answer = getAnswer(paragraph["context"], question_answer["question"])