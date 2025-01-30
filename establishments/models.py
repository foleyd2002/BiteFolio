from django.db import models

class Establishment(models.Model):
    name = models.CharField(max_length=255)
    town = models.CharField(max_length=255)  # Replacing 'location' with 'town'

    COUNTIES = [
    ('Antrim', 'Antrim'),
    ('Armagh', 'Armagh'),
    ('Carlow', 'Carlow'),
    ('Cavan', 'Cavan'),
    ('Clare', 'Clare'),
    ('Cork', 'Cork'),
    ('Derry', 'Derry'),
    ('Donegal', 'Donegal'),
    ('Down', 'Down'),
    ('Dublin', 'Dublin'),
    ('Fermanagh', 'Fermanagh'),
    ('Galway', 'Galway'),
    ('Kerry', 'Kerry'),
    ('Kildare', 'Kildare'),
    ('Kilkenny', 'Kilkenny'),
    ('Laois', 'Laois'),
    ('Leitrim', 'Leitrim'),
    ('Limerick', 'Limerick'),
    ('Longford', 'Longford'),
    ('Louth', 'Louth'),
    ('Mayo', 'Mayo'),
    ('Meath', 'Meath'),
    ('Monaghan', 'Monaghan'),
    ('Offaly', 'Offaly'),
    ('Roscommon', 'Roscommon'),
    ('Sligo', 'Sligo'),
    ('Tipperary', 'Tipperary'),
    ('Tyrone', 'Tyrone'),
    ('Waterford', 'Waterford'),
    ('Westmeath', 'Westmeath'),
    ('Wexford', 'Wexford'),
    ('Wicklow', 'Wicklow'),
    ]

    county = models.CharField(max_length=255, choices=COUNTIES, default='Dublin',)
    type = models.CharField(max_length=100, choices=[('Food', 'Food'), ('Drink', 'Drink')])
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    visited_at = models.DateField()

    def __str__(self):
        return self.name