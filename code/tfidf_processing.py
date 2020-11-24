import pandas as pd
import numpy as np
import bs4 as bs

# load terms
masc_terms = pd.read_csv('./terms/terms_m.csv', header=None)
fem_terms = pd.read_csv('./terms/terms_f.csv', header=None)

# load postings
data = pd.read_csv('./data/data.csv')
j = len(data['job_description'])
out = open('./data/calculated_terms_tfidf.csv', mode='w', encoding="utf8")

print('job_title,masc,fem', file=out)
# for each posting, compute the number of terms that are used from the term lists
corpus = []
for i in range(j):
    jd = data['job_description'][i]
    jd_cleaned = bs.BeautifulSoup(jd, features="html.parser")
    jd_final = jd_cleaned.get_text().lower()
    corpus.append(jd_final)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=0.0005, max_df=0.9995)
X = vectorizer.fit_transform(corpus)
print(len(vectorizer.stop_words_))
print(len(vectorizer.get_feature_names()))
print(vectorizer.stop_words_)

