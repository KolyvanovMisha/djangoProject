
from mongoengine import Document, fields


class Task(Document):
    title = fields.StringField()

    def __str__(self):
        return self.title
