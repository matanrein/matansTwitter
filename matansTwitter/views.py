from django.shortcuts import render
from django.http import HttpResponse
from matansTwitter.models import User
from matansTwitter.models import Tweet
from matansTwitter.models import Follow
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.

#create a new user
def createUser(request,user_id,name):
	user_id_json={}
	user_id_json['user_id'] = -1 #default return value for failed requests
	if User.objects.filter(user_id=user_id).exists(): #if a user with the given id already exist return without creating
		return JsonResponse(user_id_json)
	if User.objects.filter(name=name).exists(): #if a user with the given name already exist return without creating
		return JsonResponse(user_id_json)
	user = User(user_id=user_id,name=name) #new user object to represent the new user
	user.save() #save new user to database
	user_id_json={}
	user_id_json['user_id'] = user_id
	return JsonResponse(user_id_json)

#create a new tweet
def tweet(request,user_id,tweet_id,tweet_text):
	twit_json={}
	if not(User.objects.filter(user_id=user_id).exists()): #if a user with the given id doesn't exist return without creating
		return JsonResponse(twit_json)
	if Tweet.objects.filter(tweet_id=tweet_id).exists(): #if a twit with the given id already exist return without creating
		return JsonResponse(twit_json)
	new_tweet = Tweet(tweet_id=tweet_id,user_id=user_id,tweet_text=tweet_text) #new twit object
	new_tweet.save() #save twit to database
	twit_json['tweet_id']=tweet_id
	twit_json['user_id']=user_id
	twit_json['tweet_text']=tweet_text
	twit_json['date']=str(new_tweet.date)
	return HttpResponse(json.dumps(twit_json), content_type="application/json")
	
#follow user's tweets		
def follow(request,follower_id,followed_id):
	if Follow.objects.filter(followed_id=followed_id,follower_id=follower_id).exists(): #if the follow alredy exist return without creating
		return HttpResponse("follow already exists")
	new_follow=Follow(followed_id=followed_id,follower_id=follower_id)
	new_follow.save()
	return HttpResponse("follower: "+new_follow.follower_id+",followed:"+new_follow.followed_id)
	
#get twits by the given user, and by the users followed by him
def getTweets(request,user_id):
	twitsString=''
	userTweets = Tweet.objects.filter(user_id=user_id)
	follow_list=Follow.objects.filter(follower_id=user_id)
	for follow in follow_list:
		currentTwits=Tweet.objects.filter(user_id=follow.followed_id)
		userTweets = userTweets | currentTwits
	twits_json=[]
	for twit in userTweets:
		tmp={}
		tmp['twit_id']=twit.tweet_id
		tmp['user_id']=twit.user_id
		tmp['tweet_text']=twit.tweet_text
		tmp['date']=str(twit.date)
		twits_json.append(tmp)
	return HttpResponse(json.dumps(twits_json[0:9]), content_type="application/json")