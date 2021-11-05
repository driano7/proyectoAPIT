from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd
import os
labels_path='./training'


stopwords=stopwords.words("spanish")

cv = CountVectorizer(stop_words=stopwords)
print(type(cv),cv)
data_cv = cv.fit_transform(data_clean.transcript)

os.list():
with open()
'''
# data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
# data_dtm.index = data_clean.index

# data_dtm.to_pickle("dtm.pkl")
# Let's also pickle the cleaned data (before we put it in document-term matrix format) and the CountVectorizer object
data_clean.to_pickle('data_clean.pkl')
pickle.dump(cv, open("cv.pkl", "wb"))

data_dtm
'''
