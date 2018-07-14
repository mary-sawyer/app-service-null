from django.db import models
SANTA_CLARA='SC'
FREMONT='FR'
SSJC= 'South San Jose'
WSJC='West san jose'
ESJC= 'East San Jose'
MPTAS='Milpitas'
MV='Mountain View'
PA='palo alto'
MP='melon park'
NONE= 'None'
# Create your models here.
CITIES = (
	(SANTA_CLARA,'SC'),
	(FREMONT,'FR'),
	(SSJC, 'South San Jose'),
	(WSJC,'West san jose'),
	(ESJC, 'East San Jose'),
	(MPTAS,'Milpitas'),
	(MV, 'Mountain View'),
	(PA,'palo alto'),
	(MP, 'melon park'),
	(NONE, 'None'),
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
	address=models.CharField(max_length=255, choices=CITIES, default=NONE)
	work_hours=models.IntegerField()
#	project_type=models.CharField(max_length=255, choices=PROJECTS)
	desired_background=models.CharField(max_length=255)
