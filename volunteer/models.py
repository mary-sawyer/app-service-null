from django.db import models

# Create your models here.
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

	MUSLIM = 'Muslim Community at PANW'
	LGBTQ = 'LGBTQ'
	WOMEN = 'Women'
	CHILD_WELFARE= 'Child'
	HEALTH = 'Health'
	VETERAN = 'Vet'
	NO='None'
	
	GENDER_CHOICES=((MALE, 'Male'),(FEMALE, 'Female'),(OTHER, 'Other'),(NOSAY, 'Prefer not to say'))
	COM_LEVELS=((LOW,'Less than 10 hours/week'),(MEDIUM,'From 5-10 hours/week'),(HIGH, 'More than 10 hours/week'))
	
	PREV_EXP=((NONE, 'None'),(FAIR, 'Worked with some organizations before'),(GOOD, 'Worked with more than 5 organizations before'),(SUPERIOR,'Worked with more than 10 organizations before'))
	JOB_DESCRIPTIONS=((BUSINESS,'Business'),(IT,'IT'),(Infosec,'Infosec'),(SALES,'Sales and Marketing'))
	SOCIETIES = (
	(MUSLIM,'Muslim Community at PANW'),
	(LGBTQ,'LGBTQ Community at PANW'),
	(HEALTH,'Health and Witness at PANW'),
	(CHILD_WELFARE, 'Child Welfare Organization'),
	(VETERAN,'Vet'),
	(NO,'None')
	)
	name=models.CharField(max_length=255)
	location=models.CharField(max_length=255)
	gender=models.CharField(max_length=255, choices=GENDER_CHOICES)
	#commitment=models.CharField(max_length=255, choices=COM_LEVELS, default=LOW)
	prev_exp=models.CharField(max_length=255, choices=PREV_EXP,default=NONE)
	job=models.CharField(max_length=255, choices=JOB_DESCRIPTIONS,default=IT)
	skills=models.CharField(max_length=1000)
	society=models.CharField(max_length=255, choices=SOCIETIES, default=NO)
	
	
