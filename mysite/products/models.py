from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    parent = models.ForeignKey('self',blank=True, null=True, related_name='child',on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('cat_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.cat_name


Rating = [
    ('b', 'Bad'),
    ('a', 'Average'),
    ('e', 'Excellent')
]

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    catagory = models.ForeignKey(Category, on_delete=models.DO_NOTHING,null=True)
    rating = models.CharField(max_length = 1, choices = Rating)
    mfg_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
    def show_desc(self):
        return self.description[:50]

            

