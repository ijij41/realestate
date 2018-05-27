from __future__ import unicode_literals

from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(db_column='title',max_length=200)  # Field name made lowercase.
    news_pub_date = models.DateTimeField(db_column='news_pub_date')
    content = models.TextField(db_column='content')
    url = models.URLField(db_column='url')



