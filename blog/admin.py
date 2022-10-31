from django.contrib import admin
from .models import Post
# Register your models here.
# . < 현재 경로 기준으로
admin.site.register(Post)