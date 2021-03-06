from django import forms
from django.forms.models import inlineformset_factory, BaseFormSet
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
	username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
	password1 = forms.CharField(label=_("Password"),
		widget=forms.PasswordInput)
	password2 = forms.CharField(label=_("Password confirmation"),
		widget=forms.PasswordInput,
		help_text=_("Enter the same password as above, for verification."))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class AddTeamForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(AddTeamForm, self).__init__(*args, **kwargs)
		self.fields['coach'].queryset = User.objects.filter(username=user)

	class Meta:
		model = Team

class AddSeasonForm(forms.ModelForm):
	class Meta:
		model = Season

	def __init__(self, *args, **kwargs):
		coach = kwargs.pop('coach')
		super(AddSeasonForm, self).__init__(*args, **kwargs)
		self.fields['team'].queryset=Team.objects.filter(coach=coach)

class SeasonForm(forms.ModelForm):
	class Meta:
		model = Season
		fields = ('year',)

class PositionForm(forms.ModelForm):
	class Meta:
		model = DepthChart

class AddGameForm(forms.ModelForm):
	class Meta:
		model = Game

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Player
		fields = ('team', 'season', 'first_name', 'last_name', 'position', 'class_standing', 'throws', 'hits')

class HitStatsForm(forms.ModelForm):
	class Meta:
		model = HitterStats
		fields = ('game','player','at_bats', 'runs', 'hits', 'doubles', 'triples', 'hr', 'rbi', 'walks', 'hbp', 'sacrafice', 'strikeouts')


class PitchStatsForm(forms.ModelForm):
	class Meta:
		model = PitcherStats
		fields = ('game','player','starting_pitcher', 'full_innings', 'part_innings', 'hits_allowed', 'runs_allowed', 'earned_runs', 'walks_allowed', 'strikeout_amount', 'wild_pitches', 'hit_by_pitch', 'win', 'loss', 'sv')
