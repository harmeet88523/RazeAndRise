# This one of my most documented views file
# It is never too late to start a good habit

##################################################### IMPORT STATEMENTS ###########################################################

from django.shortcuts import render
from main.models import *

###################################################### GLOBAL VARIABLES ###########################################################

asset_sellof_rate = #<complete>
labour_sellof_rate = asset_sellof_rate #<complete>

########################################################## VIEWS ####################################################################

# Create your views here.

def add_value(request):
	if request.method == 'POST':
		form=AddValueForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			for t in data['team_list']:	
				try :
					team=Team.objects.get(no=t)
				except : #<complete> object not found specific error
					return HttpResponse('Team not found according to number')
				#<complete> for all assets money and labour

#This view is when a team wants to invoke a use_power
#This view checks whether a team that has a particular power has it or no
#This view also checks whether the affetcted team has any safegaurds
def use_power(request):
	#<complete>

# This views allows a team to buy a power
# This view will check whether there is quantity left of that power
# It also checks whether the team has enough money to buy the power
def buy_power(request):
	#<complete>

# This is a function and not a django view
# It is used to sell of a team's assets or labour
# It will sell of at the predetermined rate
def sell_commodities(term):
	#<complete>

# This view allows a team to sell of its commodities
# It will ensure that the team has the quantity that it intends to sell
def sell(request):
	#<complete>

# This is a view which is called when a round gets over
# It will automatically generate cash for a team at the end
# It will calculate the net worth of the company at the end of each round and store it in the database
def round_completion(request):
	#<complete>

# This is a function and not a view 
# This is used to calculate the net worth of a team and store it in the database
# This function is invoked in almost every view to update the networth of the team
def calculate_net_worth(team):
	#<complete>

# This is a an experiment from my side
# This view is to revert back a mistake if made
# This is done by generating a log and reverting back as and when required
def revert_back(request):
	#<complete>

############################################# OPTIONAL SEGMENT ######################################################################

# This view allows a team to buy a question
# This view will also check whether the team has enough money to buy that question
# It will also sell of the commodities of the company at the predecided rate to raise money to buy the question
def buy_question(request):
	#<complete>
	#<optional> write only if the the question wala thing has to be incorporated

# This view is called when a team answers a question
# It checks whether an answer is right or not and accordingly awards the team
def attempt_question(request):
	#<complete>
	#<optional> write only if the the question wala thing has to be incorporated