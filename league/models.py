from django.db import models
from random import randint

BUDGET = 100
MAX_PLAYERS = 14
AVAILABLE_POSITIONS = (
        ('qb','quarterback'),
        ('rb', 'running back'),
        ('wr', 'wide receiver'),
        ('te', 'tight end'),
        ('k', 'kicker'),
        ('def', 'defense')
    )

# Create your models here.
class League(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def get_random_undraftend(self):
        all_players = self.player_set.all()
        valid_players = []
        for player in all_players:
            if not player.roster:
                valid_players.append(player)
        return valid_players[randint(0, len(valid_players) - 1)]

    def __str__(self):
        return self.name


class Roster(models.Model):
    name = models.CharField(max_length=200)
    budget = models.IntegerField(default=BUDGET)
    league = models.ForeignKey(League)

    def get_bid_stats(self):
        players = self.player_set.all()
        print 'players = %d' % len(players)
        print 'total cost = %d' % sum([i.cost for i in players])
        spent = sum([i.cost for i in players])
        remaining = BUDGET - spent
        max_bid = remaining - (MAX_PLAYERS - len(players))
        return {'spent': spent, 'remaining': remaining, 'max_bid': max_bid}

    def __str__(self):
        return self.name

class Player(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    position = models.CharField(max_length=200, choices=AVAILABLE_POSITIONS)
    bye_week = models.IntegerField()
    league = models.ForeignKey(League)
    roster = models.ForeignKey(Roster, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)

    def is_drafted(self):
        return self.roster is not None

    class Meta:
        ordering = ['number']