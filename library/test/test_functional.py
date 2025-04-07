from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from library.models import Order
from library.test.TestUtils import TestUtils
from django.contrib.admin.sites import site


class OrderFunctionalTest(TestCase):

    def test_create_order(self):
        """Test if an order is created successfully"""
        test_obj = TestUtils()
        try:
            order = Order.objects.create(order_number="ORD123", customer_name="John Doe", status="Pending", total_price=100.50)
            if order:
                test_obj.yakshaAssert("TestCreateOrder", True, "functional")
                print("TestCreateOrder = Passed")
            else:
                test_obj.yakshaAssert("TestCreateOrder", False, "functional")
                print("TestCreateOrder = Failed")
        except:
            test_obj.yakshaAssert("TestCreateOrder", False, "functional")
            print("TestCreateOrder = Failed")

    def test_admin_order_registered(self):
        """Test if Order model is registered in Django Admin"""
        test_obj = TestUtils()
        try:
            is_registered = site.is_registered(Order)
            if is_registered:
                test_obj.yakshaAssert("TestAdminOrderRegistered", True, "functional")
                print("TestAdminOrderRegistered = Passed")
            else:
                test_obj.yakshaAssert("TestAdminOrderRegistered", False, "functional")
                print("TestAdminOrderRegistered = Failed")
        except:
            test_obj.yakshaAssert("TestAdminOrderRegistered", False, "functional")
            print("TestAdminOrderRegistered = Failed")

    def test_order_status_filter(self):
        """Test if admin panel allows filtering by order status"""
        test_obj = TestUtils()
        try:
            admin_class = site._registry.get(Order)
            if admin_class and "status" in admin_class.list_filter:
                test_obj.yakshaAssert("TestOrderStatusFilter", True, "functional")
                print("TestOrderStatusFilter = Passed")
            else:
                test_obj.yakshaAssert("TestOrderStatusFilter", False, "functional")
                print("TestOrderStatusFilter = Failed")
        except:
            test_obj.yakshaAssert("TestOrderStatusFilter", False, "functional")
            print("TestOrderStatusFilter = Failed")
