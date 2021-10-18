from django.db import models
from mongoengine import Document, fields


class Task(Document):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
