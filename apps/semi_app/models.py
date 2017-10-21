from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        
        if len(postData["first_name"]) < 2:
            errors += ["First name must be at least 2 characters"]
        if len(postData["last_name"]) < 2:
            errors += ["Last name must be at least 2 characters"]
        if not postData["first_name"].isalpha() or not postData["last_name"].isalpha():
            errors += ["Names may not contain numbers of symbols"]
        if not EMAIL_REGEX.match(postData["email"]):
            errors += ["That is not a valid email"]
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255, default="email@email.com")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "<User Object - id:{}, name: {} {}>".format(self.id, self.first_name, self.last_name)

    objects = BlogManager()