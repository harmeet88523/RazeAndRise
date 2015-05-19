#<complete> explain the schema of the database

####################################################### IMPORT STATTEMENTS ############################################################

from django.db import models

####################################################### GLOBAL VARIABLES   ############################################################

power_category_choices=(
	('attack','Attack'),
	('defense','Defense'),
	)

commodity_choices=(
	('money','Money'),
	('assets','Assets'),
	('labour','Labour'),
	)

########################################################## MODELS #####################################################################

# Create your models here.

class Team(models.Model):
	no=models.PositiveSmallIntegerField(unique=True)
	name=models.CharField(max_length=200)
	money=models.PositiveIntegerField(default=0)
	assets=models.PositiveIntegerField(default=0)
	labour=models.PositiveIntegerField(default=0)
	net_worth=models.PositiveIntegerField(default=0)
	# qs=models.ManyToManyField('Question') #<optional> addonly if question wala thing is to be incorporated
	# aqs=models.ManyToManyField('Question') #<optional> addonly if question wala thing is to be incorporated
	powers=models.ManyToManyField('Power')
	cash_generated=models.PositiveIntegerField() # thsi store teh cash generated in the current round
	is_eliminated = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name + ' ' + self.member_set.filter(team_leader=True)[0].name

class Participant(models.Model):
	team=models.ForeignKey('Team')
	name=models.CharField(max_length=200)
	email=models.EmailField()
	phone=models.PositiveIntegerField()
	college=models.CharField(max_length=200)
	team_leader=models.BooleanField(default=False)

	def __unicode__(self):
		return self.name + ' ' + self.team.name

class Power(models.Model):
	category=models.CharField(max_length=8,choices=power_category_choices)
	commodity=models.CharField(max_length=6,choices=commodity_choices)
	price=models.PositiveIntegerField()
	strength=models.PositiveIntegerField()
	quantity=models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.category + ' ' + unicode(self.price) + ' - ' + unicode(self.quantity) + ' left'

######################################################## OPTIONAL SEGMENT ##################################################################

'''class Question(models.Model):
	#<optional> complete only if the question wala thing is to be incorporated
	#<complete>
	'''