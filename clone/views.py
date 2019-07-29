from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Image, Profile,Comments
from .forms import NewComment,NewImage,UpdateProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def homepage (request):
    return render(request,'home.html')

@login_required(login_url='/accounts/login')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImage(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homepage')
    else:
        form = NewImage()
    return render(request, 'post.html', {"form": form})

