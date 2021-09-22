from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Email Address Required')
    class Meta:
        model = Account
        fields = ("email","username","password1","password2")



class AccountAuthenticationForm(forms.ModelForm):
    print("here")
    password = forms.CharField(label='Password', widget=forms.PasswordInput)    #by default test field widget will make password not readable

    class Meta:
        model = Account
        fields = ('email', 'password')                                          #these two fields will be visible on login screen.
        print(" then here")
    def clean(self):                                                           #before anything is done this will be executed (an interceptor kind)
        print("in clean now")
        if self.is_valid():                                                  #check for form validation
            email = self.cleaned_data['email']                              #to convert the data to appropriate form and send to server
            password = self.cleaned_data['password']#same as above
            print("cleaned")
            if not authenticate(email=email, password=password):
                print("called authenticate and checked authenication")
                raise forms.ValidationError("Invalid login")

        print("exiting clean method")





class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email','username')


    def clean_email(self):
        # pass
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
                print("inside try")
            except Account.DoesNotExist:
                return email
                print("inside except")
            raise forms.ValidationError('Email "%s" is already in use' % email)



    def clean_username(self):
        # pass
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use' % username)




