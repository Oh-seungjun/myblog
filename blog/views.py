from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, "blog/home.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, "blog/post_detail.html", {"post": post})