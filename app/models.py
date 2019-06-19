from django.db import models
from datetime import datetime

# Create your models here.
class RegistModel(models.Model):
    GENDER_CHOICES = (
        (1, '男性'),
        (0, '女性'),
    )

    name = models.CharField('名字', max_length=16)
    birthday = models.DateField('出生年月日')
    gender = models.IntegerField('性别', choices=GENDER_CHOICES)
    age = models.IntegerField('年龄')
    birth_place = models.CharField('籍贯', max_length=64)
    address = models.CharField('家庭住址', max_length=256)

    created = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            'birthday': self.birthday.strftime('%Y/%m/%d'),
            "gender": "男性" if self.gender == '1' else '女性',
            "age": self.age,
            "birth_place": self.birth_place,
            "address": self.address
        }



    class Meta:
        ordering = ('created',)
