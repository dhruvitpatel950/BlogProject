from django.contrib import admin
from blogs.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ('title','content')

    
