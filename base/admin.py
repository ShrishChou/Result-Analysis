from django.contrib import admin
from .models import Player, DoublesMatch, SinglesMatch, Duel,Score3set,Score8game
# Register your models here.

admin.site.register(Player)
admin.site.register(DoublesMatch)
admin.site.register(SinglesMatch)
admin.site.register(Duel)
admin.site.register(Score3set)
admin.site.register(Score8game)

