from django.shortcuts import render

# Create your views here.
def add_money(request):
	if request.method == 'POST':
		form=AddMoneyForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			for t in data['team_list']:	
				try :
					team=Team.objects.get(no=t)
				except : #<complete> object not found specific error
					return HttpResponse('Team not found according to number')
				