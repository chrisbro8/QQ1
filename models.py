# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CourseworkAdmin(models.Model):
    admin_firstname = models.CharField(max_length=50, blank=True, null=True)
    admin_lastname = models.CharField(max_length=50, blank=True, null=True)
    admin_username = models.CharField(max_length=50, blank=True, null=True)
    admin_email = models.CharField(db_column='admin_Email', max_length=254, blank=True, null=True)  # Field name made lowercase.
    admin_password = models.CharField(max_length=50, blank=True, null=True)
    admin_dateofbirth = models.DateField(db_column='admin_Dateofbirth', blank=True, null=True)  # Field name made lowercase.
    admin_accountstatus = models.IntegerField(blank=True, null=True)
    admin_creationdate = models.DateTimeField(db_column='admin_creationDate', blank=True, null=True)  # Field name made lowercase.
    admin_address = models.CharField(max_length=50, blank=True, null=True)
    adminid = models.CharField(db_column='adminID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_id = models.BigIntegerField(db_column='User_id', blank=True, null=True)  # Field name made lowercase.
    admin_phonenumber = models.IntegerField(db_column='admin_phoneNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursework_admin'


class CourseworkAdminandequipment(models.Model):
    admin = models.OneToOneField(CourseworkAdmin, models.DO_NOTHING, db_column='Admin_id', blank=True, null=True)  # Field name made lowercase.
    equipment = models.OneToOneField('CourseworkEquipment', models.DO_NOTHING, db_column='Equipment_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursework_adminandequipment'


class CourseworkEquipment(models.Model):
    equipmentid = models.CharField(db_column='EquipmentID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipmentname = models.CharField(db_column='Equipmentname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipment_type = models.CharField(db_column='Equipment_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipment_category = models.CharField(db_column='Equipment_category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipment_lastused = models.DateTimeField(db_column='Equipment_lastUsed', blank=True, null=True)  # Field name made lowercase.
    equipment_warrantyinfo = models.DateTimeField(db_column='Equipment_warrantyinfo', blank=True, null=True)  # Field name made lowercase.
    equipment_assignedlocation = models.CharField(db_column='Equipment_assignedlocation', max_length=30, blank=True, null=True)  # Field name made lowercase.
    equipment_restrictionstatus = models.IntegerField(db_column='Equipment_restrictionStatus', blank=True, null=True)  # Field name made lowercase.
    equipment_usagetype = models.IntegerField(db_column='Equipment_UsageType', blank=True, null=True)  # Field name made lowercase.
    equipment_images = models.CharField(db_column='Equipment_images', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursework_equipment'


class CourseworkReport(models.Model):
    reportkey = models.CharField(db_column='reportKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastgeneratedreport = models.DateTimeField(blank=True, null=True)
    reservation = models.ForeignKey('CourseworkReservation', models.DO_NOTHING, db_column='Reservation_id', blank=True, null=True)  # Field name made lowercase.
    admin = models.OneToOneField(CourseworkAdmin, models.DO_NOTHING, db_column='Admin_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursework_report'


class CourseworkReservation(models.Model):
    bookingid = models.CharField(db_column='BookingID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    booking_status = models.IntegerField(db_column='Booking_status', blank=True, null=True)  # Field name made lowercase.
    booking_alertstatus = models.IntegerField(db_column='Booking_alertstatus', blank=True, null=True)  # Field name made lowercase.
    booking_madedate = models.DateTimeField(db_column='Booking_madeDate', blank=True, null=True)  # Field name made lowercase.
    booking_startdate = models.DateTimeField(db_column='Booking_startDate', blank=True, null=True)  # Field name made lowercase.
    booking_enddate = models.DateTimeField(db_column='Booking_endDate', blank=True, null=True)  # Field name made lowercase.
    admin_id = models.BigIntegerField(db_column='Admin_id', blank=True, null=True)  # Field name made lowercase.
    user = models.OneToOneField('CourseworkUser', models.DO_NOTHING, db_column='User_id', blank=True, null=True)  # Field name made lowercase.
    equipment = models.ForeignKey(CourseworkEquipment, models.DO_NOTHING, db_column='Equipment_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursework_reservation'


class CourseworkUser(models.Model):
    userid = models.CharField(db_column='userID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='User_Email', max_length=254, blank=True, null=True)  # Field name made lowercase.
    user_accountstatus = models.IntegerField(db_column='User_accountstatus', blank=True, null=True)  # Field name made lowercase.
    user_address = models.CharField(db_column='User_address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_creationdate = models.DateTimeField(db_column='User_creationDate', blank=True, null=True)  # Field name made lowercase.
    user_currentreservation = models.CharField(db_column='User_currentReservation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_firstname = models.CharField(db_column='User_firstname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_historicalreservation = models.CharField(db_column='User_historicalreservation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_lastname = models.CharField(db_column='User_lastname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_password = models.CharField(db_column='User_password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usertype = models.IntegerField(db_column='UserType', blank=True, null=True)  # Field name made lowercase.
    user_dateofbirth = models.DateField(db_column='User_Dateofbirth')  # Field name made lowercase.
    user_phonenumber = models.CharField(db_column='User_phoneNumber', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursework_user'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
