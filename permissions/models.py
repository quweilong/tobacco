from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """为模型类补充字段"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        # 说明是抽象模型类, 用于继承使用，数据库迁移时不会创建BaseModel的表
        abstract = True

class PermissionsManagement(BaseModel):
    permissions_id = models.IntegerField()
    parent_permissions_id = models.IntegerField()
    permissions_name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)



