from django.conf.urls import patterns, include, url
from django.contrib import admin
from matansTwitter.views import createUser
from matansTwitter.views import tweet
from matansTwitter.views import follow
from matansTwitter.views import getTweets


#user object regexs  
nameRegex="name=(?P<name>[A-Za-z]+)"
userIdRegex="user_id=(?P<user_id>[A-Za-z0-9]+)"
tweetIdRegex="tweet_id=(?P<tweet_id>[A-Za-z0-9]+)"
tweetTextRegex="tweet_text=(?P<tweet_text>.*)"
followerRegex="follower=(?P<follower_id>[A-Za-z0-9]+)"
followedRegex="followed=(?P<followed_id>[A-Za-z0-9]+)"

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
	url(r'^create-user/'+userIdRegex+','+nameRegex+'$', createUser),
	url(r'^tweet/'+userIdRegex+','+tweetIdRegex+','+tweetTextRegex+'$', tweet),
	url(r'^follow/'+followerRegex+','+followedRegex+'$',follow),
	url(r'^getTweets/'+userIdRegex+'$',getTweets))