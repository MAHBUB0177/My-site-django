# Generated by Django 3.2.6 on 2022-03-30 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_account',
            fields=[
                ('account_number', models.IntegerField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=10)),
                ('client_address', models.CharField(max_length=10)),
                ('client_nid', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('totoal_deposit', models.IntegerField(blank=True, null=True)),
                ('total_withdwral', models.IntegerField(blank=True, null=True)),
                ('account_balance', models.IntegerField(blank=True, null=True)),
                ('app_user_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('country_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, max_length=200, null=True)),
                ('region_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('dep_id', models.CharField(auto_created=True, max_length=122, primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_location', models.CharField(max_length=200)),
                ('app_user_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(blank=True, max_length=200, null=True)),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('location_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('hire_date', models.DateField(null=True)),
                ('job_id', models.CharField(blank=True, max_length=200, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22, null=True)),
                ('commission_pct', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22, null=True)),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('department_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('job_id', models.CharField(blank=True, max_length=20, null=True)),
                ('department_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('min_salary', models.IntegerField(blank=True, null=True)),
                ('max_salary', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_id', models.IntegerField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(blank=True, max_length=200, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state_province', models.CharField(blank=True, max_length=200, null=True)),
                ('country_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='My_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('sales_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22)),
                ('total_sales', models.IntegerField(blank=True, null=True)),
                ('app_user_id', models.CharField(max_length=200, null=True)),
                ('app_data_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('region_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('region_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Products_Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22)),
                ('total_quantity', models.IntegerField()),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22)),
                ('app_user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('app_data_time', models.DateTimeField(auto_now_add=True)),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.products')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=4)),
                ('mobile', models.CharField(max_length=15)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.position')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.reporter')),
            ],
        ),
        migrations.CreateModel(
            name='Account_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('D', 'Withdrwal'), ('c', 'Deposit')], max_length=300)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_comments', models.CharField(max_length=100)),
                ('app_user_id', models.IntegerField(blank=True, null=True)),
                ('app_data_time', models.DateField(auto_now_add=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.client_account')),
            ],
        ),
    ]
