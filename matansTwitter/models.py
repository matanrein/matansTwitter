from django.db import models

# Create your models here.

#represents a user
class User(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)

#represents a tweet
class Tweet(models.Model):
	tweet_id = models.CharField(max_length=30)
	user_id = models.CharField(max_length=30)
	date = models.DateField(auto_now_add=True)
	tweet_text = models.CharField(max_length=140)
	class Meta:
		ordering = ['date']
	
#represents a followed user
class Follow(models.Model):
	follower_id = models.CharField(max_length=30)
	followed_id = models.CharField(max_length=30)