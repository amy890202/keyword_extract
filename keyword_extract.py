from rake_nltk import Rake
import nltk
import re
from nltk.tokenize import word_tokenize
# Uncomment this line if you haven't downloaded punkt before
# or just run it as it is and uncomment it if you got an error.
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt')
#nltk.download('all')
#r = Rake()

import pandas as pd 

X = pd.read_csv("olist_order_reviews_dataset_translate.csv",encoding="ISO-8859-1")
comment = X.iloc[0:100,4:5]
str1 = ''
for j in range(len(comment["review_comment_message"])):
    text = comment["review_comment_message"][j]
    #str1 = str1 + text
#print(str1)
#%%
from rake_nltk import Metric, Rake
from nltk.corpus import stopwords
# 要將其與nltk支持的特定語言一起使用
#r = Rake(language='english')

# 如果您想提供自己的停用詞和標點符號，例如(is,a,to,did...等等)
# =============================================================================
# r = Rake(
#     stopwords = stopwords.words("english"),
#     punctuations=',.'
# )
# 
# =============================================================================
# 如果要控制排名指標。使用d（w）/ f（w）作為指標，可以將此API與以下指標結合使用：
# 1. d(w)/f(w) (Default metric) Ratio of degree of word to its frequency.
# 2. d(w) Degree of word only.
# 3. f(w) Frequency of word only.

r = Rake(language='english',stopwords = stopwords.words("english"),
    punctuations=',.!',ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO,min_length=1, max_length=5)
#r = Rake(ranking_metric=Metric.WORD_DEGREE)
#r = Rake(ranking_metric=Metric.WORD_FREQUENCY)

#如果您想控制詞組中的最大或最小詞，將其設為考慮排名，以Rake實例：

#r = Rake(min_length=1, max_length=4)
#text = " The product arrived in perfect condition and before the deadline established. The good product and reached my expectations"
#str1 = re.sub(r'[^\w\s]','',str1)
#rake_nltk_var.extract_keywords_from_text(str1)
for j in range(len(comment["review_comment_message"])):
    text = comment["review_comment_message"][j]
#r.extract_keywords_from_text(text)
#keyword_extracted = r.get_ranked_phrases()
    r.extract_keywords_from_text(text)
    keyword_score = r.get_ranked_phrases_with_scores()
#print("keyword",keyword_extracted)
    #print("keyword",type(keyword_score),keyword_score)
    if keyword_score:
        maxscore = keyword_score[0][0]
        keyword = keyword_score[0][1]
# =============================================================================
#         for i in keyword_score:
#             if i[0]>maxscore:
#                 maxscore = i[0]
#                 keyword = i[1]
# =============================================================================
        print(keyword)
            
