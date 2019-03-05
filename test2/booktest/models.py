from django.db import models

# Create your models here.
# ����ͼ��ģ����BookInfo

class BookInfoManager(models.Manager):

    def all(self):
        # Ĭ�ϲ�ѯδɾ����ͼ����Ϣ
        # ���ø���ĳ�Ա�﷨Ϊ��super().������
        return super().all().filter(isDelete=False)

    # ����ģ���࣬���ղ���Ϊ���Ը�ֵ
    def create_book(self, title, pub_date):
        # ����ģ�������self.model���Ի��ģ����
        book = self.model()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = 0
        book.bcommet = 0
        book.isDelete = False
        # �����ݲ�������ݱ�
        book.save()
        return book

class BookInfo(models.Model):
    books = BookInfoManager()
    # ͼ������
    btitle = models.CharField(max_length=20)
    # ��������
    bpub_data = models.DateField()
    # �Ķ���
    bread = models.IntegerField(default=0)
    # ������
    bcomment = models.IntegerField(default=0)
    # �߼�ɾ��
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "BookInfo"

# ����Ӣ��ģ����HeroInfo
class HeroInfo(models.Model):
    # Ӣ������
    hname = models.CharField(max_length=10)
    # Ӣ���Ա�
    hgender = models.BooleanField(default=False)
    # �߼�ɾ��
    isDelete = models.BooleanField(default=False)
    # Ӣ��������Ϣ
    hcommment = models.CharField(max_length=200)
    # Ӣ����ͼ���Ĺ�ϵΪһ�Զ࣬�������Զ�����Ӣ��ģ������
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'HeroInfo'


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)
    aParent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'AreaInfo'