from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
