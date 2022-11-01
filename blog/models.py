from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author : 추후 작성 예정
    
    def __str__(self):
        return f'[{self.id}] {self.title}'
    # str > 개체로 찍을 때 뭐로 찍으면 좋을까 ~
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'