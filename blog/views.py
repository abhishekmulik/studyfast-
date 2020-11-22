from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

from blog.models import Post,Comment,SubjectList,Category
from blog.forms import PostForm,CommentForm,SubjectListForm,CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import DeleteView,UpdateView,CreateView
                                
from django.views.generic import ListView,TemplateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
class AboutView(TemplateView):
    template_name='about.html'

class contribute(TemplateView):
    template_name='contribute.html'

class SubjectListView(ListView):
    model=SubjectList

class CreateSubjectView(LoginRequiredMixin,CreateView):
    login_url='accounts/login'
    redirect_field_name='add_subject'      # not working :(
    form_class=SubjectListForm
    model=SubjectList

class CreateCategoryView(LoginRequiredMixin,CreateView):
    login_url='accounts/login'
    redirect_field_name='add_subject'      # not working :(
    form_class=CategoryForm
    model=Category

def categorylist(request,pk):
    category=Category.objects.filter(subject_id=pk)
    return render(request,"category_list.html",{'category':category})

# def postlist(request,pk):
#     post=Post.objects.filter(category_id=pk)
#     return render(request,"cate_posts.html",{'post':post})

def postview(request,pk):
    post=Post.objects.filter(category_id=pk)
    return render(request,'cate_posts.html',{'post':post})


class CategoryListView(ListView):
    model=Category

class PostListView(ListView):
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model=Post

# class CategorizedPostView(DetailView):
#     template_name='blog/cate_posts.html'
#     queryset=Post.objects.filter(pk=pk)

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForm
    model=Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForm
    model=Post

class PostDeleteView(DeleteView):
    model=Post
    success_url=reverse_lazy('subjectList')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

# class AddCategoryView(CreateView):
#     model=Category
#     template_name='add_category.html'
#     fields='__all__'

# def CategoryView(request,cats): #pk/category/cats/
#     #the post model is filtered and the category field is extracted if the passed cats is equal to category in models
#     # eg. if /catgory/groupC the from models groupC category is stored in category_posts
#     category_posts=Post.objects.filter(category=cats) 
#     return render(request,'categories.html',{'cats':cats,'category_posts':category_posts})

# def CategoryListView(request,pk):
#     # category_posts=Category.objects.filter(id=pk)
#     category_posts=Category.objects.filter(id=pk)
#     return render(request,'categories.html',{'pk':pk,'category_posts':category_posts})
    
#########################
#################
#########

@login_required
def post_published(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
  

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approved(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk) 