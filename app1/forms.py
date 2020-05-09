from django import forms
from app1.models import Employee, salary

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    #def clean_regno(self):
        #rno = self.cleaned_data['regno']
        #if (not rno.isdigit()) or (len(rno) != 4):
            #raise forms.ValidationError('Code Must be Numeric with 4 digits')
        #return rno
class salaryForm(forms.ModelForm):
    class Meta:
        model= salary
        fields='__all__'
