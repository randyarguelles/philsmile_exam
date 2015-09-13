from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404,render_to_response
from .forms import PostForm,RegistrationForm
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import Context,RequestContext
# Create your views here.from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import logout

####Pang print ng error
import logging
logger = logging.getLogger(__name__)
###
def logout_page(request):
	logout(request)
	return redirect('/')
def main_page(request):
	return render(
		request,
		'blog/main_page.html'		)
def register_page(request):
	logger.error(request.method+'<,,,,')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			logger.error('pumasok dito')
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				email=form.cleaned_data['email']
			)
			return redirect('/register/success/')
		logger.error('asas dito')
	else:
		form = RegistrationForm()
		variables = RequestContext(request, {
		'form': form
		})

		return render_to_response(
			'registration/register.html',
			variables
			)
def employee_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	logger.error(posts)
	return render(request, 'blog/post_list.html', {'posts':posts})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})