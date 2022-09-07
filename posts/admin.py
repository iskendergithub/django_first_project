from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp', 'publish']


admin.site.register(Post, PostAdmin)
