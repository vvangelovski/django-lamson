from django.db import models

class ReceivedMessage(models.Model):
    from_address = models.EmailField(max_length = 100)
    to_address = models.EmailField(max_length = 100)
    subject = models.CharField(max_length = 255)
    content = models.TextField()
