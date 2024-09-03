from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Notes page
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    #ithula vara values ah Notes Object nu save pannum..

    def __str__(self):   #__str__ method use panrapp namba kuduthan title name la save pannum -> ithum obj than
        return self.title

    class Meta:
        verbose_name = 'notes'
        verbose_name_plural = 'notes'


#Homework page
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)  #true of false

    def __str__(self):
        return self.title


#ToDo page
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title