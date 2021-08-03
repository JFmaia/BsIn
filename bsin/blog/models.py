from django import db
from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField()
    date = models.DateTimeField( auto_now_add= True)
    foto = models.ImageField()
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __init__(self: models, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'post'
    
