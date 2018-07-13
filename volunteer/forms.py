from django.forms import ModelForm
from volunteer.models import Volunteer_info

class Volunteer_info_form(ModelForm):
	class Meta:
		model = Volunteer_info
		fields = '__all__'

