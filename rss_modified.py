import feedparser as fp
import json
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime
import pandas as pd


import collections
from collections import Counter


import gensim
import pkgutil
modules = pkgutil.iter_modules(gensim.__path__)
for module in modules:
    print(module[1])

from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()

from nltk.stem.porter import *
stemmer = PorterStemmer()


# Set the limit for number of articles to download
LIMIT = 1000

data = {}

with open('NewsPapers.json') as data_file:
    companies = json.load(data_file)

count = 1
i = 0

# Iterate through each news company
valid_data = []
articles=[]
for company, value in companies.items():
    # If a RSS link is provided in the JSON file, this will be the first choice.
    # Reason for this is that, RSS feeds often give more consistent and correct data.
    # If you do not want to scrape from the RSS-feed, just leave the RSS attr empty in the JSON file.
    if 'rss' in value:
        d = fp.parse(value['rss'])
        print("Downloading articles from ", company)
        # newsPaper = {
        #     "rss": value['rss'],
        #     "link": value['link'],
        #     "articles": []
        # }

        for entry in d.entries:
            # Check if publish date is provided, if no the article is skipped.
            # This is done to keep consistency in the data and to keep the script from crashing.
            if hasattr(entry, 'published'):
                if count > LIMIT:
                    break
                article = {}
                article['Source']=company
                article['link'] = entry.link
                date = entry.published_parsed
                article['published'] = datetime.fromtimestamp(mktime(date)).isoformat()
                article['title'] = entry.title
                article['summary'] = entry.summary
                try:
                    content = Article(entry.link)
                    content.download()
                    content.parse()
                except Exception as e:
                    # If the download for some reason fails (ex. 404) the script will continue downloading
                    # the next article.
                    print(e)
                    print("continuing...")
                    continue
                article['text'] = content.text


                
                def lemmatize_stemming(text):
                    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
                hello=[]
                for token in gensim.utils.simple_preprocess(content.text) :
                    if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                        hello.append(lemmatize_stemming(token))

                valid_data.append(hello)
                
                article['valid_data'] = valid_data[i]
                i=i+1


                articles.append(article)
                print(count, "articles downloaded from", company, ", url: ", entry.link)
                count = count + 1

                #valid_data.append(hello)

        data = articles
        #data1 = valid_data
        df = pd.DataFrame(data)
        #df1= pd.DataFrame(data1)
        df.to_csv("news27_rss.csv")
        df.drop_duplicates(subset="title",keep="first", inplace=True)
        #df1.to_csv("news27_rss.csv")





"""
lists_seen = set()  
outfile = open('neatoutput.txt', "w")
infile = open('Newsrssout.txt', "r")
print ("The file Newsrssout.txt is as follows")
for line in infile:
    print (line)
    if line not in lists_seen:  
        outfile.write(line)
        lists_seen.add(line)
outfile.close()
print ("The file neatoutput.txt is as follows")
for line in open('neatoutput.txt', "r"):
    print (line)



"""
