
from shangmen_admin.settings import HOSTS
from django.db import models
from ckeditor.fields import RichTextField


class LoginUser(models.Model):
    id = models.AutoField(primary_key=True)
    openid = models.CharField(
        max_length=128, default="", verbose_name="openid")
    nickName = models.CharField(max_length=128, default="", verbose_name="昵称")
    avatarUrl = models.CharField(max_length=512, default="", verbose_name="头像")
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['openid'])]
        verbose_name_plural = '注册用户'


class LoginUserAddress(models.Model):
    id = models.AutoField(primary_key=True)
    loginUser = models.IntegerField(default=0, verbose_name="登录用户")
    name = models.CharField(max_length=128, verbose_name="姓名")
    mobile = models.CharField(max_length=128, verbose_name="手机号")
    address = models.CharField(max_length=512, verbose_name="地址")
    isDefault = models.BooleanField(default=False, verbose_name="是否默认地址")
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '用户地址'


class HomeBar(models.Model):
    id = models.AutoField(primary_key=True)
    src = models.ImageField(verbose_name='首页轮播图',
                            upload_to='image', max_length=200)

    class Meta:
        verbose_name_plural = '首页轮播图'

    def src_url(self):
        if self.src and hasattr(self.src, 'url'):
            return HOSTS + self.src.url
        else:
            return HOSTS + '/media/default/user.jpg'


class ShopInfo(models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=128, verbose_name="手机号")
    weixin = models.CharField(max_length=128, verbose_name="微信")
    address = models.CharField(max_length=256, verbose_name="地址")
    sumery = RichTextField(verbose_name="商店简介")
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '店铺信息'


class Shangpin(models.Model):
    TAG = [
        ('ms', '秒杀'),
        ('yh', '优惠'),
        ('cx', '促销'),
    ]

    PUBLISH = [
        (1, '发布'),
        (0, '未发布'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, verbose_name="标题")
    src = models.ImageField(verbose_name='头图',
                            upload_to='image', max_length=200)
    view_price = models.DecimalField(
        verbose_name="对比价格", max_digits=5, decimal_places=2, blank=False, null=False)
    real_price = models.DecimalField(
        verbose_name="真实价格",  max_digits=5, decimal_places=2, blank=False, null=False)
    tag = models.CharField(max_length=128, verbose_name="标签", choices=TAG)
    sumery = RichTextField(verbose_name="商品介绍")
    isPublish = models.IntegerField(choices=PUBLISH)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '商品详情'

    def get_tag_name(self):
        return self.get_tag_display()


class Order(models.Model):
    PAY = [
        (1, '已支付'),
        (0, '未支付'),
    ]

    WC = [
        (1, '已完成'),
        (0, '未完成'),
    ]

    id = models.AutoField(primary_key=True)
    loginUser = models.IntegerField(default=0, verbose_name="登录用户")
    shangpin = models.IntegerField(default=0, verbose_name="商品")
    title = models.CharField(max_length=128, verbose_name="标题", default="")
    src = models.CharField(max_length=128, verbose_name="图片", default="")
    sumery = RichTextField(verbose_name="商品介绍", default='')
    real_price = models.DecimalField(
        verbose_name="真实价格",  max_digits=5, decimal_places=2, blank=False, null=False)
    isPay = models.IntegerField(default=0, choices=PAY)
    isWanCheng = models.IntegerField(default=0, choices=WC)
    fuwu_name = models.CharField(
        max_length=128, verbose_name="上门服务姓名", default="")
    fuwu_mobile = models.CharField(
        max_length=128, verbose_name="上门服务手机号", default="")
    fuwu_address = models.CharField(
        max_length=512, verbose_name="上门服务地址", default="")
    yuyue_name = models.CharField(
        max_length=128, verbose_name="预约人姓名", default="")
    yuyue_mobile = models.CharField(
        max_length=128, verbose_name="预约人手机号", default="")
    yuyue_note = models.CharField(
        max_length=512, verbose_name="预约备注", default="")
    appoint_time = models.CharField(
        max_length=128, verbose_name="上门时间", default="")
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '订单详情'


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=128, verbose_name="标题", default="")
    content = models.CharField(
        max_length=512, verbose_name="内容", default="")
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '通知'
