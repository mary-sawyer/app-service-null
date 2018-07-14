from django import forms
from django.forms import ModelForm
from org.models import Org_info
PROGRAMMING = 'Programming'
COOK = 'Cooking'
TEACHING = 'Teaching'
ORGANIZING ='Organizing'
LEGAL = 'Legal'
CAMPING = 'Camping'
PAINTING = 'Painting'
MUSIC = 'Music'
PHYSICAL_WORK = 'Physical Activity'
CYBERSECURITY ='Cybersecurity education'
MUSLIM = 'Muslim Employee Network'
LGBTQ = 'LGBTQ'
WOMEN = 'Women'
VETERAN='Veterans Employee Network'
JUNTOS='JUNTOS'
BLACK='Black Employee Network'
EARLY= 'Early in Career'
NO='None'
BACKGROUND=(
	(PROGRAMMING,'Programming'),
	(COOK, 'Cooking'),
	(TEACHING, 'Teaching'),
	(ORGANIZING,'Organizing'),
	(LEGAL,'Legal'),
	(CAMPING, 'Camping'),
	(PAINTING, 'Painting'),
	(MUSIC, 'Music'),
	(PHYSICAL_WORK, 'Physical Activity'),
	(CYBERSECURITY,'Cybersecurity education'),
	(MUSLIM,'Muslim Employee Network'),
	(LGBTQ,'LGBTQ'),
	(VETERAN,'Veterans Employee Network'),
	(JUNTOS,'JUNTOS'),
	(BLACK,'Black Employee Network'),
	(EARLY, 'Early in Career'),
	(NO,'None')
	)


class Org_info_form(ModelForm):
	bg = forms.MultipleChoiceField(choices=BACKGROUND, widget=forms.CheckboxSelectMultiple(), label='Desired Background')
	class Meta:
		model = Org_info
		fields = ['name','description','participants','address','work_hours']

