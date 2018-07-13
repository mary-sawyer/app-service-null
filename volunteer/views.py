from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Volunteer_info
from django.urls import reverse
from .forms import Volunteer_info_form
# Create your views here.
def input(request):
    # if this is a POST request we need to process the form data
	volunteer_dbobj=Volunteer_info()
	if(request.method == 'POST'):
        # create a form instance and populate it with data from the request:
		form = Volunteer_info_form(data=request.POST)
        # check whether it's valid:
		if form.is_valid():
			form.name=form.cleaned_data.get('name')
			form.location=form.cleaned_data.get('location')
			form.gender=form.cleaned_data.get('gender')
			
			print("Form's Valid. YAYYY!")
			volunteer_dbobj.name=form.name;
			volunteer_dbobj.location=form.location;
			volunteer_dbobj.gender=form.gender;
			
			volunteer_dbobj.save();
			
			return HttpResponseRedirect(reverse('input'),)
    # if a GET (or any other method) we'll create a blank form
	else:
		form = Volunteer_info_form()
	return render(request, 'input.html', {'form':form , 'volunteer_info': Volunteer_info.objects.all() }, )
