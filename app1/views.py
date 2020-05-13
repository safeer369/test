from django.shortcuts import render
from django.http import HttpResponseRedirect
from app1.forms import EmployeeForm, salaryForm
from app1.models import Employee
from app1.models import salary

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def sidebar(request):
    return render(request,'sidebar.html')

def salary(request):
    form = salaryForm()
    if request.method == 'POST':
        print("qqqqqqqqqqq")
        form = salaryForm(request.POST, request.FILES)
        if form.is_valid():
            print("wwwwwwwwwwwwww")
            form.save()
            return HttpResponseRedirect('salary')
        else:
            print("############INVALID FORM############")
    return render(request,'Salary.html',{"form":form,"hra_rate":0.3,"ma_rate":-0.1,"da_rate":0.2,"ta_rate":0.1,"pf_rate":-0.25,"tax_rate":-0.2,"e-total_rate":("da_rate"+"hra_rate"+"ta_rate")})


# def employee(request):
#     return render(request,'employee_reg.html')

def saveEmployee(request):
    #if not request.session.has_key('username'):
        #return HttpResponseRedirect('login')
    print("called - 111111111")
    form = EmployeeForm()
    if request.method == 'POST':
        print("called - 2222222222")
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashboard')
        else:
            print("############INVALID FORM############")
        # else:
        #     return HttpResponseRedirect('dashboard')

    return render(request,'employee_reg.html',{"form":form})
