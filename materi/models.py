from django.db import models
from django.urls import reverse


class Post(models.Model):
    ILLUSTRATED_SLUGS = {
        "pengantar-arsitektur-perangkat-lunak",
        "pola-arsitektur-fundamental-layered-dan-monolith",
        "pola-arsitektur-kinerja-tinggi",
        "visualisasi-arsitektur-uml-dan-c4-model",
        "architectural-drivers-mengarahkan-desain-sistem",
        "architectural-quality-attributes",
        "modern-data-blueprint",
    }

    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    course = models.CharField(max_length=120, default="Arsitektur Perangkat Lunak")
    excerpt = models.TextField()
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("materi:detail", kwargs={"slug": self.slug})

    @property
    def image_path(self):
        if self.slug in self.ILLUSTRATED_SLUGS:
            return f"materi/images/{self.slug}.svg"
        return "materi/images/default.svg"
