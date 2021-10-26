

#%%
def most_used_words(text):
    tokens = word_tokenize(text)
    frequency_dist = nltk.FreqDist(tokens)
    print("There is %d different words" % len(set(tokens)))
    return sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)


# In[10]:


from nltk.corpus import stopwords

#nltk.download("stopwords")

mword = most_used_words(str1)
themost = []
for w in mword:
    if len(themost) == 100:
        break
    if w in stopwords.words("english"):
        continue
    else:
        themost.append(w)


# In[11]:


print("themost",sorted(themost,reverse=True))
