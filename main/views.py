from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import ProductForm
from .models import Product

# Home page view
def home(request):
    return render(request, 'main.html')

# View to handle adding a product via form submission
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-json')  # Redirect to a page to list all products (optional)
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
