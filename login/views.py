from django.shortcuts import render
from .forms import Signupform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from myapp import views

def signup(request):
    firstname=''
    lastname=''
    emailvalue=''
    uservalue=''
    passwordvalue1=''
    passwordvalue2=''

    form= Signupform(request.POST or None)
    if form.is_valid():
        fs= form.save(commit=False)
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        emailvalue= form.cleaned_data.get("email")
        uservalue= form.cleaned_data.get("username")
        passwordvalue1= form.cleaned_data.get("password1")
        passwordvalue2= form.cleaned_data.get("password2")
        if passwordvalue1 == passwordvalue2:
            try:
                user= User.objects.get(username=uservalue) #if able to get, user exists and must try another username
                context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'signup.html', context)
            except User.DoesNotExist:
                user= User.objects.create_user(uservalue, password= passwordvalue1,
                                           email=emailvalue)
                user.save()


                login(request,user)

                fs.user= request.user

                fs.save()
                context= {'form': form}
                return render(request, 'index.html', context)
            
        else:
            context= {'form': form, 'error':'The passwords that you provided don\'t match'}
            return render(request, 'signup.html', context)
        

    else:
        context= {'form': form}
        return render(request, 'signup.html', context)
""" login function"""

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("index/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print  ("invalid login details ") + username + " " + password
              return render_to_response('login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render_to_response('login.html', {}, context)
