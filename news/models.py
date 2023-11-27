from django.db import models
from users.models import User


class New(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    @classmethod
    def like_or_dislike(cls, new_id, user):
        new = New.objects.get(pk=new_id)

        is_like = False
        is_added = False

        for like in new.likes.all():
            if like == user:
                is_like = True
                break

        if not is_like:
            new.likes.add(user)
            is_added = True

        if is_like:
            new.likes.remove(user)

        return new, is_added

    def comments_count(self):
        return self.comments.all().count()

    def likes_count(self):
        return self.likes.count()


