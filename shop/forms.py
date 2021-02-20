from django.forms import ModelForm
from .models import Logins

class Loginsform(ModelForm):
   class Meta:
      model = Logins
      fields = '__all__'