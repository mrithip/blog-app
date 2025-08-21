from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Post, About
import logging
from .forms import ContactForm
# Create your views here.


# posts = [
#     {'id':1,'title':'post 1','content':'this is content of post 1'},
#     {'id':2,'title':'post 2','content':'this is content of post 2'},
#     {'id':3,'title':'post 3','content':'this is content of post 3'},
#     {'id':4,'title':'post 4','content':'this is content of post 4'}
# ]
def index(request):
    blog_title = "Latest Posts and Blogs"
    all_posts=Post.objects.all().order_by('-created_at') 
    paginator = Paginator(all_posts,5)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    return render(request,'blog/index.html',{'blog_title':blog_title,'page_obj':page_obj})

def detail(request,slug):
    # post = next((item for item in posts if item['id']==int(id)),None)
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post doesnot exists")

    return render(request,'blog/detail.html',{"post":post,'related_post':related_posts})

def oldurl(request):
    return redirect(reverse("blog:newurl"))

def newurl(request):
    return HttpResponse("new url")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            logger = logging.getLogger('TESTING')
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success = "your email has been sent !"
            return render(request,"blog/contact.html",{'form':form,'success':success})
        else:
            logger.debug("Form not validated !")
        
    return render(request,"blog/contact.html")

def about(request):
    about = About.objects.first().about
    return render(request,"blog/about.html",{"about":about})