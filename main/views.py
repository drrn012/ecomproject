from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import ProductForm
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def home(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'main.html', {
        'products': products,
        'username': request.user.username,
        'last_login': request.user.last_login,
    })

# View to handle adding a product via form submission
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# View to display all products in JSON format
def product_json(request):
    products = Product.objects.all()
    data = list(products.values())  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)

# View to display all products in XML format
def product_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')

# View to display a product by its ID in JSON format
def product_json_by_id(request, id):
    product = Product.objects.filter(id=id).values()
    if product:
        return JsonResponse(list(product), safe=False)
    return JsonResponse({'error': 'Product not found'}, status=404)

# View to display a product by its ID in XML format
def product_xml_by_id(request, id):
    product = Product.objects.filter(id=id)
    if product.exists():
        data = serializers.serialize('xml', product)
        return HttpResponse(data, content_type='application/xml')
    return HttpResponse('<error>Product not found</error>', status=404, content_type='application/xml')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})