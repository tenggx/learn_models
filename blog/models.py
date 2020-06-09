from django.db import models

# Create your models here.
from django.db.models import Model


class Article(models.Model):
    # 文章唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    tile = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章内容
    content = models.TextField()
    # 发布日期
    publish_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.tile
