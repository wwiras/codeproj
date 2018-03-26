from django.db import models

# Create your models here.
class Post(models.Model):
    
    name = models.CharField('Name',max_length=300,blank=False,null=False)
    content = models.TextField('Content',max_length=300,blank=True,null=True)
    date_exp = models.DateTimeField('Expiry Date',blank=False,null=False)

    def __str__(self):
    	return self.name


class PostLog(models.Model):
    ipaddr = models.CharField('Client IP Address',max_length=64,blank=False,null=False)
    date_visit = models.DateTimeField('Visit Date',blank=True,null=True)
    browser_agent = models.CharField('Browser Agent',max_length=400,blank=False,null=False)
    # post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='postlogs')
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.browser_agent
