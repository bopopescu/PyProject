from django.db import models

# Create your models here.
class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)

    class Meta:
        db_table = 'TypeInfo'

class NewsInfo(models.Model):
    ntitle = models.CharField(max_length=60)  # ���ű���
    ncontent = models.TextField()  # ��������
    npub_date = models.DateTimeField(auto_now_add=True)
    # ���ŷ���ʱ��
    ntype = models.ManyToManyField('TypeInfo')
    # ͨ��ManyToManyField����TypeInfo���NewsInfo��֮���Զ�Ĺ�ϵ

    class Meta:
        db_table = 'NewsInfo'