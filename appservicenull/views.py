from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from fusioncharts import FusionCharts
from .models import *
import json

# Create your views here.
def index(request):
	cursor1 = connection.cursor()
	cursor1.execute("""select job, count(job) from volunteer_vol_info GROUP BY job""")
	data = cursor1.fetchall()
	
	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
	dataSource['chart'] = { 
		"caption": "Volunteer Rank",
		"subCaption": "See how your department compares!",
		"xAxisName": "Department",
		"yAxisName": "Employees",
		"theme": "zune"
	}
	
	dataSource['data'] = []
	for i in data:
		data = {}
		data['label'] = i[0]
		data['value'] = i[1]
		dataSource['data'].append(data)
	print(json.dumps(dataSource))
	# Create an object for the Column 2D chart using the FusionCharts class constructor
	column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
	return render(request,'index.html', {'output': column2D.render()})
def input(request):
	return render(request,'volunteer/input.html')
