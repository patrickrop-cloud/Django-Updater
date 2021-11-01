from django.test import TestCase
from updateme.views import new_business
from .models import Business,NeighbourHood,User,Admin

# Create your tests here.

class userTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user0=User(name='patrick',email='patrick@gmail.com',id=1)

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.user0,User))

    def test_save_user(self):
        self.user0.save_user()
        userp=User.objects.all()
        self.assertTrue(len(userp)>0)

    def test_delete_user(self):
        self.user0.save_user()
        user_record=User.objects.all()
        self.user0.delete_user()
        self.assertTrue(len(user_record)==0)


class AdminTestClass(TestCase):
    #setup method
    def setUp(self):
        self.admin=Admin(name='patrick')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.admin,Admin))

    def test_save_admin(self):
        self.admin.save_admin()
        admin_p=Admin.objects.all()
        self.assertTrue(len(admin_p)>0)

    def test_delete_admin(self):
        self.admin.save_admin()
        admin_record=Admin.objects.all()
        self.admin.delete_admin()
        self.assertTrue(len(admin_record)==0)


class BusinessTestClass(TestCase):
    #setup method
    def setUp(self):
        self.business=Business(name='coffee',email="coffee@gmail.com")

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_create_business(self):
        self.business.create_business()
        business1=Business.objects.all()
        self.assertIsNotNone(business1)

    def test_delete_business(self):
        self.business.create_business()
        business_record=Business.objects.all()
        self.business.delete_business()
        self.assertTrue(len(business_record)==0)

    def test_find_business(self):
        business=Business.objects.all()
        search_term='coffee'
        db_term=search_term
        if db_term !=search_term:
            return('no match')

        else:
            return(search_term) 

    def test_update_business(self):
        business=Business.objects.all()
        new_biz=Business.update_business(self)
        expected_business=f'{new_biz}'
        self.assertTrue(expected_business,'new_biz')

class NeighbourhoodTestClass(TestCase):
    #setup method
    def setUp(self):
        self.neighbourhood=NeighbourHood(name='car sales',location="kanairo")

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,NeighbourHood))

    def test_create_neighbourhood(self):
        new_neighbourhood=NeighbourHood.create_neighbourhood(self)
        neighbourhood1=f'{new_neighbourhood}'
        self.assertTrue(neighbourhood1,'new_neighbourhood')

    # def test_delete_neighbourhood(self):
    #     self.neighbourhood.create_neighbourhood()
    #     neighbourhood_record=NeighbourHood.objects.all()
    #     self.neighbourhood.delete_neighbourhood()
    #     self.assertTrue(len(neighbourhood_record)==0)

    def test_update_neighbourhood(self):
        new_neighbour=NeighbourHood.update_neighbourhood(self)
        expected_neighbour=f'{new_neighbour}'
        self.assertTrue(expected_neighbour,'new_neighbour')

