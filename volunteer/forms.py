from django import forms
from django.forms import ModelForm
from volunteer.models import Vol_info
from org.models import Org_info
MUSLIM = 'Muslim Employee Network'
LGBTQ = 'LGBTQ'
WOMEN = 'Women'
VETERAN='Veterans Employee Network'
JUNTOS='JUNTOS'
BLACK='Black Employee Network'
EARLY= 'Early in Career'
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
SOCIETIES = (
	(MUSLIM,'Muslim Employee Network'),
	(LGBTQ,'LGBTQ'),
	(VETERAN,'Veterans Employee Network'),
	(JUNTOS,'JUNTOS'),
	(BLACK,'Black Employee Network'),
	(EARLY, 'Early in Career'),
	(NO,'None')
)
SKILL = ((PROGRAMMING,'Programming'),(COOK, 'Cooking'),(TEACHING, 'Teaching'),(ORGANIZING,'Organizing'),(LEGAL,'Legal'),(CAMPING, 'Camping'),(PAINTING, 'Painting'),(MUSIC, 'Music'),(PHYSICAL_WORK, 'Physical Activity'),(CYBERSECURITY,'Cybersecurity education'),)

#PROJECTS =((LOCAL_INVOLVEMENT, 'LOCAL INVOLVEMENT'),(ENVIRONMENT, 'Environment'),(DONATION, 'Donation'),(SW_COMP, 'Software and Computers'),(BUILD, 'Physical Work'),(TRAINING, 'Training and Education'),(DONATION, 'Donation'))

class Volunteer_info_form(ModelForm):
	soc = forms.MultipleChoiceField(choices=SOCIETIES, widget=forms.CheckboxSelectMultiple(), label="Employee Networks you are a part of:")

#	project_choices=[(i['name'], i['name']) for i in Org_info.objects.values('name').distinct()]
	
	p_type = forms.MultipleChoiceField(choices=lambda:[ (i['name'], i['name']) for i in Org_info.objects.values('name').distinct() ], widget=forms.CheckboxSelectMultiple(), label='Projects you may be interested')
	skill = forms.MultipleChoiceField(choices=SKILL, widget=forms.CheckboxSelectMultiple(), label = 'Skills you think you could contribute:')
	class Meta:
		model = Vol_info
		soc = forms.MultipleChoiceField(choices=SOCIETIES, widget=forms.CheckboxSelectMultiple())
#		project_type = forms.ChoiceField(choices=PROJECTS, widget=forms.CheckboxSelectMultiple())
		skills = forms.ChoiceField(choices=SKILL, widget=forms.CheckboxSelectMultiple(), label = 'Skills you think you could contribute:')
#		widgets = {
#		'society':forms.CheckboxSelectMultiple()
#		
#		}
		fields = ['name','location','gender','commitment','job']		

