from django.shortcuts import render
from django.http import HttpResponseRedirect
from app1.forms import EmployeeForm
from app1.models import Employee

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def sidebar(request):
    return render(request,'sidebar.html')

def salary(request):
    return render(request,'Salary.html')


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
