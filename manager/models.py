from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(max_length=50, verbose_name='название')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    authors = models.ManyToManyField(User, related_name="books")

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)