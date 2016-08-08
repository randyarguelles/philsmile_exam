from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404,render_to_response
from .forms import PostForm,RegistrationForm
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import Context,RequestContext
# Create your views here.from django.shortcuts import render_to_response

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.template.context_processors import csrf

import datetime
####Pang print ng error
import logging
logger = logging.getLogger(__name__)
###
global selected_date
selected_date=datetime.date.today()
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
		else:
			return HttpResponse("<p>error here</p>")
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

def index(request):
    return render_to_response('myapp/index.html')


def post_detail(request, pk):
	logger.error(request.method)
	post = Post.objects.all()
	documents = Post.objects.all()
	#~ for po in post:
	for i in post:
		logger.error(i)
	logger.error(str(documents)+'<--')
	logger.error('oh yeah')
	return render(request, 'blog/post_detail.html', {'posts': post})

def post_new(request):
	global selected_date
	logger.error(timezone.now())
	
	logger.error('awaa')
	logger.error(selected_date)
	if request.method=='POST' and 'btnform1' in request.POST:
		logger.error(type(request.POST['datepick']))
		selected_date=datetime.datetime.strptime(request.POST['datepick'],'%m/%d/%Y').date()
		logger.error(selected_date)
		logger.error('xxx')
	elif request.method == "POST":
		form = PostForm(request.POST)
		logger.error(request.POST)
		if form.is_valid():
		    post = form.save(commit=False)
		    post.employee = request.user
		    
		    #~ selected_date=datetime.datetime.strptime(request.POST['date_hidden'],'%m/%d/%Y').date()
		    post.log_date =selected_date
		    logger.error(selected_date)
		    logger.error('waaa')
		  
		    post.save()
		    return redirect('blog.views.post_new')
	#~ else:
	form = PostForm()
	post = Post.objects.filter(employee=request.user,
						log_date__year=selected_date.year,
						log_date__month=selected_date.month,
						log_date__day=selected_date.day,
						)
	hours=0
	for d in post:
		hours+=d.duration_time
		logger.error('%s laman ng post'%d.duration_time)
	logger.error(hours)
	return render(request, 'blog/post_edit.html', {
		'form': form,
		'posts':post,
		'hours':hours,
		'selected_date':selected_date})

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

