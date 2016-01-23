from django.shortcuts import render
from models import BlogArticle
from django.contrib.auth import authenticate, login


def index(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
        usname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usname, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, "blogapp/index.html",
                          {'blogs': blogs, 'user': user})
    return render(request, "blogapp/index.html",
                  {'blogs': blogs, 'user': None})


def create_blog(request):
    blogs = BlogArticle.objects.all()
    new_blog = BlogArticle()
    new_blog.title = request.POST['title']
    new_blog.author = request.user
    new_blog.content = request.POST['blog_content']
    new_blog.save()
    return render(request, "blogapp/index.html", {'blogs': blogs,
                  'user': new_blog.author})
