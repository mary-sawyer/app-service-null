from django.db import models
SANTA_CLARA='Santa Clara'
FREMONT='Fremont'
SSJC= 'South San Jose'
WSJC='West San Jose'
ESJC= 'East San Jose'
MPTAS='Milpitas'
MV='Mountain View'
PA='Palo Alto'
MP='Menlo Park'

# Create your models here.
CITIES = (
	(SANTA_CLARA,'Santa Clara'),
	(FREMONT,'Fremont'),
	(SSJC, 'South San Jose'),
	(WSJC,'West San Jose'),
	(ESJC, 'East San Jose'),
	(MPTAS,'Milpitas'),
	(MV, 'Mountain View'),
	(PA,'Palo Alto'),
	(MP, 'Menlo Park'),
	)

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
LOCAL_INVOLVEMENT = 'Farm Work'
ENVIRONMENT = 'Coastal Conservation'
DONATION = 'Blood Drive'
SW_COMP = 'Food Bank App'
BUILD = 'Construction project'
TRAINING ='Tech for Children'


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

class Org_info(models.Model):
	name=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	participants=models.IntegerField()
	address=models.CharField(max_length=255, choices=CITIES, default=SANTA_CLARA)
	work_hours=models.IntegerField()
#	project_type=models.CharField(max_length=255, choices=PROJECTS)
	desired_background=models.CharField(max_length=255)
