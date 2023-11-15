from django.test import TestCase
from app.views import front_times, no_teen_sum, xyz_there, centered_average

# Create your tests here.


class Test_views_functions(TestCase):
    # Chocolate, 2
    def test_font_times_chocolate_2(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&times=2")
        self.assertContains(response, "ChoCho")

    # Chocolate, 3
    def test_font_times_chocolate_3(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&times=3")
        self.assertContains(response, "ChoChoCho")

    # Abc, 3
    def test_font_times_Abc_3(self):
        response = self.client.get("/warmup-2/font-times/?word=Abc&times=3")
        self.assertContains(response, "AbcAbcAbc")

    # 1, 2, 3
    def test_no_teen_sum_1_2_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=1&b=2&c=3")
        self.assertContains(response, "6")

    # 2, 13, 1
    def test_no_teen_sum_2_13_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=13&c=1")
        self.assertContains(response, "3")

    # 2, 1, 14
    def test_no_teen_sum_2_1_14(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=1&c=14")
        self.assertContains(response, "3")

    # "abcxyz"
    def test_xyz_there_abcxyz(self):
        response = self.client.get("/string-2/xyz-there/?word=abcxyz")
        self.assertContains(response, "True")

    # "abc.xyz"
    def test_xyz_there_abcdotxyz(self):
        response = self.client.get("/string-2/xyz-there/?word=abc.xyz")
        self.assertContains(response, "False")

    # "xyz.abc"
    def test_xyz_there_xyzdotabc(self):
        response = self.client.get("/string-2/xyz-there/?word=xyz.abc")
        self.assertContains(response, "True")

    # centered_average([1, 2, 3, 4, 100])
    def test_centered_average_1_2_3_4_100(self):
        response = self.client.get(
            "/list-2/centered-average/?a=1&b=2&c=3&d=4&e=100&f=&g="
        )
        self.assertContains(response, "3")

    # centered_average([1, 1, 5, 5, 10, 8, 7])
    def test_centered_average_1_1_5_10_8_7(self):
        response = self.client.get(
            "/list-2/centered-average/?a=1&b=1&c=5&d=5&e=10&f=8&g=7"
        )
        self.assertContains(response, "5")

    # centered_average([-10, -4, -2, -4, -2, 0])
    def test_centered_average_10_4_2_4_2_0(self):
        response = self.client.get(
            "/list-2/centered-average/?a=-10&b=-4&c=-2&d=-4&e=-2&f=0&g="
        )
        self.assertContains(response, "-3")
