from django.db import models

REGIONS = [
    {'name': 'northern-darfur', 'population': 2113626},
    {'name': 'northern-kordofan', 'population': 2920992},
    {'name': 'northern', 'population': 699065},
    {'name': 'nile', 'population': 1120441},
    {'name': 'western-darfur', 'population': 1308225},
    {'name': 'elgezira', 'population': 3575280},
    {'name': 'khartoum', 'population': 5274321},
    {'name': 'white-nile', 'population': 1730588},
    {'name': 'abyei', 'population': 197681},
    {'name': 'gedaref', 'population': 1348378},
    {'name': 'blue nile', 'population': 832112},
    {'name': 'sennar', 'population': 1285058},
    {'name': 'southern-kordofan', 'population': 1406404},
    {'name': 'kassala', 'population': 1789806},
    {'name': 'red-sea', 'population': 1396110},
    {'name': 'southern-darfur', 'population': 4093594},
]


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    population = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name.capitalize())

# for region in REGIONS:
#     Region.objects.create(**region)
