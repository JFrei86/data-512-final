import pandas as pd
import numpy as np
import bs4 as bs

# load terms
masc_terms = pd.read_csv('./terms/terms_m.csv', header=None)
fem_terms = pd.read_csv('./terms/terms_f.csv', header=None)

# load postings
data = pd.read_csv('./data/data.csv')
j = len(data['job_description'])

# for each posting, compute the number of terms that are used from the term lists
for i in range(j):
    jd = data['job_description'][i]
    jd_cleaned = bs.BeautifulSoup(jd, features="html.parser")
    jd_final = jd_cleaned.get_text().lower().split()
    fem = 0
    masc = 0
    for term in jd_final:
        for m in masc_terms[0]:
            if term.startswith(m):
                masc += 1

        for f in fem_terms[0]:
            if term.startswith(f):
                fem += 1

    print(str(data['job_title'][i]).encode("utf-8"),str(masc),str(fem), sep=',')
