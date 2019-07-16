from django.core.cache import cache

from django.http import JsonResponse


def latest_block(request):
    return JsonResponse(cache.get('latest_block'))
