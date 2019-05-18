from django.shortcuts import render
from django.http import HttpResponse
import os
import re
import tweepy
import fnmatch
from tweepy import OAuthHandler
from textblob import TextBlob
from first_app import forms

def index(request):
    form=forms.FormName

    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():

            api = Twitter()
            tweets = api.get_tweets(query = form.cleaned_data['Tweet_Search'], count =50)
            counter=[0,0,0]
            percentage=[0,0,0]
            for tweet in tweets:
                analysis = TextBlob(api.clean(tweet[0]))
                if analysis.sentiment.polarity > 0:
                    counter[0]=counter[0]+1
                elif analysis.sentiment.polarity == 0:
                    counter[1]=counter[1]+1
                else:
                    counter[2]=counter[2]+1
            percentage[0]=(counter[0]/sum(counter))*100
            percentage[1]=(counter[1]/sum(counter))*100
            percentage[2]=(counter[2]/sum(counter))*100
            mydict={'tweets':tweets,'counter':percentage,'form':form}
            return render(request,'index.html',context=mydict)
    return render(request,'index.html',{'form':form})

class Twitter(object):
    def __init__(self):
        consumer_key = '####################'
        consumer_secret = '########################'
        access_token = '############################'
        access_token_secret = '#########################'

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")


    def clean(self,tweet):

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

    def sentiments(self, tweet):
        analysis = TextBlob(self.clean(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        tweets = []
        try:
            fetched_tweets = self.api.search(q = query, count = count)
            for tweet in fetched_tweets:
                flag=0
                parsed_tweet =""
                parsed_tweet= tweet.text
                if tweet.retweet_count > 0:
                    for i in range(0,len(tweets)):
                        if parsed_tweet == tweets[i][0]:
                            flag=1
                    if(flag==0):
                        tweets.append([parsed_tweet,self.sentiments(tweet.text)])
                else:
                    tweets.append([parsed_tweet,self.sentiments(tweet.text)])

            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))









def about(request):
    video_name = ""

    video_url = "media/007.mp4"
    return render(request, "about.html", {"url":video_url})


from first_app.forms import MMForm

def contact(request):
    form=MMForm()
    if request.method=="POST":
        form=MMForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR ")

    return render(request,"contact.html",{'form':form})
