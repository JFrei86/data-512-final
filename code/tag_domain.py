import pandas as pd
import numpy as np
import bs4 as bs
import re

# load postings
data = pd.read_csv('./data/data.csv')

# rule-based system for categorizing job posts
retail = data['job_title'].str.contains('shift.*manager|shift.*lead|store.*lead|store.*manager|sales.*associate|sales.*assistant|sales.*representative|sales engineer|sales.*agent|sales.*pro|sales consultant|sales special|sales rep|service.*representative|sales executive|support specialist|customer service|retail|part-time associate|full-time center associate|general manager|salesperson', flags=re.IGNORECASE, regex=True)
engineering = data['job_title'].str.contains('(?<!sales )engineer|data analyst|scientist|aws|azure|google|cloud|(?<!business )developer|product manager|program manager|technician|tech|chemist|solutions? architect|data architect|project manager', flags=re.IGNORECASE, regex=True)
marketing = data['job_title'].str.contains('marketing|Sales Development Representative|account rep|account manager|account executive|accounts manager|analyst', flags=re.IGNORECASE, regex=True)
business = data['job_title'].str.contains('financ|teller|branch manager|accounting|accounts payable|accounts receivable|recruit|human resource|executive assistant|concierge|administrative assistant|office manager|accountant|tax preparer|tax manager|business developer|business development|business analyst|sales manager|customer su|front|reception', flags=re.IGNORECASE, regex=True)
realestate = data['job_title'].str.contains('property manager|real estate|rental consultant|lease|leasing|mortgage', flags=re.IGNORECASE, regex=True)
creative = data['job_title'].str.contains('stylist|photo|designer|barber|beauty consultant|beauty specialist|beauty advisor', flags=re.IGNORECASE, regex=True)
medical = data['job_title'].str.contains('nurse|clinical|medical assistant|rn l|pharmacist|patient', flags=re.IGNORECASE, regex=True)
leadership = data['job_title'].str.contains('(?<!assistant to )VP|vice president|president|cfo|ceo|director|manager,', flags=re.IGNORECASE, regex=True)

# for analyzing overlap from the above rules
#print(data['job_title'][np.logical_and(retail,marketing)])

# filter by rules
job_category = retail.copy()
job_category.loc[retail] = 'retail/sales'
job_category.loc[engineering] = 'engineering'
job_category.loc[marketing] = 'marketing'
job_category.loc[business] = 'business'
job_category.loc[realestate] = 'realestate'
job_category.loc[creative] = 'creative'
job_category.loc[medical] = 'medical'
job_category.loc[leadership] = 'leadership'
job_category.loc[job_category == False] = 'ambiguous'
print(job_category)

data['job_category'] = job_category
data.to_csv('./data/data_augmented.csv')
(data['job_title'][~np.logical_or(np.logical_or(np.logical_or(np.logical_or(np.logical_or(np.logical_or(np.logical_or(engineering,business),retail),realestate),creative),medical),leadership),marketing)]).to_csv('./remaining.csv')