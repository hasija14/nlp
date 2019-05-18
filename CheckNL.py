import pandas as pd
import numpy as np
import re
from textblob import TextBlob
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import  PorterStemmer
from django.shortcuts import render
from first_app import forms
def CheckMyTweet(request):
    formm=forms.MyForm
    if request.method=='POST':
        formm=forms.MyForm(request.POST)

        if formm.is_valid():
            X=formm.cleaned_data['My_Tweet']
            review=re.sub('[^a-zA-Z]',' ',X)
            review=review.lower()
            review=review.split()
            ps=PorterStemmer()
            review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
            review=' '.join(review)
            analysis=TextBlob(review)
            send=""
            polarity=analysis.sentiment.polarity
            if polarity>0:
                send="positive"
            elif polarity==0:
                send="neutral"
            else:
                send="negative"
            return render(request,'CheckTweet.html',{'polarity':send})
    return render(request,'CheckTweet.html',{'formm':formm})
