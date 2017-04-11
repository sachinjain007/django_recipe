from django.db import models


class addRecipe(models.Model):
    username = models.CharField(max_length=220)
    recipe_name = models.CharField(max_length=220)
    recipe_add = models.TextField(max_length=220)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)


    def __str__(self):
        return self.recipe_name
    def __unicode__(self):
        return self.recipe_name


class recipeComment(models.Model):
    username = models.CharField(max_length=220)
    recipe_pk = models.CharField(max_length=220)
    recipe_comments = models.TextField(max_length=220)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)


    def __str__(self):
        return self.recipe_pk
    def __unicode__(self):
        return self.recipe_pk