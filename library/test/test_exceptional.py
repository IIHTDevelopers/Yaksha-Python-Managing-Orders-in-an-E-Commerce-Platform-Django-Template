
from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import Order
from django.core.exceptions import ValidationError

class OrderExceptionalTest(TestCase):

    def test_invalid_status_choice(self):
        """Test if assigning an invalid status choice raises an error"""
        test_obj = TestUtils()
        try:
            order = Order(order_number="ORD999", customer_name="Invalid Status", status="InvalidStatus", total_price=50.00)
            order.full_clean()  # This should raise ValidationError
            test_obj.yakshaAssert("TestInvalidStatusChoice", False, "exceptional")
            print("TestInvalidStatusChoice = Failed")
        except ValidationError:
            test_obj.yakshaAssert("TestInvalidStatusChoice", True, "exceptional")
            print("TestInvalidStatusChoice = Passed")
        except:
            test_obj.yakshaAssert("TestInvalidStatusChoice", False, "exceptional")
            print("TestInvalidStatusChoice = Failed")

    def test_duplicate_order_number(self):
        """Test if duplicate order_number raises an IntegrityError"""
        test_obj = TestUtils()
        try:
            Order.objects.create(order_number="DUPL123", customer_name="User1", total_price=200.00)
            Order.objects.create(order_number="DUPL123", customer_name="User2", total_price=150.00)
            test_obj.yakshaAssert("TestDuplicateOrderNumber", False, "exceptional")
            print("TestDuplicateOrderNumber = Failed")
        except IntegrityError as e:
            test_obj.yakshaAssert("TestDuplicateOrderNumber", True, "exceptional")
            print("TestDuplicateOrderNumber = Passed")
        except:
            test_obj.yakshaAssert("TestDuplicateOrderNumber", False, "exceptional")
            print("TestDuplicateOrderNumber = Failed")
            
