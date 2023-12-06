from django.http import JsonResponse, HttpRequest

from third_party.convertor import get_data


def index(request):
    return JsonResponse({'hello': 'world!'})


def lessons(request: HttpRequest, group=None):
    context = get_data()

    if group is not None:
        context = context[group]

    return JsonResponse(context)
