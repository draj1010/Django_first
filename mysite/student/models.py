from django.db import models

# Create your models here.

class Student(models.Model):
	roll_no = models.TextField()
	name = models.TextField(max_length = 40)
	stud_class = models.TextField()
	department = models.TextField()

class Teacher(models.Model):
	card_no = models.TextField()
	name = models.TextField()
	age = models.TextField()

class Products(models.Model):
	p_name = models.TextField()
	sku = models.TextField()
	price = models.TextField()
	desc = models.TextField()
	slug = models.TextField()