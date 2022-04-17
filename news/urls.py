from django.urls import path
from .views import *
urlpatterns = [
  
    path('home', Home.as_view(), name='home'),
    path('news-submit-action', news_submit_action, name='news-submit-action'),
    path('aboutme', about_me.as_view(), name='aboutme'),

    path('employee_insert', employee_form, name='employee_insert'),
    
    path('employee_list/',employee_list,name='employee_list'), # Rename the view of pervious one
    path('employee_update/<int:id>/',employee_form,name='employee_update'),
    path('employee_delete/<int:id>/',employee_delete,name='employee_delete'),

    path('employee_login', employee_login_view, name='employee-login'),

    path('employee-login-sbmit', employee_login_view, name='employee-login-sbmit'),
    path('employee-signup', employee_signup, name='employee-signup'),


    path('product-create-view', product_create_view.as_view(), name='product-create-view'),
    path('product-create-insert', product_create_insert, name='product-create-insert'),


    
    
    
    path('sales-create-view', sales_create_view.as_view(), name='sales-create-view'),
    path('sales-create-insert', sales_create_insert, name='sales-create-insert'),
    path('get-product-info/<slug:product_code>', get_product_info, name='get-product-info'),


    
    path('client_form',client_form,name='client_form'),
    path('client_update/<int:id>/',client_form,name='client_update'),
    path('client_list',client_list,name='client_list'),
    path('client_delete/<int:id>/',client_delete,name='client_delete'),

   


   path('account_oppening', account_oppening.as_view(), name='account_oppening'),
   path('account-create-insert', account_create_insert, name='account-create-insert'),

     

    





  

]
