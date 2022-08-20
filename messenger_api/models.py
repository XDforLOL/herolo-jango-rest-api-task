from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=60, null=False)
    body = models.CharField(null=False, max_length=360)
    read = models.BooleanField(default=False, unique=False)
    creation_date = models.DateTimeField(auto_created=True)

    sent_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sent_by', null=True)

    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='recipient', null=True)

    def __str__(self):
        return f'<Message {"ID", self.id, self.subject}>'
