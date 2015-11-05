from django.db import models
from django.contrib.auth.models import User
from vote.managers import VotableManager
from django.utils import timezone


class Recipe(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    recipe_type = models.CharField(max_length=100, blank=True, null=True)
    #text = models.CharField(max_length=200)
    preparation_time = models.CharField(max_length=100)
    ingredients = models.TextField(null=True, blank=True)
    cooking_directions = models.TextField(null=True, blank=True)
    upvotes = models.ManyToManyField(User, related_name="upvotes", blank=True)
    downvotes = models.ManyToManyField(User, related_name="downvotes", blank=True) 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class ArticleReview(models.Model):
    votes = VotableManager()


class Picture(models.Model):
    image = models.ImageField(upload_to="images")
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey('main.Recipe', null=True)


# #class Comment(models.Model):
#     post = 
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     approved_comment = models.BooleanField(default=False)

#     def approve(self):
#         self.approved_comment = True
#         self.save

#     def __str__(self):
#         return self.text

# class Cookie(models.Model):
#     title = models.ForeignKey("main.Recipe")

#     def __unicode__(self):
#         return "%s" % self.title 


# class Cake(models.Model):
#     title = models.ForeignKey("main.recipe", null=True, blank=True)

#     def __str__(self):
#         return self.title


# class Dessert_Bar(models.Model):
#     title = models.ForeignKey("main.recipe", null=True, blank=True)

#     def __str__(self):
#         return self.title




 

