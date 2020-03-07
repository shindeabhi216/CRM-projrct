from django.shortcuts import render,redirect
from .models import Customers,Products,Orders
from .forms import OrderForm,CustomerForm,ProductForm,CreateUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_user,allowed_users,admin_only

@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    customers = Customers.objects.all()
    products=Products.objects.all()
    orders=Orders.objects.all()
 #   orders=Orders.objects.filter(status__in= ('delivered','pending','outfordelivery'))[0:5]
    total_order = len(orders)
   # delivered= orders.filter(status='Delivered').count()
    delivered =orders.filter(status='Delivered').count()
    pending= orders.filter(status='Pending').count()
    outfordelivery= orders.filter(status='Outfordelivery').count()
    context = {'customers': customers,'products':products,'orders':orders,
               'total_order':total_order,
               #'delivered':delivered,
               'delivered':delivered,
               'pending':pending,
               'outfordelivery':outfordelivery
               }
    return render(request,'crmaccounts/dashboard.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request):
    products=Products.objects.all()
    context={'products':products}
    return render(request,'crmaccounts/products.html',context )


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, str_pk):
    customers= Customers.objects.get(id=str_pk)
    orders= customers.orders_set.all()
    total_orders= orders.count()
    context={'customers':customers,'orders':orders,'total_orders':total_orders}
    return render(request,'crmaccounts/customers.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request):
    form = OrderForm()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request, 'crmaccounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request,pk):
    order = Orders.objects.get(id=pk)
    form =OrderForm(instance=order)
    if request.method =="POST":
        form =OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(request, 'crmaccounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request,pk):
    order = Orders.objects.get(id=pk)
    order.delete()
    return redirect("/")


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_customer(request,pk):
    customer = Customers.objects.get(id=pk)
    form =CustomerForm(instance=customer)
    if request.method =="POST":
        form= CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/")
    context ={'form':form}
    return render(request,'crmaccounts/update_customer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_customer(request,pk):
    customer =Customers.objects.get(id=pk)
    customer.delete()
    return redirect("/")


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_product(request,pk):
    product = Products.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form':form}
    return render(request,'crmaccounts/update_product.html',context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def delete_product(request,pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return redirect("/")

@unauthenticated_user
def registerpage(request):
    form=CreateUserForm()
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user =request.POST.get('username')
            messages.success(request,"Successfully account is created for "+user)
            return redirect('login')
    context={'form':form}
    return render(request,'crmaccounts/register.html',context)

@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        uname =request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Username or Password is Wrong')
    return render(request,'crmaccounts/login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    customers = Customers.objects.get(user=request.user)
    orders = request.user.customers.orders_set.all()
    total_order = len(orders)
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    outfordelivery = orders.filter(status='Outfordelivery').count()
    context = {'orders': orders,
               'total_order': total_order,
               'delivered': delivered,
               'pending': pending,
               'outfordelivery': outfordelivery,
               'cutomers':customers}
    return render(request,'crmaccounts/user.html',context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
# def userPage(request):
#     orders = request.user.customers.orders_set.all()
#     total_order = len(orders)
#     context={'total_order':total_order}
#     return render(request,'crmaccounts/user.html',context)

















