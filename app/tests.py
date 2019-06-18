from django.test import TestCase

# Create your tests here.
from app.models import RegistModel

class RegistModelTests(TestCase):

    def setUp(self):
        print("=======RegistModelTests =======")
        self.name ="小张"
        self.age = '12'
        self.gender = '1'
        self.birth_place = '广东'
        self.birthday = '2018-06-10'
        self.address = "我的家庭地址"

    def test_add_user(self):
        new_regist = RegistModel(
            name=self.name,
            age=self.age,
            gender=self.gender,
            birthday=self.birthday,
            birth_place=self.birth_place,
            address=self.address
        )

        new_regist.save()
        self.assertEqual(new_regist.name, self.name)

    def test_find_regist(self):
        new_regist = RegistModel(
            name=self.name,
            age=self.age,
            gender=self.gender,
            birthday=self.birthday,
            birth_place=self.birth_place,
            address=self.address
        )

        new_regist.save()

        res = self.client.get('/register?name=%s' % self.name)

        self.assertEqual(200, res.status_code)

        res = res.json()
        print(res)
        self.assertEqual(self.name, res['data'][0]['name'])

        res = self.client.get('/register?id=%s' % new_regist.id)

        self.assertEqual(200, res.status_code)

        res = res.json()

        self.assertEqual(self.name, res['data'][0]['name'])


    def add_new_regist(self):
        res = self.client.post(
            '/register/',
            {
                'name': self.name,
                'age': self.age,
                'gender': self.gender,
                'birthday': self.birthday,
                'birth_place': self.birth_place,
                'address': self.address
            }
        )

        self.assertEqual(200, res.status_code)

        self.assertEqual(1, RegistModel.objects.filter(name=self.name).count())