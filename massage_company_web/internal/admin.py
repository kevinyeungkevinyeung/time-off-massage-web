from django.contrib import admin
from .models import Client, Employee, MembershipRecord, Service, Transaction, Expense
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from datetime import date

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","phone_number","full_time")

admin.site.register(Employee,EmployeeAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name","price")

admin.site.register(Service,ServiceAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("date","client","service_id","amount_recieved")
    list_filter = (('date', DateRangeFilter),("client"))
    
    def get_rangefilter_created_at_default(self, request):
        return (date.today, date.today)

admin.site.register(Transaction, TransactionAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("employee_id","category","amount","paid","report_date")
    list_filter = (("paid"),("category"),('report_date', DateRangeFilter))

admin.site.register(Expense,ExpenseAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display =  ("first_name","last_name","gender","age","phone_number","email")
    
    list_filter = (("gender"),)

admin.site.register(Client, ClientAdmin)

class MembershipRecordAdmin(admin.ModelAdmin):
    list_display = ("client","amount_recieved","employee","transaction_date")
    list_filter = (('transaction_date', DateRangeFilter),("client"),("employee"))

admin.site.register(MembershipRecord,MembershipRecordAdmin)