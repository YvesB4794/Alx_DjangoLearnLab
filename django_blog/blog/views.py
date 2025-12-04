# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileUpdateForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# ✅ USER REGISTRATION
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


# ✅ USER PROFILE
@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "registration/profile.html", {"form": form})
