from django.shortcuts import render, get_object_or_404
from .models import Blog


#Blog.objects.create(title ="eadasd", date='2002-02-02' , description='good for good')

def all_blogs(request):

    blogs = Blog.objects.order_by('-date')
    number = len(blogs)
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'number': number, })

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog })
