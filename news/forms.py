from django import forms
from .models import *
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False


# from .models import *
class ProductsModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_code', 'product_name', 'sales_price')
        labels = {
            'product_code':'Product Code',
            'product_name':'Product Name',
            'sales_price':'Sales Price',
        }


class ProductsSalesModelForm(forms.ModelForm):
    product_name = forms.CharField(label='Product Name', initial="",)
    def __init__(self, *args, **kwargs):
        super(ProductsSalesModelForm, self).__init__(*args, **kwargs)
        self.fields['unit_price'].widget.attrs['readonly'] = True
        self.fields['total_price'].widget.attrs['readonly'] = True
        self.fields['product_name'].widget.attrs['readonly'] = True
        self.fields['product_name'].initial = ""
        self.fields['product_name'].required = False

    class Meta:
        model = Products_Sales
        fields = ('unit_price', 'total_quantity', 'total_price', 'product_code','product_name')
        labels = {
            'product_code':'Product Code',
            'unit_price':'unit price',
            'total_price':'Total Price',
            'total_quantity':'Total Quantity',
        }

# class account_info(forms.ModelForm):
#      class Meta:
#             model = client_account
#         fields = ('account_number', 'client_name', 'date_of_birth', 'client_nid')
#         labels = {
#             'account_number':'Account number',
#             'client_name':'Client Name',
#             'date_of_birth':'Date Of Birth',
#             'client_nid':'Client Nid ',
#         }


        
class DateInput(forms.DateInput):
       input_type = 'date'

class clieantAccountFrom(forms.ModelForm):
    class Meta:
        model = client_account
        fields = ('account_number', 'client_name', 'client_address','client_nid','date_of_birth','totoal_deposit','total_withdwral','account_balance')
        widgets = {
                'date_of_birth': DateInput(),
                 }
        labels = {
                'account_number':'Account number ',
                'client_name':'Client Name',
                

            }

class DateInput(forms.DateInput):
         input_type = 'date'
class accounttransactionForm(forms.ModelForm):
     class Meta:
        model = Account_Transaction
        fields = ('account_number', 'transaction_type', 'transaction_amount','transaction_comments','date_of_birth')
        widgets = {
                'date_of_birth': DateInput(),
                 }
        labels = {
                'account_number':'Account number ',
                
                

            }

