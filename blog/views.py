from django.shortcuts import render
from . models import Post, Category
from django.views.generic import ListView, DetailView

# Create your views here.

# def index(request):
#     posts = Post.objects.all().order_by('-id') #-붙이면 decending~(최근에 쓴글이 먼저)
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )

class PostList(ListView):
    model = Post
    ordering = '-pk'
    
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
            # template_name = 'blog/index.html'

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )

class PostDetail(DetailView):
    model = Post