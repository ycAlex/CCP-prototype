from django.shortcuts import render, redirect
from .models import BlogPost, Comments


# from forms import CommentForm


# Create your views here.
def index(request):
    if request.method == "GET":
        blog = BlogPost.objects.get(pk=1)
        comments = Comments.objects.filter(blog=blog)
        return render(request, "content_1.html", context={'blog': blog,
                                                          'comments': comments})


def blog_add(request, blog=1):
    if request.method == "POST":
        username = request.POST.get("username", "anonymous")
        email = request.POST.get("email", "null")
        content = request.POST.get("content", None)

        if content:
            comment = Comments(username=username, email=email, content=content,
                               blog=BlogPost.objects.get(id=blog))
            comment.save()
        return redirect("/blog/")


def comment_add(request, comment):
    if request.method == "GET":
        return render(request, "comment_comment_add.html", context={"title": "Comment",
                                                                    "comment": comment})
    if request.method == "POST":
        username = request.POST.get("username", "anonymous")
        email = request.POST.get("email", "null")
        content = request.POST.get("content", None)
        if content:
            p_comment = Comments.objects.get(id=comment)
            Comments(username=username, email=email, content=content,
                     blog=p_comment.blog, parent_comment=p_comment.pk,
                     level=p_comment.level + 1).save()
            return redirect("index")
