from django.utils import timezone
from .models import Post, Project
from django.shortcuts import render, render_to_response
from .forms import PostForm, RegistrationForm, ProjectForm
from django.shortcuts import redirect
from django.template import RequestContext
# Create your views here.from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
import datetime
# ###Pang print ng error
# import logging
# logger = logging.getLogger(__name__)


def logger(message):
    print (message)
##

# #For Testing only 1##
global selected_date
selected_date = datetime.date.today()
######


def logout_page(request):
    logout(request)
    return redirect('/')


def main_page(request):
    return render(
        request,
        'blog/main_page.html')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            logger('pumasok dito')
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return redirect('/register/success/')
        else:
            return HttpResponse("<p>error here</p>")
        logger('asas dito')
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


def project_list(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        # logger(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
    form = ProjectForm()
    projects = Project.objects.all()
    return render(request, 'blog/post_projects.html', {
        'form': form,
        'projects': projects
    })


def post_detail(request, pk):
    logger(request.method)
    post = Post.objects.all()
    # ~ for po in post:
    for i in post:
        logger(i)
    return render(request, 'blog/post_detail.html', {'posts': post})


def post_new(request):
    # #For Testing only 1##
    global selected_date
    # request.session['selected_date'] = selected_date
    if 'selected_date' not in request.session:
        request.session['selected_date'] = selected_date
    # print (request.session['selected_date'],"My session date")
    # print request.session
    #####
    logger(timezone.now())

    logger('awaa')
    logger(request.session['selected_date'])
    if request.method == 'POST' and 'btnform1' in request.POST:
        pass
    if request.method == "POST":
        form = PostForm(request.POST)
        logger(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.employee = request.user

            # ~ selected_date=datetime.datetime.strptime
            # (request.POST['date_hidden'],'%m/%d/%Y').date()
            post.log_date = request.session['selected_date']
            post.save()
            return redirect('post_new')

    if 'datepick' in request.GET:
        logger(type(request.GET['datepick']))
        request.session['selected_date'] = datetime.datetime.strptime(
            request.GET['datepick'], '%m/%d/%Y').date()
        logger(request.session['selected_date'])
        logger('xxx')
    form = PostForm()
    post = Post.objects.filter(
        employee=request.user,
        log_date__year=request.session['selected_date'].year,
        log_date__month=request.session['selected_date'].month,
        log_date__day=request.session['selected_date'].day,
    )
    monthly_posts = Post.objects.filter(
        employee=request.user,
        log_date__year=request.session['selected_date'].year,
        log_date__month=request.session['selected_date'].month,
    )
    month_hours = 0
    for mp in monthly_posts:
        # print mp,"MP!!"
        month_hours += mp.duration_time
    hours = 0
    for d in post:
        hours += d.duration_time
        print d.if_late(),"waakokos"
        logger('%s laman ng post' % d.duration_time)
    logger(hours)
    return render(request, 'blog/post_edit.html', {
        'form': form,
        'posts': post,
        'hours': hours,
        'monthly_hours': month_hours,
        'selected_date': request.session['selected_date']})


# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
