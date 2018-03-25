from django.db import models

# Create your models here.
class Post(models.Model):
    
    name = models.CharField('Name',max_length=300,blank=False,null=False)
    content = models.TextField('Content',max_length=300,blank=True,null=True)
    date_exp = models.DateTimeField('Expiry Date',blank=True,null=True)

    def __str__(self):
    	return self.name