from django.conf.urls import url
from first_app import views
from first_app import CheckNL
app_name='first_app'

urlpatterns=[
url(r'^CheckMyTweet/$',CheckNL.CheckMyTweet,name='CheckMyTweet'),
#url(r'^feedback/$',views.feedback,name="feedback")
url(r'^about/$',views.about,name='about'),
url(r'^contact/$',views.contact,name='contact')
]
