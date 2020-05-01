from django.db import models

# Create your models here.

class Userx(models.Model):
	name = models.TextField()
	email = models.TextField()
	password = models.TextField()

	def __str__(self):
		return self.name

class todo(models.Model):
	task_title = models.TextField()
	task = models.TextField()
	author = models.ForeignKey(Userx, default = None, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.task_title


