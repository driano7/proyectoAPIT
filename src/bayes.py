from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

data = fetch_20newsgroups()
print(type(data.target_names))

categories = ['talk.religion.misc', 'soc.religion.christian',
              'sci.space', 'comp.graphics']

train = fetch_20newsgroups(subset='train', categories=categories)
print(train.data[0])
# test = fetch_20newsgroups(subset='test', categories=categories)
# # print(train.data[5])
# # print(type(train.target))
# model = make_pipeline(TfidfVectorizer(), MultinomialNB
#
# model.fit(train.data, train.target)
# labels = model.predict(test.data)
# print(labels)
