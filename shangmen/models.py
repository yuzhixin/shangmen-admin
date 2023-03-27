
from shangmen_admin.settings import HOSTS
from django.db import models
from ckeditor.fields import RichTextField


class HomeBar(models.Model):
    id = models.AutoField(primary_key=True)
    src = models.ImageField(verbose_name='首页轮播图', null=True,
                            blank=True, upload_to='image', max_length=200)

    def __str__(self):
        return self.src

    def src_url(self):
        if self.src and hasattr(self.src, 'url'):
            return HOSTS + self.src.url
        else:
            return HOSTS + '/media/default/user.jpg'

class ShopInfo(models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=128)
    weixin = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    sumery = RichTextField()