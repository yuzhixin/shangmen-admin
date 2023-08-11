
from django.views.decorators.csrf import csrf_exempt
from shangmen_admin.settings import MEDIA_HOSTS, AppID, AppSecret
from django.http import JsonResponse, HttpResponse
from shangmen.models import HomeBar, ShopInfo, Shangpin, LoginUser, LoginUserAddress, Order
import requests
import json


def yanzheng(request):
    return HttpResponse("570914c873eaf12ffca0b0e5c5222d14")


def check_login(fn):
    def wrapper(request):
        openid = request.META.get("HTTP_OPENID")
        if openid:
            loginUser = LoginUser.objects.filter(openid=openid).first()
            if not loginUser:
                return JsonResponse({'code': 401, 'msg': '用户未登录'})
            request.session['user'] = str(loginUser.id)
            return fn(request)
        else:
            return JsonResponse({'code': 401, 'msg': '用户未登录'})
    return wrapper


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
    if jscode == "":
        return JsonResponse({'code': -1, 'ret': "获取code", 'msg': ''})
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(
        AppID, AppSecret, jscode)
    data = requests.get(url)
    return JsonResponse({'code': 0, 'ret': data.json(), 'msg': ''})


def login(request):
    openid = request.GET.get("openid", "")
    if openid == "":
        return JsonResponse({'code': -1, 'ret': "获取用户异常", 'msg': ''})
    loginUser = LoginUser.objects.filter(openid=openid).first()
    if not loginUser:
        loginUser = LoginUser.objects.create(openid=openid)
    ret = {
        "openid": loginUser.openid,
        "nickName": loginUser.openid,
        # "avatarUrl": loginUser.avatarUrl,
    }
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})


@csrf_exempt
def update_current_user(request):
    userInfo = json.loads(request.body)
    if userInfo.get("openid", "") == "":
        return JsonResponse({'code': -1, 'ret': "获取用户异常", 'msg': '获取用户异常'})
    loginUser = LoginUser.objects.filter(
        openid=userInfo.get("openid", "")).first()
    if not loginUser:
        return JsonResponse({'code': -1, 'ret': "获取用户异常", 'msg': '获取用户异常'})
    loginUser.nickName = userInfo.get("nickName", "")
    loginUser.avatarUrl = userInfo.get("avatarUrl", "")
    loginUser.save()
    return JsonResponse({'code': 0, 'ret': {}, 'msg': ''})


@check_login
def current_user(request):
    loginUser = LoginUser.objects.filter(id=request.session['user']).first()
    ret = {
        "openid": loginUser.openid,
        "nickName": loginUser.nickName,
        "avatarUrl": loginUser.avatarUrl,
    }
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})


@check_login
def address_list(request):
    loginUser = LoginUser.objects.filter(id=request.session['user']).first()
    addresList = LoginUserAddress.objects.filter(loginUser=loginUser.id)
    ret = []
    for addres in addresList:
        ret.append({
            "id": addres.id,
            "name": addres.name,
            "mobile": addres.mobile,
            "address": addres.address,
            "isDefault": addres.isDefault,
        })
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})


@check_login
def default_address(request):
    loginUser = LoginUser.objects.filter(id=request.session['user']).first()
    addres = LoginUserAddress.objects.filter(
        loginUser=loginUser.id).filter(isDefault=True).first()
    if addres:
        ret = {
            "id": addres.id,
            "name": addres.name,
            "mobile": addres.mobile,
            "address": addres.address,
            "isDefault": addres.isDefault,
        }
    else:
        ret = {}
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})


@check_login
def set_default_address(request):
    loginUser = LoginUser.objects.filter(id=request.session['user']).first()
    addressId = request.GET.get("addressId", "")
    LoginUserAddress.objects.filter(
        loginUser=loginUser.id).update(isDefault=False)
    LoginUserAddress.objects.filter(loginUser=loginUser.id).filter(
        id=addressId).update(isDefault=True)
    return JsonResponse({'code': 0, 'ret': {}, 'msg': ''})


@csrf_exempt
@check_login
def add_address(request):
    loginUser = LoginUser.objects.filter(id=request.session['user']).first()
    data = json.loads(request.body)
    LoginUserAddress.objects.filter(
        loginUser=loginUser.id).update(isDefault=False)
    addres = LoginUserAddress.objects.create(
        loginUser=loginUser.id,
        name=data.get('name'),
        mobile=data.get('mobile'),
        address=data.get('address'),
        isDefault=True,
    )
    ret = {
        "id": addres.id,
        "name": addres.name,
        "mobile": addres.mobile,
        "address": addres.address,
        "isDefault": addres.isDefault,
    }
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})


@csrf_exempt
@check_login
def update_address(request):
    loginUser = LoginUser.objects.filter(id=request.session['user']).first()
    data = json.loads(request.body)
    LoginUserAddress.objects.filter(loginUser=loginUser.id).filter(
        id=data.id).update(
        isDefault=data.isDefault,
        name=data.name,
        mobile=data.mobile,
        address=data.address
    )
    return JsonResponse({'code': 0, 'ret': {}, 'msg': ''})


@csrf_exempt
@check_login
def create_order(request):
    loginUser = LoginUser.objects.filter(id=request.session['user']).first()
    data = json.loads(request.body)
    address_id = data['address_id']
    product_id = data['product_id']
    shangmenInfo = data['shangmenInfo']
    appointTime = data['appointTime']
    product = Shangpin.objects.filter(id=product_id).first()
    address = LoginUserAddress.objects.filter(id=address_id).first()
    appoint_time = appointTime.split('(')[0] + " " + appointTime.split(')')[1]
    order = Order(loginUser=loginUser.id, shangpin=product.id, title=product.title, real_price=product.real_price, fuwu_name=address.name, fuwu_mobile=address.mobile,
                  fuwu_address=address.address, yuyue_name=shangmenInfo['name'], yuyue_mobile=shangmenInfo['phone'], yuyue_note=shangmenInfo.get('note', ''), appoint_time=appoint_time)
    order.save()
    return JsonResponse({'code': 0, 'ret': {'order': order.id}, 'msg': ''})


@check_login
def order_list(request):
    isWanCheng = request.GET.get("isWanCheng")
    loginUser = LoginUser.objects.filter(id=request.session['user']).first()
    orders = Order.objects.filter(loginUser=loginUser.id).order_by('-id')
    if isWanCheng:
        orders = orders.filter(isWanCheng=1)
    ret = []
    for order in orders:
        ret.append({
            "shangpin": order.shangpin,
            "title": order.title,
            "real_price": order.real_price,
            "isPay": order.isPay,
            "isWanCheng": order.isWanCheng,
            "appoint_time": order.appoint_time,
            "created_at": order.created_at,
        })
    return JsonResponse({'code': 0, 'ret': ret, 'msg': ''})
