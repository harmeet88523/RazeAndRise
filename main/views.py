# This one of my most documented views file
# It is never too late to start a good habit

##################################################### IMPORT STATEMENTS ###########################################################

from django.shortcuts import render
from main.models import *

###################################################### GLOBAL VARIABLES ###########################################################

sell_dict={'assets' : ,'labour' :  }

# Here nw - networth
nw_rate_dict={}
nw_rate_dict['assets']=1 #<complete>
nw_rate_dict['labour']=1 #<complete>

#Here cg - cash generation
cg_rate_dict = {}
cg_rate_dict['assets']=1 #<complete>
cg_rate_dict['labour']=1 #<complete>

#This stores the minimum limit below which a team cannot sell its commodities
min_lim={}
min_lim['assets']=0 #<complete>
min_lim['labour']=0 #<complete>

#This is the minimum limit that one has to kept while initially distributing the commodities
i_min_limit={}
i_min_limit['assets']=0 #<complete>
i_min_limit['labour']=0 #<complete>

initial_value=500000 #<complete>

########################################################## VIEWS ####################################################################

# Create your views here.

#This view is used to add a new team to the database
#This view also checks whether it isnt less than the minimum amount decided the initial amount as decided
def add_team():
	


#This view is used to add value to a particular team
def add_value(request):#<done>
	if request.method == 'POST':
		form=AddValueForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			add_commodity(data['team'],data['commodity'],data['amount'])
			calculate_net_worth(data['team'])
		else:
			return HttpResponse('Invalid')#<complete> 
	else:
		raise Http404 #<complete>

#TC: This is a python function and not a view
#This function adds value to the particular commodity of a team
def add_commodity(team,term,amount):
	final_amount=getattr(team,term) + amount
	setattr(team,term,amount)
	return

#This view is when a team wants to invoke a power
#This view checks whether a team that has a particular power has it or no
#This view also checks whether the affected team has any safegaurds
def use_power(request):
	if request.method =='POST':
		form=UsePowerForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			try : 
				using_team = Team.objects.get(data['using_team']) # This is the team which is using the power 
			except: #<complete> specific error code
				return HttpResponse('No such team exists') #<complete> check whether any json needed
			try : 
				used_team = Team.objects.get(data['used_team']) # This is the team on which the power is being used
			except: #<complete> specific error code
				return HttpResponse('No such team exists') #<complete> check whether any json needed
			
			# Checking if either of teams is eliminated

			if using_team.is_eliminated == True or used_team.is_eliminated == True:
				return HttpResponse('One of the teams is already eliminated') #<complete> check whether any json needed

			# Checking if the 'using_team' has the power it wants to use

			if not using_team.powers.filter(pk=data['power'].pk):
				return HttpResponse('The team doesnt have this power') #<complete> check for json
			
			# Checking if the power is 'Attack' type or 'Defense' type

			if data['power'].type == 'defense':
				return HttpResponse('The power being used is of defense type') #<complete> check for json
			
			# Checking for safeguards, if any.
			# Here the rule is if you have a safeguard of say x value and attack on you is of y value
			# If x < y then x is fully used and the remainder damage is done.
			# If x >= y then x is fully used and no damage is done.
			# Also, multiple smaller safeguards can be used.
			# If both less and greater than safeguards present then lesser than used first

			safeguards_used_team = used_team.powers.filter(category='defense',commodity = data['power'].commodity)
			safeguards_used_team_e = safeguards_used_team.filter(strength=data['power'].strength) # Here 'e' is for equal strength
			safeguards_used_team_l = safeguards_used_team.filter(strength__lt=data['power'].strength).order_by('strength') # Here 'l' is for lesser strength
			safeguards_used_team_g = safeguards_used_team.filter(strength__gt=data['power'].strength).order_by('strength') # Here 'g' is for greater strength

			net_attack = 0 # Here this represents the net attack after safeguards
			
			if safeguards_used_team_e:
				net_attack=0
			elif safeguards_used_team_l:
				for s in safeguards_used_team_l:
					if 






# This views allows a team to buy a power
# This view will check whether there is quantity left of that power
# It also checks whether the team has enough money to buy the power
def buy_power(request): #<partially done>
	if request.method == 'POST':
		form = BuyPowerForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			try :
				team=Team.objects.get(no=data['team'])				
			except: #<complete> specific error code
				return HttpResponse('No such team exists') #<complete> check whether any json needed

			# Checking whether the team is eliminated

			if team.is_eliminated == 'True':
				return HttpResponse('Team already eliminated') #<complete> check whether any json needed

			# Here it will check if the team has enough money to buy that power

			if team.money < data['price']:
				return HttpResponse('Not enough money') #<complete> check whether any json needed

			# End Block

			try:
				p=Power.objects.get(category=data['category'],price=data['price'],strength=data['strength'])
			except : #<complete> The specific error code
				return	HttpResponse('No such power exists') #<complete> check whether any json needed

			# Here validation will be done to check if enough quantity left of that power

			if p.quantity == 0:
				return HttpResponse('This power is over') #<complete> check whether any json needed
			else :
				team.money-= p.price 
				team.powers.add(p)
				calculate_net_worth(team)
				p.quantity -= 1
				p.save()

			# End of Block

			return HttpResponse('Success') #<complete> send updated json
		else :
			return HttpResponse('Failure') #<complete> send updated json
	else : 
		#<complete> Decide what to do
		raise Http404


# This is a function and not a django view
# It is used to sell of a team's assets or labour
# It will sell of at the predetermined rate
# It will ensure that the team has the quantity that it intends to sell
def sell_commodities(team,term,amount):#<done>
	# Here is checks if the team has enough quantity to sell the respective commodity

	if final_amount < min_lim[term]:
		return False

	final_amount=getattr(team,term) - amount
	setattr(team,term,final_amount)
	team.money += sell_dict[term] * amount
	calculate_net_worth(team)
	return True

# This view allows a team to sell of its commodities
def sell(request):#<partially done>
	if request.method == 'POST':
		form = SellCommoditiesForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			if data['team'].is_eliminated == True:
				return HttpResponse('team already eliminated')

			if not sell_commodities(data['team'],data['commodity'],data['amount']):
				return HttpResponse('Cant Sell any more of ' + data['commodity']) #<complete> check for json response
			else :
				return HttpResponse('Done') #<complete> check for json response
		else:
			return HttpResponse('Invalid data sent') #<complete> check for json response
	else:
		raise Http404

# This is a view which is called when a round gets over
# It will automatically generate cash for a team at the end
# It will calculate the net worth of the company at the end of each round and store it in the database
def round_completion(request):#<partially done>
	if request.method == 'POST':
		team_list=Team.objects.filter(is_eliminated=False)
		for team in team_list:
			team.money += team.assets * cg_rate_dict['assets'] + team.labour * cg_rate_dict['labour']
			calculate_net_worth(team)
		return HttpResponse('Done') #<complete> send json
	else :
		raise Http404

# This is a function and not a view 
# This is used to calculate the net worth of a team and store it in the database
# This function is invoked in almost every view to update the networth of the team
def calculate_net_worth(team): #<done>
	team.net_worth= team.money * money_nw_rate + team.assets * nw_rate_dict['assets'] + team.labour * nw_rate_dict['labour']
	team.save()
	return

############################################# OPTIONAL SEGMENT ######################################################################

'''
# This is a an experiment from my side
# This view is to revert back a mistake if made
# This is done by generating a log and reverting back as and when required
def revert_back(request):
	#<complete>

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
'''