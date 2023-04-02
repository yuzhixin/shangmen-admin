
import requests
from shangmen.models import HomeBar, ShopInfo, Shangpin
from django.http import JsonResponse
from shangmen_admin.settings import MEDIA_HOSTS, AppID, AppSecret


def home_info(request):
    homeBar = HomeBar.objects.all()
    ret = []
    for home in homeBar:
        ret.append({
            "src": MEDIA_HOSTS + home.src.name,
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
    query = request.GET.get("query", "")
    if query:
        shangpins = Shangpin.objects.filter(
            isPublish=1).filter(title__icontains=query)
    else:
        shangpins = Shangpin.objects.filter(isPublish=1)
    ret = []
    for shangpin in shangpins:
        ret.append({
            "id": shangpin.id,
            "src": MEDIA_HOSTS + shangpin.src.name,
            "title": shangpin.title,
            "view_price": shangpin.view_price,
            "real_price": shangpin.real_price,
            "tag": shangpin.get_tag_name(),
            "sumery": shangpin.sumery,
        })
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})


def code_to_session(request):
    jscode = request.GET.get("code", "")
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(AppID, AppSecret, jscode)
    data = requests.get(url)
    return JsonResponse({'code': 0, 'ret': data.json(), 'msg': ''})