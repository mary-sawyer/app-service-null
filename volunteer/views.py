from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import Volunteer_info_form
# Create your views here.
def input(request):
    # if this is a POST request we need to process the form data
	if(request.method == 'POST'):
        # create a form instance and populate it with data from the request:
		form = Volunteer_info_form(request.POST)
        # check whether it's valid:
		if form.is_valid():
			print("Form's Valid. YAYYY!")
			return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
	else:
		form = Volunteer_info_form()
	return render(request, 'input.html', {'form':form})
