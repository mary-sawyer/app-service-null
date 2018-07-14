from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Vol_info
from django.urls import reverse
from .forms import Volunteer_info_form
from django.db import connection
# Create your views here.
def input(request):
    # if this is a POST request we need to process the form data
	volunteer_dbobj=Vol_info()
	match_cursor = connection.cursor()
	match_cursor.execute("""select * from matchscore""")
	data = match_cursor.fetchall()

	if(request.method == 'POST'):
        # create a form instance and populate it with data from the request:
		form = Volunteer_info_form(data=request.POST)
        # check whether it's valid:
		if form.is_valid():
			form.name=form.cleaned_data.get('name')
			form.location=form.cleaned_data.get('location')
			form.gender=form.cleaned_data.get('gender')
#			form.prev_exp=form.cleaned_data.get('prev_exp')
			form.job=form.cleaned_data.get('job')
			form.skill=form.cleaned_data.get('skill')
			form.soc=form.cleaned_data.get('soc')
			form.p_type=form.cleaned_data.get('p_type')
			form.commitment=form.cleaned_data.get('commitment')
			print("Form's Valid. YAYYY!")
			volunteer_dbobj.name=form.name;
			volunteer_dbobj.location=form.location;
			volunteer_dbobj.gender=form.gender;
			#volunteer_dbobj.prev_exp=form.prev_exp;
			volunteer_dbobj.job=form.job;
			volunteer_dbobj.skills=form.skill;
			volunteer_dbobj.society=form.soc;
			volunteer_dbobj.project=form.p_type
			volunteer_dbobj.commitment=form.commitment

			volunteer_dbobj.save();
			
			return HttpResponseRedirect(reverse('input'),)
    # if a GET (or any other method) we'll create a blank form
	else:
		form = Volunteer_info_form()
	return render(request, 'input.html', {'form':form , 'data':data }, )
	
