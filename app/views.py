from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from app.models import RegistModel


def allow_all(response):
    """
    解决跨域的问题
    :param response:
    :return:
    """
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        birth_place = request.POST.get("birth_place")
        birthday = request.POST.get("birthday")
        address = request.POST.get("address")

        try:
            new_regist = RegistModel(
                name=name,
                age=age,
                gender=gender,
                birthday=birthday,
                birth_place=birth_place,
                address=address
            )
            new_regist.save()
            response = JsonResponse({'is_error':False, 'msg':'OK', 'data':new_regist.to_json()})
        except Exception as e:
            print(e)
            response = JsonResponse({'is_error': True, 'msg': e, 'data': {}})

        return allow_all(response)


    name = request.GET.get("name")
    id = request.GET.get("id")
    res = None
    if id:
        res = RegistModel.objects.filter(id=id).all()
    elif name:
        res = RegistModel.objects.filter(name=name).all()

    if res:
        response = JsonResponse({
            'is_error': False,
            'msg': 'OK',
            'data': [i.to_json() for i in res]
        })
    else:
        if id or name:
            response = JsonResponse({
                'is_error': False,
                'msg': "没有数据",
                'data': [],
            })
        else:
            response = JsonResponse({
                'is_error': True,
                'msg': "缺少参数",
                'data': [],
            })
    return allow_all(response)