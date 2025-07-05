from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    #class Meta:
    #    verbose_name_plural = 'blogpost'

    def __str__(self):
        if len(self.text) >= 50:
            text_ = f"{self.text[:50]}..."
            return text_

        return self.text
    
#class TopicBlog(models.Model):
#    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
#    title = models.CharField(max_length=200)

#    def __str__(self):
#        return self.title


    