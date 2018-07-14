from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Org_info
from django.urls import reverse
from .forms import Org_info_form
from django.db import connection


# Create your views here.
def dashboard(request):
	# if this is a POST request we need to process the form data

	org_dbobj=Org_info()
	match_cursor = connection.cursor()
	match_cursor.execute("""select * from matchscore""")
	data = match_cursor.fetchall()
	if(request.method == 'POST'):
        # create a form instance and populate it with data from the request:
		form = Org_info_form(data=request.POST)
        # check whether it's valid:
		if form.is_valid():
			form.name=form.cleaned_data.get('name')
			form.description=form.cleaned_data.get('description')
			form.participants=form.cleaned_data.get('participants')
			form.address=form.cleaned_data.get('address')
			form.work_hours=form.cleaned_data.get('work_hours')
	#		form.p_type=form.cleaned_data.get('p_type')
			form.bg=form.cleaned_data.get('bg')
			print("Form's Valid. YAYYY!")
			org_dbobj.name=form.name;
			org_dbobj.description=form.description;
			org_dbobj.participants=form.participants;
			org_dbobj.address=form.address;
			org_dbobj.work_hours=form.work_hours;
	#		org_dbobj.project_type=form.p_type;
			org_dbobj.desired_background=form.bg;
			org_dbobj.save();
			'''
			match_cursor = connection.cursor()
			match_cursor.execute("""select * from matchscore GROUP BY name""")
			data = match_cursor.fetchall()
			'''
			return HttpResponseRedirect(reverse('dashboard'),)

	else:
		form=Org_info_form()
	return render(request, 'dashboard.html', {'form':form , 'data': data  },)





