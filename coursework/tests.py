from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from myapp.models import Customer, Admin, Equipment, Reservation, Report, AdminandEquipment
from django.urls import reverse
from django.contrib.auth.models import User, Group
from myapp.models import Equipment, Reservation, Customer
from myapp.forms import CreateUserForm
from django.contrib.messages import get_messages

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.customer = Customer.objects.create(
            user=self.user,
            userID='TEST001',
            user_firstname='John',
            user_lastname='Doe',
            user_Email='john@example.com',
            user_password='password',
            user_Dateofbirth=timezone.now(),
            user_accountstatus=0,
            user_creationDate=timezone.now(),
            user_currentReservation='',
            user_historicalreservation='',
            user_phoneNumber='1234567890',
            user_address='123 Test St',
            userType=0,
            profile_pic=None
        )
        self.admin = Admin.objects.create(
            adminID='ADMIN001',
            admin_firstname='Jane',
            admin_lastname='Smith',
            admin_username='jane',
            admin_Email='jane@example.com',
            admin_password='password',
            admin_Dateofbirth=timezone.now(),
            admin_accountstatus=0,
            admin_creationDate=timezone.now(),
            admin_phoneNumber='9876543210',
            admin_address='456 Admin Ave',
            Report=None
        )
        self.equipment = Equipment.objects.create(
            EquipmentID='EQUIP001',
            Equipmentname='Laptop',
            Equipment_type='Laptop',
            Equipment_category='PC/Laptop',
            Equipment_lastUsed=timezone.now(),
            Equipment_warrantyinfo=timezone.now(),
            Equipment_assignedlocation='XR Lab',
            Equipment_restrictionStatus=0,
            Equipment_UsageType=0,
            Equipment_images=None,
            customer=self.customer
        )
        self.reservation = Reservation.objects.create(
            BookingID='BOOK001',
            Booking_status=0,
            Booking_madeDate=timezone.now(),
            Booking_startDate=timezone.now(),
            Booking_endDate=timezone.now(),
            Customer=self.customer,
            Admin=self.admin,
            Equipment=self.equipment
        )
        self.report = Report.objects.create(
            reportKey='REPORT001',
            lastgeneratedreport=timezone.now(),
            Admin=self.admin,
            Reservation=self.reservation
        )
        self.admin_and_equipment = AdminandEquipment.objects.create(
            Admin=self.admin,
            Equipment=self.equipment
        )

    def test_customer_model(self):
        self.assertEqual(self.customer.user_firstname, 'John')
        self.assertEqual(self.customer.user_lastname, 'Doe')
      

    def test_admin_model(self):
        self.assertEqual(self.admin.admin_firstname, 'Jane')
        self.assertEqual(self.admin.admin_lastname, 'Smith')
  

    def test_equipment_model(self):
        self.assertEqual(self.equipment.Equipmentname, 'Laptop')
        self.assertEqual(self.equipment.Equipment_category, 'PC/Laptop')


    def test_reservation_model(self):
        self.assertEqual(self.reservation.Booking_status, 0)
    
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.group = Group.objects.create(name='user')
        self.group.user_set.add(self.user)
        self.customer = Customer.objects.create(user=self.user)


    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_view(self):
        client = Client()
        response = client.get(reverse('loginpage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_loginadmin_view(self):
        client = Client()
        response = client.get(reverse('loginadmin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginadmin.html')

    def test_logoutuser_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('logoutuser'))
        self.assertEqual(response.status_code, 302)  # Redirects after logout

    def test_register_view(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UserRegister.html')

    def test_equipment_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('equipment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'equipment.html')

    def test_viewbookings_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('ViewBookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ViewBookings.html')

    def test_edituseraccount_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('EditUserAccount'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edituseraccount.html')

    def test_adminviewbookings_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('AdminViewBookings'))
        self.assertEqual(response.status_code, 403)  # Should return 403 because user is not admin

    def test_editbookingstatus_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('EditBookingStatus', kwargs={'booking': 'BOOK001', 'status': 1}))
        self.assertEqual(response.status_code, 200)

    def test_cart_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_profilepage_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('profilepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_notify_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('notify'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notify.html')

    def test_registerequipment_view(self):
        client = Client()
        response = client.get(reverse('RegisterEquipment'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page as it's for admin only

    def test_viewequipment_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('ViewEquipment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewequipment.html')

    def test_edit_equipment_view(self):
        client = Client()
        response = client.get(reverse('EditEquipment', kwargs={'equipmentid': '1'}))
        self.assertEqual(response.status_code, 302)  # Redirects to login page as it's for admin only

    def test_settings_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings.html')
