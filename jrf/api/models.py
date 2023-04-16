from django.db import models
from django.urls import reverse
from uuid import uuid4
from pytils.translit import slugify
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", db_index=True)
    info = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    content = models.TextField(blank=True, null=True, verbose_name="Контент")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    modification_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    ispublished = models.BooleanField(default=True, verbose_name="Опубликовано")
    awatar = models.ImageField(upload_to="awatars/%Y/%m/%d", verbose_name="Картинка")
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name="Категория",
                                 db_index=True, related_name="get_posts")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, verbose_name="Автор")

    # Выводит не объект №, а наименование title
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"articleID": self.pk})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            unique_slug = slugify(self.title)
            while Articles.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
            self.slug = unique_slug

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"
        # ordering = ['-modification_date']


class Categories(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    modification_date = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("getCategoryArticles", kwargs={"categoryID": self.pk})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            unique_slug = slugify(self.name)
            while Categories.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
            self.slug = unique_slug

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
        # ordering = ['-modification_date']