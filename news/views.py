from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from.models import *


from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import render, redirect

from .forms import clieantAccountFrom
from .models import client_account

   
from django.db import connection, transaction
from .forms import *
import json
from django.http import JsonResponse


# Create your views here.
class Home(TemplateView):
    template_name='news/bootstrap.html'

def news_submit_action(request):
    print("Hello")
    fname = request.GET["fname"]
    lname = request.GET["lname"]
    mydata = My_Info(first_name=fname, last_name=lname)
    mydata.save()
    print(fname)
    print(lname)
    return render(request, 'news/index.html')



class about_me(TemplateView):
    template_name='news/aboutme.html'
    def get(self, request):
        data = dict()
        request.session["user_full_name"] = "Full Name"
        data["user_full_name"]=request.session["user_full_name"]
        return render(request, self.template_name, data)




def employee_form(request, id=0):
    
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "news/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "news/employee_list.html", context)

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')



def employee_login_view(request):
    if request.method=='GET':
        return render(request,'news/employee_login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session["app_user_id"]=username
                return redirect('employee_list')
        else:
            return render(request,'news/employee_login.html',{'message':"invalid username and password"})



def employee_signup(request):
    if request.method == "GET":
        return render(request, "news/employee-signup.html")
    else:
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        confirm_password = request.POST.get('confirm_password', False)

        if len(username)==0 or len(password)==0:
            return render(request, "news/employee-signup.html", {"message": "Please check your Input"})

        if password != confirm_password:
            return render(request, "news/employee-signup.html", {"message": "Password and Confirm Password does't match"})
        else:
            user = User.objects.create_user(username, '', password)
            user.save()
        return render(request, 'news/employee_login.html')

 


class product_create_view(TemplateView):
    template_name = 'news/product-create.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'news/employee_login.html')
        data = dict()
        form = ProductsModelForm()
        data['form']=form
        return render(request, self.template_name, data)

@transaction.atomic
def product_create_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'news/employee_login.html')
    data=dict()
    data['form_is_valid'] = False

    if request.method=='POST':
        form = ProductsModelForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    app_user_id = request.session["app_user_id"]

                    sales_price = form.cleaned_data['sales_price']
                    product_code = form.cleaned_data['product_code']

                    if Products.objects.filter(product_code=product_code).exists():
                        data['error_message']='Product Code Already Exist!'
                        return JsonResponse(data)

                    if sales_price<0:
                        data['error_message']='Sales price should not be negative values!'
                        return JsonResponse(data)

                    post = form.save(commit=False)
                    post.app_user_id = app_user_id
                    post.save()
                    data['form_is_valid'] = True
                    data['succ_message'] = "Save Successfully"
            except Exception as e:
                print(str(e))
                data['form_is_valid'] = False
                data['error_message']=str(e)
                return JsonResponse(data)
        else:
            data['error_message']=form.errors.as_json()
    return JsonResponse(data)


class sales_create_view(TemplateView):
    template_name = 'news/product-sales.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'news/employee_login.html')
        data = dict()
        form = ProductsSalesModelForm()
        data['form'] = form
        return render(request, self.template_name, data)


@transaction.atomic
def sales_create_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'news/employee_login.html')
    data=dict()
    data['form_is_valid'] = False

    if request.method=='POST':
        form = ProductsSalesModelForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    app_user_id = request.session["app_user_id"]
                    product_code = form.cleaned_data['product_code']

                    post = form.save(commit=False)
                    post.app_user_id = app_user_id
                    post.save()
                    data['form_is_valid'] = True
                    data['succ_message'] = "Save Successfully"
            except Exception as e:
                print(str(e))
                data['form_is_valid'] = False
                data['error_message']=str(e)
                return JsonResponse(data)
        else:
            data['error_message']=form.errors.as_json()
    return JsonResponse(data)


def get_product_info(request, product_code):

    data = dict()
    product_name=''
    sales_price=0
    try:
        product_info = Products.objects.get(product_code=product_code)
        product_name = product_info.product_name
        sales_price = product_info.sales_price
    except Exception as e:
        product_name = ''
        sales_price=0

    data['product_name']=product_name
    data['sales_price']=sales_price
    data['form_is_valid'] = True
    return JsonResponse(data)





def client_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = clieantAccountFrom()
        else:
            client = client_account.objects.get(pk=id)
            form = clieantAccountFrom(instance=client)
        return render(request, "news/client_account.html", {'form': form})
    else:
        if id == 0:
            form = clieantAccountFrom(request.POST)
        else:
            client = client_account.objects.get(pk=id)
            form = clieantAccountFrom(request.POST,instance= client)
        if form.is_valid():
            form.save()
        return redirect('client_list')

def client_list(request):
    query=client_account.objects.all()
    dict={'query':query}
    return render(request,'news/client_list.html',context=dict)

def client_delete(request,id):
    client = client_account.objects.get(pk=id)
    client.delete()
    return redirect('client_list')





class account_oppening(TemplateView):

    template_name = 'news/account_create.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'news/client_login.html')
        data = dict()
        form = accounttransactionForm()
        data['form']=form
        return render(request, self.template_name, data)



@transaction.atomic
def account_create_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'news/client_login.html')
    data=dict()
    data['form_is_valid'] = False

    if request.method=='POST':
        form = accounttransactionForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    app_user_id = request.session["app_user_id"]
                    account_number = form.cleaned_data['account_number']

                    if Account_Transaction.objects.filter(account_number=account_number).exists():
                        data['error_message']='account_number Already Exist!'
                        return JsonResponse(data)

                        

                    # if sales_price<0:
                    #     data['error_message']='Sales price should not be negative values!'
                    #     return JsonResponse(data)

                    post = form.save(commit=False)
                    post.app_user_id = app_user_id
                    post.save()
                    data['form_is_valid'] = True
                    data['succ_message'] = "Save Successfully"
            except Exception as e:
                print(str(e))
                data['form_is_valid'] = False
                data['error_message']=str(e)
                return JsonResponse(data)
        else:
            data['error_message']=form.errors.as_json()
    return JsonResponse(data)





