from django.db import models


# Create your models here.

class Todo(models.Model):

    choice = [
       ("important", "important"),
       ("less important", "less import"),
       ("not important", "not important"),
    ]

    title = models.CharField(max_length=150)
    # done = models.BooleanField(default=False)
    content = models.TextField()
    dateadded = models.DateField(auto_now_add=True)
    priority = models.CharField(choices = choice, max_length=50  )
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'
    
    

    def __str__(self):
        return self.title + " " + "|" + " " +  str(self.priority)