from django.shortcuts import render, redirect 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from index.models import Post1


def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})




@login_required
def profile(request):
    posts= Post1.objects.filter(author=request.user).all()
    if posts.count()==0:
        post = Post1.objects.create(author= request.user, title= 'Hello I just Created an Account',content='Hello i am new Here')
        post.save()
    return redirect('profile_view')



@login_required
def update(request):
    if request.method=='POST':

        u_form=UserUpdateForm(request.POST, instance=request.user)  
        p_form=ProfileUpdateForm(request.POST,  request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)  
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }  

    return render(request,'update.html',context)


class UserPostListView(LoginRequiredMixin, ListView):
    
    model=Post1
    template_name='profile.html'
    context_object_name='posts'
    
    paginate_by=5

    def get_queryset(self):
        

        return Post1.objects.filter(author=self.request.user).order_by('-date_posted')
    
