from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'id': self.id})


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='media', default='default.png')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, blank=True, null=True, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        output_size = (800, 600)
        img.thumbnail(output_size)
        img.save(self.image.path)


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True,
                             on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['created_on']
