import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity

excel_file = 'elective_datasheet.xlsx'
data = pd.read_excel(excel_file)
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 3),min_df=0,stop_words='english')
tfidf_matrix = tf.fit_transform(data['Description'])
userInput = input()
tfidf_userInput = tf.fit(data["Description"])
queryTFIDF = tfidf_userInput.transform([userInput])
cosine_similarities = cosine_similarity(queryTFIDF, tfidf_matrix)
related_product_indices = cosine_similarities.argsort()[:-11:-1]
topIndices = related_product_indices[0][::-1]
for i in topIndices[0:5]:
	print(data.ix[i])


