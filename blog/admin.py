from django.contrib import admin
from .models import Post, Category
# Register your models here.
# . < 현재 경로 기준으로
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    
admin.site.register(Category, CategoryAdmin)