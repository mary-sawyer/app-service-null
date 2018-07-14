from django import forms
from django.forms import ModelForm
from volunteer.models import Vol_info
from org.models import Org_info
MUSLIM = 'Muslim Community at PANW'
LGBTQ = 'LGBTQ'
WOMEN = 'Women'
CHILD_WELFARE= 'Child'
HEALTH = 'Health'
VETERAN = 'Vet'
NO='None'
PROGRAMMING = 'Programming'
COOK = 'Cooking'
TEACHING = 'Teaching'
ORGANIZING ='Organizing'
LEGAL='Legal'
CAMPING = 'Camping'
PAINTING= 'Painting'
MUSIC = 'Music'
PHYSICAL_WORK = 'Physical Work'
CYBERSECURITY = 'Cybersecurity Education and Awareness'
'''
LOCAL_INVOLVEMENT = 'Local Involvement'
SW_COMP = 'Software and Computers'
BUILD = 'Physical Work'
LOCAL_INVOLVEMENT = 'Local Involvement'
ENVIRONMENT = 'Environment'
DONATION = 'Donation'
SW_COMP = 'Software and Computers'
BUILD = 'Physical Work'
TRAINING ='Training and Education'
DONATION = 'Donation'
'''
NOTHING='Nothing'
NOT='Not'
SOCIETIES = ((MUSLIM,'Muslim Community at PANW'),(LGBTQ,'LGBTQ Community at PANW'),(HEALTH,'Health and Witness at PANW'),(CHILD_WELFARE, 'Child Welfare Organization'),(VETERAN,'Vet'),(NO,'None'))        

SKILL = ((PROGRAMMING,'Programming'),(COOK, 'Cooking'),(TEACHING, 'Teaching'),(ORGANIZING,'Organizing'),(LEGAL,'Legal'),(CAMPING, 'Camping'),(PAINTING, 'Painting'),(MUSIC, 'Music'),(PHYSICAL_WORK, 'Physical Activity'),(CYBERSECURITY,'Cybersecurity education'),)

#PROJECTS =((LOCAL_INVOLVEMENT, 'LOCAL INVOLVEMENT'),(ENVIRONMENT, 'Environment'),(DONATION, 'Donation'),(SW_COMP, 'Software and Computers'),(BUILD, 'Physical Work'),(TRAINING, 'Training and Education'),(DONATION, 'Donation'))

class Volunteer_info_form(ModelForm):
	soc = forms.MultipleChoiceField(choices=SOCIETIES, widget=forms.CheckboxSelectMultiple())
#	project_choices=[(i['name'], i['name']) for i in Org_info.objects.values('name').distinct()]
	
	p_type = forms.MultipleChoiceField(choices=lambda:[ (i['name'], i['name']) for i in Org_info.objects.values('name').distinct() ], widget=forms.CheckboxSelectMultiple(), label='Projects you may be interested')
	skill = forms.MultipleChoiceField(choices=SKILL, widget=forms.CheckboxSelectMultiple())
	class Meta:
		model = Vol_info
		soc = forms.MultipleChoiceField(choices=SOCIETIES, widget=forms.CheckboxSelectMultiple())
#		project_type = forms.ChoiceField(choices=PROJECTS, widget=forms.CheckboxSelectMultiple())
		skills = forms.ChoiceField(choices=SKILL, widget=forms.CheckboxSelectMultiple())
#		widgets = {
#		'society':forms.CheckboxSelectMultiple()
#		
#		}
		fields = ['name','location','gender','commitment','job']		

