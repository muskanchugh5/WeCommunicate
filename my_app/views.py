from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from my_app.models import Post,Comment,User_info
from my_app.forms import PostForm,CommentForm,UserForm,UserProfileForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
class AboutView(TemplateView):
    template_name='About.html'
 
class PostListView(ListView):
    model=Post
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model=Post
   

# class CreatePostView(LoginRequiredMixin,CreateView):
    
#     login_url='/login/'
#     redirect_field_name='my_app/post_detail.html'
#     form_class=PostForm
#     model=Post
#     context_object_name='post'

@login_required
def CreatePost(request):
    if(request.method=="POST"):
        form=PostForm(data=request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('my_app:post_detail',pk=post.pk)
        else:
            return HttpResponse("invalid information")
    else:
        form=PostForm()
    return render(request,'post_form.html',{'form':form})
    

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='my_app/post_detail.html'
    form_class=PostForm
    model=Post

class DeletePostView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy("my_app:post_list")


class DraftPostView(LoginRequiredMixin,ListView):
    model=Post
    login_url='/login/'
    redirect_field_name='my_app/post_detail.html'
    template_name="draft_post.html"
  

    def get_queryset(self):
      return Post.objects.filter(author=self.request.user)

    # def for_user(self, user):
    #     if user.is_authenticated():
    #         return self.get_query_set().filter(Post__author=user)
    #     else:
    #         return self.get_query_set().none()

   

@login_required
def publish_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    print(post.title)
    post.publish()
    return redirect('my_app:post_list')


@login_required
def add_comment(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.author=request.user
            comment.save()
            return redirect('my_app:post_detail', pk=post.pk)
        else :
            HttpResponse("Invalid")
    else :
        form=CommentForm()
    return render(request,'comment_form.html',{'form':form,'post':post})

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('my_app:post_detail',pk=post_pk)

class UpdateCommentView(UpdateView,LoginRequiredMixin):
    login_url='/login/'
    redirect_field_name='my_app/post_detail.html'
    form_class=CommentForm
    model=Comment

class CommentListView(DetailView):
    model=Post
    template_name="comment_list.html"

def reg(request):
    registered=False
    if request.method=="POST":
        Userform=UserForm(data=request.POST)
        Profileform=UserProfileForm(data=request.POST)

        if Userform.is_valid() and Profileform.is_valid():
            user=Userform.save()
            user.set_password(user.password)
            user.save()

            profile=Profileform.save(commit=False)
            profile.username=user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            
            profile.save()
            registered=True
    
    else:
        Userform=UserForm()
        Profileform=UserProfileForm()
    return render(request,'form_page.html',{'Userform':Userform,'Profileform':Profileform,'registered':registered})


def profile(request):
    return redirect('my_app:post_list')

class ProfileView(ListView):
    model=Post
    template_name="profile_list.html"
    
   