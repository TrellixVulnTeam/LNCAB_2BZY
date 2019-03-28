from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Player
from django.shortcuts import redirect

from .forms import PlayerForm,UserForm,LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required



def index(request):
    template = loader.get_template('../templates/header.html')
    players = Player.objects.all()
    context={"players":players,
    }

    return HttpResponse(template.render(context,request))


@login_required
def logged_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    return render(request,'logged_index.html',{'user':user})



def registerUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/users/playerform.html')
    else:
        user_form = UserForm()
    return render(request, '../templates/userform.html', {'user_form': user_form})




def registerPlayer(request):
    if request.method == 'POST':
        player_form = PlayerForm(request.POST)
        if player_form.is_valid():
            new_player=player_form.save(commit=False)
            new_player.save()
            return render(request,'../templates/playerform_done.html',{'new_player':new_player})
    else:
        player_form=PlayerForm()
    return render(request, '../templates/playerform.html', {'player_form': player_form})



def user_login(request):
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                password=cd['password'])
            pk=user.pk

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/users/'+str(pk))
                else:
                    return HttpResponse('Disabled account')

        else:
            return HttpResponse('Wrong credentials')
    else:
        login_form=LoginForm()
    return render(request,'../templates/login.html',{'login_form':login_form})




def logout(request):
    return redirect('/users/')






