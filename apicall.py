import requests
import boto3
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import json
import tempfile
from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()


url = ('https://newsapi.org/v2/everything?'
       'q=Economy&'
       'sources=bbc-news,the-hindu,abc-news&'
       'from=2019-09-05&'
       'sortBy=popularity&'
       'apiKey=5579350968fb43f6861a0db1b887235c')

response = requests.get(url).json()

t="Newso.json"

f = open(t,"a")
print(response,file=f)
f.close()

json_results = int(response['totalResults'])

print(json_results)

noise_list = ["is", "a", "this", "..."]
my_list = []
final_list = []
for i in range(0,20):
    json_link = response['articles'][i]['url']
    my_list.append(json_link)

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)
def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    for i in range(20):
        url = my_list[i]
        response1 = simple_get(url)

        if response1 is not None:
            html = BeautifulSoup(response1, 'html.parser')
            for i, p in enumerate(html.select('p')):
                t1="apicalloutputt.txt"
                f = open(t1,"a")
                print(p.text,file=f)
                lem.lemmatize(p.text, "v")
                words = p.text.split() 
                noise_free_words = [word for word in words if word not in noise_list] 
                noise_free_text = " ".join(noise_free_words)

                final_list.append(noise_free_text)
                f.close()
    new_final_list = [] 
    for num in final_list: 
        if num not in new_final_list: 
            new_final_list.append(num)

    

    

    f=open("haaaa.txt","a")
    print(new_final_list,file=f)
    f.close()

    bucketName = "test-bucket-saikiran"
    Key = t1
    outPutname = t1

    s3 = boto3.client('s3')
    s3.upload_file(Key,bucketName,outPutname)



"""
bucketName = "test-bucket-saikiran"
Key = t
outPutname = t

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)


"""
"""response.json()

directory_name = "aniket/bucket/python" #it's name of your folders
s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
"""

