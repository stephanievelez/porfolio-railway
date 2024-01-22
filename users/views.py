from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render

def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index')) #reverse() gets URL from a named URL pattern, so Django redirects to the topics page


def register(request):
    """Register a new user"""
    if request.method == "POST":
        #Display blank registration form
        form = UserCreationForm()

    else:
        #process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1']) #get the password,after matched, of the 1st password..username and password
            #are saved under authenticated user
            login(request, authenticated_user) #creates a valid session for the new user
            return HttpResponseRedirect(reverse('learning_logs:index'))

        context = {'form': form}
        return render(request, 'users/register.html', context)