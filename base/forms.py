from django.forms import ModelForm
from django.forms import modelformset_factory, inlineformset_factory,BaseInlineFormSet
from .models import SinglesMatch,DoublesMatch,Duel


class DuelForm(ModelForm):
    class Meta:
        model = Duel
        fields = "__all__"  # Add other duel fields as needed

class SinglesMatchForm(ModelForm):
    class Meta:
        model = SinglesMatch
        fields = "__all__"  # Add other singles match fields as needed

class DoublesMatchForm(ModelForm):
    class Meta:
        model = DoublesMatch
        fields = "__all__"   # Add other doubles match fields as needed

SinglesMatchInlineFormSet = inlineformset_factory(Duel, SinglesMatch, form=SinglesMatchForm, extra=6, fk_name='duel')
DoublesMatchInlineFormSet = inlineformset_factory(Duel, DoublesMatch, form=DoublesMatchForm, extra=3, fk_name='duel')

SinglesMatchInlineForm = inlineformset_factory(Duel, SinglesMatch, form=SinglesMatchForm, extra=1, fk_name='duel')
DoublesMatchInlineForm = inlineformset_factory(Duel, DoublesMatch, form=DoublesMatchForm, extra=1, fk_name='duel')