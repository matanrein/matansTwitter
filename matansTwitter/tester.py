import requests
import json

def create_user(user_id,name):
	print("creating user with id="+user_id+" and name="+name)
	url=u'http://127.0.0.1:8000/create-user/user_id=%s,name=%s' % (user_id,name)
	r=requests.get(url)
	print(r.json())
	
def follow(follower_id,followed_id):
	print("user "+follower_id+" is now following user "+followed_id)
	url=u'http://127.0.0.1:8000/follow/follower=%s,followed=%s' % (follower_id,followed_id)
	r=requests.get(url)
	print(str(r.content))
	
def twit(user_id,twit_id,twit_text):
	print("user "+user_id+" is twitting:"+twit_text)
	url=u'http://127.0.0.1:8000/tweet/user_id=%s,tweet_id=%s,tweet_text=%s' % (user_id,twit_id,twit_text)
	r=requests.get(url)
	print(r.json())

def getTwits(user_id):
	print("printing twits for user: "+user_id)
	url=u'http://127.0.0.1:8000/getTweets/user_id=%s' % (user_id)
	r=requests.get(url)
	print(r.json())


#creating users
create_user("1","a")
create_user("2","b")
create_user("3","c")

#creating follows
follow("1","2")
follow("2","3")

#twitting
twit("2","11","user b twit number 1")
twit("2","12","user b twit number 2")
twit("2","13","user b twit number 3")
twit("2","14","user b twit number 4")
twit("2","15","user b twit number 5")
twit("2","16","user b twit number 6")
twit("2","17","user b twit number 7")
twit("2","18","user b twit number 8")

twit("3","19","user c twit number 1")
twit("3","20","user c twit number 2")
twit("3","21","user c twit number 3")
twit("3","22","user c twit number 4")
twit("3","23","user c twit number 5")
twit("3","24","user c twit number 6")
twit("3","25","user c twit number 7")
twit("3","26","user c twit number 8")
twit("3","27","user c twit number 9")

twit("1","28","user a twit number 1")
twit("1","29","user a twit number 2")
twit("1","30","user a twit number 3")
twit("1","31","user a twit number 4")
twit("1","32","user a twit number 5")
twit("1","33","user a twit number 6")
twit("1","34","user a twit number 7")
twit("1","35","user a twit number 8")


#get twits
print("getting twits for user 1")
getTwits("1")




