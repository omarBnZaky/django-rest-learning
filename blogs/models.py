from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
import os
from django.utils.text import slugify

User = get_user_model()
# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'blogs'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Blog(models.Model):
    """docstring for Blog."""

    title = models.CharField(max_length=50,null=False,blank=False)
    message = models.TextField()
    image = models.ImageField(upload_to=path_and_rename,null=True)
    user = models.ForeignKey(User,related_name='blogs',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,verbose_name='date published')
    date_updated = models.DateTimeField(auto_now=True,verbose_name='date updated')
    slug = models.SlugField(blank=True,unique=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
