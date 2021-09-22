from django.db import models

# Create your models here.

#
#
# PRIORITY=[("H","HIGH"),("M","MEDIUM")]
#
# class Question(models.Model):
#     title = models.CharField(max_length=200)
#     question = models.CharField(max_length=200)
#     priority = models.CharField(max_length=10,choices=PRIORITY)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "The Question"
#         verbose_name_plural= "People Questions"