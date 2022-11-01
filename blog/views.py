from django.shortcuts import render
from . models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id') #-붙이면 decending~(최근에 쓴글이 먼저)
    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
        }
    )
