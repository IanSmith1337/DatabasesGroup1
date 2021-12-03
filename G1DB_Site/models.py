from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    uid = models.CharField(db_column='uid', primary_key=True, max_length=255)
    email = models.EmailField(db_column='email')
    name = models.CharField(db_column='name', blank=True, max_length=255)
    
    class Meta:
        db_table = 'user'

class Customer(models.Model):
    custid = models.AutoField(db_column='Custid', primary_key=True)  # Field name made lowercase.
    custname = models.CharField(db_column='CustName', max_length=10)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'customer'


class Employee(models.Model):
    empid = models.AutoField(db_column='Empid', primary_key=True)  # Field name made lowercase
    fname = models.CharField(db_column='Fname', max_length=10)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'employee'

class RankData(models.Model):
    rank=models.IntegerField()
    zipcode=models.CharField(max_length=100)
    
    class Meta:
        db_table = 'rankdata'

class Order1(models.Model):
    orderid = models.AutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    deliveryfee = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(db_column='Total_amount', blank=True, null=True)  # Field name made lowercase.
    deliveryid = models.ForeignKey('Delivery', models.DO_NOTHING, db_column='deliveryid', blank=True, null=True)
    custid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Custid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'order1'


class Orderdetails(models.Model):
    orderdetailid = models.AutoField(primary_key=True)
    ordertype = models.CharField(max_length=20)
    amount = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    orderdate = models.DateTimeField()
    custid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Custid', blank=True, null=True)  # Field name made lowercase.
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='Empid', blank=True, null=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Order1, models.DO_NOTHING, db_column='orderid', blank=True, null=True)
    
    class Meta:
        db_table = 'orderdetails'

class Delivery(models.Model):
    deliveryid = models.AutoField(primary_key=True)
    deliveryfee = models.FloatField(blank=True, null=True)
    deliverytype = models.CharField(db_column='Deliverytype', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='Empid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'delivery'


class Hotspot(models.Model):
    zipcode = models.CharField(db_column='Zipcode', primary_key=True, max_length=5)  # Field name made lowercase.
    hotspotfee = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    deliveryid = models.ForeignKey(Delivery, models.DO_NOTHING, db_column='deliveryid', blank=True, null=True)

    class Meta:
        db_table = 'hotspot'


"""class Items(models.Model):
    itemid = models.AutoField(primary_key=True)
    itemprice = models.FloatField(blank=True, null=True)
    itemname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'items'"""

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

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





class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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

class RestaurantorderappPost(models.Model):
    title = models.CharField(unique=True, max_length=300)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'restaurantorderapp_post'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)

