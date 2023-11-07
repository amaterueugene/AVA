from django.db import models


class Account(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    url = models.URLField(max_length=250, blank=True, verbose_name="URL")
    login = models.CharField(max_length=50, blank=True, verbose_name="Login")
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=50, verbose_name="Password")
    # привязать к юзеру
