from django.db import models

class EmailAlert(models.Model):
    Name= models.CharField(max_length=255)
    Email=models.EmailField()	
    updated=models.DateField(auto_now=True)	
    created=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Email
        
class Post(models.Model):
    Title= models.CharField(max_length=255)
    Body=models.TextField()	
    Cover=models.ImageField(upload_to='posts_images',blank=True)	
    Updated=models.DateTimeField(auto_now=True)	
    Created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title