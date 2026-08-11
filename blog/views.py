from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, "blog/home.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, "blog/post_detail.html", {"post": post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    
    else:
        form = PostForm()

    return render(request, "blog/post_from.html", {"form": form})