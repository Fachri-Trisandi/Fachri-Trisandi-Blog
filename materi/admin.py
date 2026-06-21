from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order", "updated_at")
    list_filter = ("course",)
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "title")
