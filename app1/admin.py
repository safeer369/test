from django.contrib import admin
from app1.models import Gender,MaritalStatus,Designation,Department,Employee,salary

# Register your models here.

admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(salary)
