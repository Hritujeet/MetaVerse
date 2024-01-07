from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    img = models.ImageField(upload_to='main/images', default="")
    likes = models.IntegerField()
    views = models.IntegerField()

    def __str__(self) -> str:
        return f"Post by {self.user}"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    timeStamp = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return f"Comment by {self.user}"
