from django.db import models
from users.models import User
from news.models import New


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=256)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    new = models.ForeignKey(to=New, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-created',)


