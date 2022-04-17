from django.db import models
from django import forms


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    def __str__(self):
        return self.full_name
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class My_Info(models.Model):
    first_name =  models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=4)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
    



class Products(models.Model):
    product_code = models.CharField(max_length=100, primary_key=True)
    product_name = models.CharField(max_length=100)
    sales_price = models.DecimalField(max_digits=22, decimal_places=2,default=0.00, blank=True)
    total_sales = models.IntegerField(blank=True,null=True)
    app_user_id = models.CharField(max_length=200,blank=False, null=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name

class Products_Sales(models.Model):
    product_code = models.ForeignKey(Products,on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=22, decimal_places=2,default=0.00, blank=True)
    total_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=22, decimal_places=2,default=0.00, blank=True)
    app_user_id = models.CharField(max_length=200,blank=True, null=True)
    app_data_time = models.DateTimeField(auto_now_add=True)






class client_account(models.Model):
    account_number=models.IntegerField(primary_key=True)
    client_name=models.CharField(max_length=10)
    client_address=models.CharField(max_length=10)
    client_nid=models.IntegerField()
    date_of_birth = models.DateField()
    totoal_deposit=models.IntegerField(null=True, blank=True)
    total_withdwral=models.IntegerField(null=True, blank=True)
    account_balance=models.IntegerField(null=True, blank=True)
    app_user_id=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.client_name
    

CHOICES=(
    ('D','Withdrwal'),
    ('c','Deposit'),
)


class Account_Transaction(models.Model):
    account_number=models.ForeignKey(client_account,on_delete=models.PROTECT)
    transaction_type =models.CharField(max_length=300, choices = CHOICES)
    transaction_amount=models.IntegerField()
    transaction_comments=models.CharField(max_length=100)
    app_user_id=models.IntegerField(null=True, blank=True)
    app_data_time=models.DateField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)



class Regions(models.Model):
    region_id = models.CharField(max_length=20, primary_key=True)
    region_name = models.CharField(max_length=200, blank=True, null=True)

class Jobs(models.Model):
    job_id = models.CharField(max_length=20, primary_key=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)


class Countries(models.Model):
    country_id = models.CharField(max_length=20, primary_key=True)
    country_name = models.CharField(max_length=200, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)


class Locations(models.Model):
    location_id = models.IntegerField( primary_key=True)
    street_address = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state_province = models.CharField(max_length=200, blank=True, null=True)
    country_id = models.CharField(max_length=20, blank=True, null=True)

class Departments(models.Model):
    department_id = models.IntegerField( primary_key=True)
    department_name = models.CharField(max_length=200, blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)


class Employees(models.Model):
    employee_id = models.IntegerField( primary_key=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    hire_date = models.DateField(null=True)
    job_id = models.CharField(max_length=200, blank=True, null=True)
    salary = models.DecimalField(max_digits=22, decimal_places=2,default=0.00, blank=True,null=True)
    commission_pct = models.DecimalField(max_digits=22, decimal_places=2,default=0.00, blank=True,null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)

class Job_History(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    start_date =  models.DateField(null=True)
    end_date =  models.DateField(null=True)
    job_id =  models.CharField(max_length=20, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)

class department(models.Model):
    
    dep_name=models.CharField(max_length=100,blank=False)
    dep_id=models.CharField( primary_key=True,auto_created=True,max_length=122)
    dep_location=models.CharField(max_length=200)
    app_user_id=models.CharField(max_length=100,blank=True)
    # app_data_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dep_name




