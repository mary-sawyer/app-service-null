from django.db import models

class Departments(models.Model):
	# employee from dept
	DeptNum = models.CharField(max_length=50)
	Dept = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s %s' % (self.DeptNum, self.Dept)
