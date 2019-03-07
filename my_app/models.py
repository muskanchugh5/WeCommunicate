from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    title=models.CharField(max_length=256)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse('my_app:post_list')


    def publish(self):
        print("hey")
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey('Post',related_name="Comment",on_delete=models.CASCADE)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.author)


    def get_absolute_url(self):
        return reverse('my_app:post_detail',kwargs={'pk':self.post.pk})


class User_info(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    profilepic=models.ImageField(blank=True,upload_to='profilePic')
   
    def __str__(self):
        return self.username.username
