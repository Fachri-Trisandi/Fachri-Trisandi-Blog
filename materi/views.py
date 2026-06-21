from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Post


def get_blog_widgets():
    return {
        "total_posts": Post.objects.count(),
        "recent_posts": Post.objects.order_by("-updated_at")[:4],
    }


def index(request):
    query = request.GET.get("q", "").strip()
    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query)
            | Q(excerpt__icontains=query)
            | Q(content__icontains=query)
        )

    context = {
        "posts": posts,
        "query": query,
        **get_blog_widgets(),
    }
    return render(request, "materi/index.html", context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    related_posts = Post.objects.exclude(pk=post.pk)[:3]
    return render(
        request,
        "materi/detail.html",
        {"post": post, "related_posts": related_posts, **get_blog_widgets()},
    )
