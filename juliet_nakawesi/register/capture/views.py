from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            new_player = form.save(commit=False)
            new_player.save()
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
