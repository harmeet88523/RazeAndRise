from django.db import models

power_category_choices=(
	('Atk','Attack'),
	('Def','Defense'),
)
# Create your models here.
class Team(models.Model):
	no=models.PositiveSmallIntegerField()
	name=models.CharField(max_length=200)
	money=models.PositiveIntegerField(default=0)
	assets=models.PositiveIntegerField(default=0)
	labour=models.PositiveIntegerField(default=0)
	qs=models.ManyToManyField('Question')
	aqs=models.ManyToManyField('Question')
	powers=models.ManyToManyField('Power')

	def __unicode__(self):
		return self.name + ' ' + self.member_set.filter(team_leader=True)[0].name

class Member(models.Model):
	team=models.ForeignKey('Team')
	name=models.CharField(max_length=200)
	email=models.EmailField()
	phone=models.PositiveIntegerField()
	college=models.CharField(max_length=200)
	team_leader=models.BooleanField(default=False)

	def __unicode__(self):
		return self.name + ' ' + self.team.name

class Power(models.Model):
	category=models.CharField(max_length=3,choices=power_category_choices)
	price=models.PositiveIntegerField()
	strength=models.PositiveIntegerField()
	quantity=models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.category + ' ' + unicode(self.price) + ' - ' + unicode(self.quantity) + ' left'