from django.contrib import admin
from .models import HomeBar, ShopInfo, Shangpin, LoginUser, LoginUserAddress


class LoginUserAddressAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'mobile', 'address')

    search_fields = ('id', 'name', 'mobile', 'address')

    ordering = ('-id',)

class HomeBarAdmin(admin.ModelAdmin):

    # 列表页，列表顶部显示的字段名称
    list_display = ('id', 'src')

    # 列表页出现搜索框，参数是搜索的域
    search_fields = ('id', 'src')

    # 右侧会出现过滤器，根据字段类型，过滤器显示过滤选项
    # list_filter = ('publication_date',)

    # 页面中的列表顶端会有一个逐层深入的导航条，逐步迭代选项
    # date_hierarchy = 'date'

    # 自然是排序所用了，减号代表降序排列
    ordering = ('-id',)


class ShopInfoAdmin(admin.ModelAdmin):

    # 列表页，列表顶部显示的字段名称
    list_display = ('mobile', 'weixin')


class ShangpinAdmin(admin.ModelAdmin):

    # 列表页，列表顶部显示的字段名称
    list_display = ('id', 'title', 'view_price',
                    'real_price', 'tag', 'isPublish')

    # 列表页出现搜索框，参数是搜索的域
    search_fields = ('title', 'tag', 'isPublish')

    # 自然是排序所用了，减号代表降序排列
    ordering = ('-id',)


admin.site.register(HomeBar, HomeBarAdmin)
admin.site.register(ShopInfo, ShopInfoAdmin)
admin.site.register(Shangpin, ShangpinAdmin)
admin.site.register(LoginUser)
admin.site.register(LoginUserAddress, LoginUserAddressAdmin)
