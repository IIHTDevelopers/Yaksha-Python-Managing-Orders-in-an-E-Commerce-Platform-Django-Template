from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from library.models import Order
from django.urls import reverse
from django.test import TestCase


class OrderBoundaryTest(TestCase):

    def test_min_price_value(self):
        """Test if total_price accepts minimum allowed value"""
        test_obj = TestUtils()
        try:
            order = Order.objects.create(order_number="MINPRICE", customer_name="Alice", total_price=0.01)
            if order.total_price >= 0.01:
                test_obj.yakshaAssert("TestMinPriceValue", True, "boundary")
                print("TestMinPriceValue = Passed")
            else:
                test_obj.yakshaAssert("TestMinPriceValue", False, "boundary")
                print("TestMinPriceValue = Failed")
        except:
            test_obj.yakshaAssert("TestMinPriceValue", False, "boundary")
            print("TestMinPriceValue = Failed")