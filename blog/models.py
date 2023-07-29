from django.db import models
from django.contrib.auth.models import User

class FixModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

class Category(FixModel):
    name = models.CharField(max_length=75, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Post(FixModel):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='post/covers/')
    category = models.ManyToManyField(Category)
    
class Comment(FixModel):
    message = models.TextField()
    post = models.ManyToOneRel(Post)

class Like(FixModel):
    post = models.ManyToOneRel(Post)