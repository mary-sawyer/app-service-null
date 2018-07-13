ngo.forms import ModelForm
from org.models import Org_info

class Org_info_form(ModelForm):
        class Meta:
                model = Org_info
                fields = '__all__'

