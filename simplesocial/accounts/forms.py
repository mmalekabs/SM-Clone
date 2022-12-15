from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateFrom(UserCreationForm): #This calss which is inheret from UserCreationForm must have another name (in my situation it is UserCreateForm)
    
    class Meta:
        fields = ('username', 'email', 'password', 'passwordConfirmation')
        model = get_user_model()
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            #Here we are doing a label from the form view instead of HTML page
            self.fields['username'].label = "Display Name"
            self.fields['email'].label = "Email Address"