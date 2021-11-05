from nltk.corpus import stopwords as ntlk_stopwords
from sklearn.feature_extraction.text import CountVectorizer
from TextExtractor import TextExtractor
from sklearn.decomposition import LatentDirichletAllocation as LDA
import os
def test():
    stopwords=ntlk_stopwords.words("spanish")+ntlk_stopwords.words("english")
    counter=CountVectorizer(stop_words=stopwords)
    docs=[]
    TRAINING='./training'
    for area in os.listdir(TRAINING):
        print(f"Area: {area}")
        # aux=[]
        for file in os.listdir(TRAINING+'/'+area):
            if file[-3:]=='pdf':
                file=TextExtractor(TRAINING+'/'+area+'/'+file)
                text=file.getAllText(splited=False)
                # aux.append(text)
                docs.append(text)

    bag_of_words=counter.fit_transform(docs)
    NUM_LABELS=4
    NUM_WORDS=100
    lda = LDA(n_components=NUM_LABELS, n_jobs=-1)
    lda.fit(bag_of_words)
    words = counter.get_feature_names()
    for topic_index, topic in enumerate(lda.components_):
        print(f"\nTopic #{topic_index}:")
        print(" , ".join([words[i]
                        for i in topic.argsort()[:-NUM_WORDS - 1:-1]]))
