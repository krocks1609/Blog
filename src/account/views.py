from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout

from account.forms import RegistrationForm,AccountAuthenticationForm,AccountUpdateForm
from blog.models import BlogPost

def registration_view(request):
    context={}
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')

            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  #get request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')



def login_view(request):
    context={}
    user = request.user
    print("User context created")
    if user.is_authenticated:
        return redirect("home")

    if request.POST:                                               #when clicked on login button
        print("clicked on login")
        form = AccountAuthenticationForm(request.POST)
        print("fforrm")
        if form.is_valid():
            print("VVVVVV")
            email = request.POST['email']
            print("e")
            password = request.POST['password']
            print("p")
            user = authenticate(email=email, password=password)
            print("a")
            if user:
                login(request, user)
                print("user obj exists")
                return redirect("home")

    else:   #user not authecticated(i.e. viewing login page without authentication)
        form = AccountAuthenticationForm()
        print("inside else")
    print("Going for context")
    context['login_form'] = form
    print("Context Rendering")
    return render(request, 'account/login.html', context)




def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context={}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.user.email,
                "username": request.user.username,
            }
            form.save()

            context['success_message'] = 'Updated'

    else:
        form = AccountUpdateForm(
            initial={
                "email" : request.user.email,
                "username" : request.user.username,
            }
        )

    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts
    return render(request, 'account/account.html', context)

def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})








