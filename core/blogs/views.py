from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm,UserRegistrationForm ,LoginForm, CommentForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator


def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(
            Q(published = True) | Q(author = request.user)
        ).distinct()
    else:    
        posts = Post.objects.filter(published = True)
    
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains = query) | Q(content__icontains = query)
        )

    paginator = Paginator(posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogs/post_list.html', {'page_obj': page_obj, 'query': query})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.order_by('created_at')
    if request.method ==  'POST':
        if not request.user.is_authenticated:
            messages.error('you have to login first to comment')
            return redirect('login')
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()

    return render(request, 'blogs/post_detail.html', 
                  {'post':post, 'comments': comments, 'form': form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    
    return render(request, 'blogs/post_form.html', {'form': form , 'action':'Create'})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_list')
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
    return render(request, 'blogs/post_form.html', {'form':form, 'action': 'Update'})  

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_list')
    if request.method == 'POST':                  
        post.delete()
        return redirect('post_list')
    
    return render(request, 'blogs/post_confirm_delete.html', {'post': post})                   

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
                )
        if user :
            login(request,user)
            return redirect('post_list')
        
        else:
            messages.error(request, 'invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'blogs/login.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            user.save()
            messages.success(request, "Account created! Login below")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blogs/registration.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/blog/')