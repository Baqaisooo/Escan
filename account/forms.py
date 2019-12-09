from django.contrib.auth.forms import UserCreationForm
from .models import User

class USERCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "phone", "region", "city")
