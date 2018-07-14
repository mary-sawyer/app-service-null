from django.db import models

# Create your models here.
SANTA_CLARA='Santa Clara'
FREMONT='Fremont'
SSJC= 'South San Jose'
WSJC='West San Jose'
ESJC= 'East San Jose'
MPTAS='Milpitas'
MV='Mountain View'
PA='Palo Alto'
MP='Menlo Park'


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


class Vol_info(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	OTHER = 'O'
	NOSAY = 'N'
        
	LOW = 'L'
	MEDIUM = 'M'
	HIGH = 'H'
	NONE = 'N'

	FAIR = 'FAIR'
	GOOD = 'GOOD'
	SUPERIOR = 'S'
       
	BUSINESS = 'B'
	IT = 'IT'
	Infosec = 'Infosec'
	SALES = 'S&M'

	MUSLIM = 'Muslim Employee Network'
	LGBTQ = 'LGBTQ'
	VETERAN='Veterans Employee Network'
	JUNTOS='JUNTOS'
	BLACK='Black Employee Network'
	EARLY= 'Early in Career'
	WOMEN = 'Women Network'
	NO='None'

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

	LOCAL_INVOLVEMENT = 'Farm Work'
	ENVIRONMENT = 'Coastal Conservation'
	DONATION = 'Blood Drive'
	SW_COMP = 'Food Bank App'
	BUILD = 'Construction project'
	TRAINING ='Tech for Children'

	NOTHING='Nothing'
	NOT='Not'
	
	GENDER_CHOICES=((MALE, 'Male'),(FEMALE, 'Female'),(OTHER, 'Other'),(NOSAY, 'Prefer not to say'))
	COM_LEVELS=((LOW,'Less than 10 hours/week'),(MEDIUM,'From 5-10 hours/week'),(HIGH, 'More than 10 hours/week'))
	
	#PREV_EXP=((NONE, 'None'),(FAIR, 'Worked with some organizations before'),(GOOD, 'Worked with more than 5 organizations before'),(SUPERIOR,'Worked with more than 10 organizations before'))
	JOB_DESCRIPTIONS=((BUSINESS,'Business'),(IT,'IT'),(Infosec,'Infosec'),(SALES,'Sales and Marketing'))
	SOCIETIES = (
	(MUSLIM,'Muslim Employee Network'),
	(LGBTQ,'LGBTQ'),
	(VETERAN,'Veterans Employee Network'),
	(JUNTOS,'JUNTOS'),
	(BLACK,'Black Employee Network'),
	(EARLY, 'Early in Career'),
	(WOMEN, 'Women Network'),
	(NO,'None')
	)
	
	SKILL = (
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
	)
	PROJECTS =(
	(LOCAL_INVOLVEMENT, 'Farm Work'),
	(ENVIRONMENT, 'Coastal Conservation'),
	(DONATION, 'Blood Drive'),
	(SW_COMP, 'Food Bank App'),
	(BUILD, 'Construction project'),
	(TRAINING, 'Tech for Children'),
	)

	
	name=models.CharField(max_length=255)
	location=models.CharField(max_length=255, choices=CITIES)
	gender=models.CharField(max_length=255, choices=GENDER_CHOICES)
	commitment=models.CharField(max_length=255, choices=COM_LEVELS, default=LOW)
	#prev_exp=models.CharField(max_length=255, choices=PREV_EXP,default=NONE)
	job=models.CharField(max_length=255, choices=JOB_DESCRIPTIONS,default=IT)
	skills=models.CharField(max_length=1000)
	society=models.CharField(max_length=255)
	project=models.CharField(max_length=255)	
	
	
