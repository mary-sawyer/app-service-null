from django.forms import ModelForm
from volunteer.models import Vol_info
class Volunteer_info_form(ModelForm):
	class Meta:
		model = Vol_info
		fields = '__all__'

