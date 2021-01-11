from django.http import JsonResponse

from .models import Region


def stats(request):
    """Provide name, number_countries and total_population for each region."""
    response = {"regions": Region.get_stats()}

    return JsonResponse(response)
