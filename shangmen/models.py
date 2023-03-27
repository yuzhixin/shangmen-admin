
import os
from django.db import models


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.name, instance.identity_card, ext)
    return os.path.join(instance.major.name, filename) # 系统路径分隔符差异，增强代码重用性


class HomeBar(models.Model):
    id = models.AutoField(primary_key=True)
    src = models.ImageField('照片', upload_to = user_directory_path, blank=False, null=False)

    def __str__(self):
        return self.src

    def src_url(self):
        if self.src and hasattr(self.src, 'url'):
            return self.src.url
        else:
            return '/media/default/user.jpg'