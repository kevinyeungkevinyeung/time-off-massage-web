from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.
class Client(models.Model):
    
    """
    This Model Describe and store information about the clients
    
    client_id = unique id for each client, this is the primary key for the tabke
    
    first_name = the first name of the client
    
    last_name = the last name of the client
    
    age = the age of the client
    
    phone_number = the phone number of the client
        # this is the mandatory field
        
    email = the email address of the client
    
    joined_date = the date when the client first joined
    """
    
    GENDER_CHOICE = (
                    ('male',"Male"),
                    ('female','Female'),
                    ('others','Others')
    )
    
    # unique id for each customer, this id will be auto-gen
    cleint_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(
                            validators=[MinValueValidator(1),MaxValueValidator(100)]
                            )
    
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    email = models.EmailField(null=True, unique=True)
    joined_date = models.DateField()
    last_updated = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    
class Employee(models.Model):
    
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    full_time = models.BooleanField(default=False)
    monthly_salary = models.DecimalField(max_digits=8, decimal_places=2)
    joined_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class MembershipRecord(models.Model):
    
    # client who purchased the membership
    client = models.ForeignKey(Client, null=True, on_delete= models.SET_NULL)
    amount_recieved = models.DecimalField(max_digits=8, decimal_places=2)
    amount_worth = models.DecimalField(max_digits=8, decimal_places=2)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    commission_paid = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_date = models.DateField()
    record_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client}"
    
    class Meta:
        ordering = ['-transaction_date',]
    

    
class Service(models.Model):
    
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.service_name}-${self.price}"
    
    
class Transaction(models.Model):
    
    SERVICE_CHOICES = (
                    ("feet_massage","Feet Massage"),
                    ("full_body","Full Body"),
                    ("cupping","Cupping"),
                    ("basic_oil_massage","Basic Oil Massage")
    )
    
    LEAD_CHOICES = (
                    ("friends_and_family","Friends and Family"),
                    ("ig","Instagram"),
                    ("plaform","Platform"),
                    ("poster","Poster")
    )
    
    trans_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, null=True, on_delete= models.SET_NULL)
    service_id = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    existing_customer = models.BooleanField(default=False)
    amount_recieved = models.DecimalField(max_digits=8, decimal_places=2, default=False)
    tips = models.DecimalField(max_digits=8, decimal_places=2)
    lead = models.CharField(max_length=30, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.date}-{self.client}-{self.service_id}"
    
    class Meta:
            ordering = ['-date',]
    
    
class Expense(models.Model):
    
    EXPENSE_CHOICE = (
                    ('salary',"Salary"),
                    ('rent','Rent'),
                    ('utilties','Utilities'),
                    ('marketing',"Marketing"),
                    ("promotion","Promotion"),
                    ("equipment","Equipment"),
                    ("others","Others"),
                    
    )
    
    expense_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=False)
    category = models.CharField(max_length=25, choices=EXPENSE_CHOICE)
    paid = models.BooleanField(default=False)
    note = models.TextField()
    attachment = models.ImageField(upload_to='images',null=True,blank=True)
    report_date = models.DateField()
    
    def __str__(self):
        return f"{self.employee_id}--{self.amount}"