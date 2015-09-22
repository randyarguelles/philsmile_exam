from django.shortcuts import render
from django.utils import timezone
from .models import Post,CertificateModel
from django.shortcuts import render, get_object_or_404,render_to_response
from .forms import PostForm,RegistrationForm,CertificatesForm
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
    #~ post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'posts':posts})
def certificate_list(request,pk):
    logger.error(request.method)
    if request.method == 'POST':
        form = CertificatesForm(request.POST, request.FILES)
        logger.error('pumasok')
        if form.is_valid():
            cert = form.save(commit=False)
            #~ logger.error('pumasok ulit')
            #~ newdoc=CertificateModel(docfile = request.FILES['docfile'])
            #~ newdoc.save()
            cert.save()
            #~ post = form.save(commit=False)
            post = get_object_or_404(Post, pk=pk)
            formp = PostForm(request.POST)
            #~ post = formp.save(commit=False)
            post.emp_certificate.add(cert)
            #~ post.published_date = timezone.now()
            post.save()
           
            
            
            #~ return HttpResponseRedirect(reverse('blog.views.certificate_list'))
            return redirect('blog.views.certificate_view', pk=cert.pk)
            #~ return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CertificatesForm()
        
    documents = CertificateModel.objects.all()
    logger.error('dito pumasok')
    
    c={'documents':documents, 'form': form}
    c.update(csrf(request))
    return render_to_response(
                'blog/certificate_list.html',
                c
                )
    #~ return render_to_response(
                #~ 'blog/certificate_list.html',
                #~ {'documents':documents, 'form': form},
                #~ context_instance = RequestContext(request)
                #~ )
def index(request):
    return render_to_response('myapp/index.html')

def certificate_view(request,pk):
    post = get_object_or_404(Post,pk=pk)
    #~ certificate=get_object_or_404(CertificateModel,pk=pk)
    certificate=CertificateModel.objects.get(certificate_name='55')
    cer_doc=CertificateModel.objects.all()
    #~ for m_o in cer_doc:
        #~ logger.error(m_o.docfile)
    documents=Post.objects.all()
    #~ logger.error(dir(documents))
    #~ logger.error(str(documents))
    #~ logger.error(str(certificate.docfile))
    logger.error(str(post.emp_certificate))
    logger.error(str(post.published_date))
    
    return render(request, 'blog/certificate_detail.html', {'post': post,'documents':documents})
def post_detail(request, pk):
    logger.error(request.method)
    post = get_object_or_404(Post, pk=pk)
    documents = Post.objects.all()
    #~ for po in post:
    logger.error(str(documents)+'<--')
    logger.error('oh yeah')
    return render(request, 'blog/post_detail.html', {'post': post,'documents':documents})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        logger.error(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            #~ newdoc=CertificateModel(docfile = request.FILES['file'])
            #~ newdoc.save()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
        logger.error('post new not post!!')
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

