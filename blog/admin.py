from django.contrib import admin
from blog.models import BlogsPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_dispaly = ['title', 'body', 'timestamp']


admin.site.register(BlogsPost, BlogPostAdmin)