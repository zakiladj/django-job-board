from django.contrib.auth.forms import AuthenticationForm
from django.db.models.fields.related import ForeignKey
from django.shortcuts import redirect, render
from .forms import SignupForm,UserForm,ProfileForm
from django.contrib.auth import authenticate, login
from .models import profile
from django.urls import reverse

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password  =form.cleaned_data['password1']
            print(password)
            user = authenticate(username = username,password = password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form =SignupForm()
    return render(request,'registration/signup.html',{'form':form})

def profile_view(request):
    profile_user = profile.objects.get(user=request.user)
    
    return render(request,'profile/profile.html',{'profile':profile_user })

def  profile_edit(request):
    profile_user = profile.objects.get(user = request.user)
    if request.method == 'POST':
        form_user = UserForm(request.POST,instance=request.user) 
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile_user)
        if form_user.is_valid() and profile_form.is_valid():
            form_user.save() 
            myprofile = profile_form.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        form_user = UserForm(instance=request.user) 
        profile_form = ProfileForm(instance=profile_user)        
    return render(request,'profile/profile_edit.html',{'userform':form_user,'profileform':profile_form})