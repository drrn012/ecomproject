from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import ProductForm  
from .models import Product  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def home(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'main.html', {
        'products': products,
        'username': request.user.username,
        'last_login': request.user.last_login,
    })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  
            product.save()
            return redirect('home') 
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def product_json(request):
    products = Product.objects.filter(user=request.user)  
    data = list(products.values())  
    return JsonResponse(data, safe=False)

@login_required
def product_xml(request):
    products = Product.objects.filter(user=request.user)  
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')

@login_required
def product_json_by_id(request, id):
    product = Product.objects.filter(id=id, user=request.user).values()  
    if product:
        return JsonResponse(list(product), safe=False)
    return JsonResponse({'error': 'Product not found or not authorized'}, status=404)

@login_required
def product_xml_by_id(request, id):
    product = Product.objects.filter(id=id, user=request.user) 
    if product.exists():
        data = serializers.serialize('xml', product)
        return HttpResponse(data, content_type='application/xml')
    return HttpResponse('<error>Product not found or not authorized</error>', status=404, content_type='application/xml')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('home')

@csrf_exempt  # Use if CSRF tokens are not being sent with AJAX requests
@login_required
def create_product_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Ensure you're parsing the incoming JSON
            form = ProductForm(data)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user  # Assign the logged-in user to the product
                product.save()
                return JsonResponse({'success': True, 'product': {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,  # Ensure these fields exist in your model
                    'price': product.price  # Ensure these fields exist in your model
                }})
            return JsonResponse({'success': False, 'error': form.errors}, status=400)  # Return form errors if invalid
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)
