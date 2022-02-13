from django.shortcuts import render
import requests
from .models import *
from .forms import *
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def index(request):
	now = datetime.datetime.now()
	if request.method == 'POST':
		city = request.POST.get('city')
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=38bb75c4fc58317f9725959133500028'
		city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
		weather_data = []
		print(type(city_weather['cod']))
		if city_weather['cod'] == 200:
			cityObj,created = City.objects.get_or_create(name=city.title())
			weather = {
		        'city' : cityObj,
		        'temperature' : city_weather['main']['temp'],
		        'description' : city_weather['weather'][0]['description'],
		        'icon' : city_weather['weather'][0]['icon']
		    }
			form = WeatherRecordForm(weather)
			if form.is_valid():
				form.save()
			else:
				for field in form:
					for error in field.errors:
						messages.warning(request, "%s : %s" % (field.name, error))
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			weather_data = WeatherRecord.objects.filter(created_at__date=now.date())
			context = {
				'weather': weather_data,
			}
			return render(request, 'weather_dashboard/index.html', context)
		else:
			messages.warning(request, "City Name is Incorrect!!")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		weather_data = WeatherRecord.objects.filter(created_at__date=now.date())
		context = {
			'weather': weather_data,
		}
		return render(request, 'weather_dashboard/index.html', context) #returns the index.html template
