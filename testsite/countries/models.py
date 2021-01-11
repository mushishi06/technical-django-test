from django.db import models


class Country(models.Model):
    """Country model."""

    name = models.CharField(max_length=100)
    alpha2Code = models.CharField(max_length=2)
    alpha3Code = models.CharField(max_length=3)
    population = models.IntegerField()
    topLevelDomain = models.CharField(max_length=10)
    capital = models.CharField(max_length=100)

    region = models.ForeignKey(
        "Region",
        on_delete=models.CASCADE,
        related_name="countries",
    )

    def __str__(self):
        return self.name

    @classmethod
    def get_stats_by_region(cls, region_id, region_name=""):
        """Get the Stats by giving Region id."""
        countries = cls.objects.filter(region_id=region_id)
        region = {
            "name": region_name,
            "number_countries": cls.get_number_countries(countries),
            "total_population": cls.get_total_population(countries)
        }
        return region

    @staticmethod
    def get_number_countries(countries):
        """Get the number of countrie in countries."""
        return countries.count() or 0

    @staticmethod
    def get_total_population(countries):
        """Get the Sum of the populations in countries."""
        return countries.aggregate(populations=models.Sum('population'))['populations'] or 0


class Region(models.Model):
    """Region model."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def get_stats(cls):
        """Get the stats of all the Regions."""
        data = []
        regions = cls.objects.all()
        for region in regions:
            data.append(Country.get_stats_by_region(region.id, region.name))
        return data
