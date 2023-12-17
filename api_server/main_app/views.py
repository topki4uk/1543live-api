from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from third_party.convertor import get_data


def index(request):
    return JsonResponse({'hello': 'world!'})


@csrf_exempt
def lessons(request: HttpRequest, group=None):
    context = {}

    if request.method == 'POST':
        if request.POST is not None:
            data = request.POST.get('html')
            context = get_data(data)

    if group is not None:
        context = context[group]

    return JsonResponse(context)
