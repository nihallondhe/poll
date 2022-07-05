from django.forms import ModelForm

from .models import Poll

from .models import User

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'



class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'