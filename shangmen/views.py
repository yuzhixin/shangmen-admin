from django.shortcuts import render

# Create your views here.

from shangmen.models import HomeBar, ShopInfo, Shangpin
from django.http import JsonResponse


def home_info(request):
    homeBar = HomeBar.objects.all()
    ret = []
    for home in homeBar:
        ret.append({
            "src": home.src.name,
            "content": "",
        })
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})


def shop_info(request):
    shop = ShopInfo.objects.first()
    ret = {
        "mobile": shop.mobile,
        "weixin": shop.weixin,
        "address": shop.address,
        "sumery": shop.sumery,
    }
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})


def shangpin_list(request):
    shangpins = Shangpin.objects.all()
    ret = []
    for shangpin in shangpins:
        ret.append({
            "id": shangpin.id,
            "src": shangpin.src.name,
            "title": shangpin.title,
            "view_price": shangpin.view_price,
            "real_price": shangpin.real_price,
            "tag": shangpin.tag,
            "sumery": shangpin.sumery,
        })
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})
