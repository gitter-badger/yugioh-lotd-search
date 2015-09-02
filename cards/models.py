from django.db import models
from cardsources.models import Deck,Booster

class CardType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Card(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(help_text='The card text (can include flavour text)')

    card_types = models.ManyToManyField(CardType)
    limitation = models.IntegerField(default=3)
    database_id = models.IntegerField(unique=True, help_text='The Yugioh-Card database id')

    image_url = models.URLField(max_length=200)

    decks = models.ManyToManyField(Deck)
    boosters = models.ManyToManyField(Booster)

    # Monster card specific
    attribute = models.CharField(
        max_length = 2,
        choices = (
            ('dk', 'DARK'),
            ('dv', 'DIVINE'),
            ('ea', 'EARTH'),
            ('fr', 'FIRE'),
            ('lt', 'LIGHT'),
            ('wt', 'WATER'),
            ('wn', 'WIND'),
        ),
    )
    level = models.IntegerField(null=True)
    stars = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)

    # Spell card specific
    effect_type = models.CharField(
        max_length = 4,
        choices = (
            ('con', 'Continuous Spell'),
            ('fld', 'Field Spell'),
            ('eq', 'Equip Spell'),
            ('qp', 'Quick-Play Spell'),
            ('rit', 'Ritual Spell'),
            ('coun', 'Counter Spell'),
            ('cnt', 'Counter Trap'),
            ('cont', 'Continuous Trap'),
            ('nt', 'Normal Trap')
        )
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
