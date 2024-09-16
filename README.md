# Assignment 2

## 1. Project Initialization:
I started by creating a Django project with the command:

```bash
django-admin startproject ecomproject
```

This set up the core structure of the project. In settings.py, I made sure the basic configurations were in place:

Database: I set up the database connection. I used the default SQLite for development, but I configured it so that when I deploy to PWS, I can switch to PostgreSQL or MySQL easily.

Allowed Hosts: I added localhost for development and the PWS domain to allow hosting.
Static Files: I configured the paths to static files (like CSS and JavaScript) so that they could be properly served in both local and production environments.

## 2. App Creation:
I created a new app called store to handle the core functionality of the e-commerce platform:

```bash
python manage.py startapp store
```

In the project's settings.py, I registered this new app in INSTALLED_APPS so Django could recognize it.

## 3. Database Models:
In models.py within the store app, I created three models: Product, Category, and Order. For each of these models, I defined fields that reflect the business logic of the e-commerce platform, such as product names, prices, categories, and order details.

After defining the models, I ran the following commands to apply these changes to the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

This created the necessary tables in the database.

## 4. Views and Templates:
Next, I worked on the logic for the views. In views.py, I created functions to handle requests for product listings, individual product details, and cart management. Each function processed user requests and fetched the required data from the database.

For the user interface, I used Django's template system. I created dynamic HTML templates that pulled in data from the views, making sure the content displayed on the page reflected what was in the database.

## 5. URLs and Routing:
In urls.py, I mapped specific URL paths to the corresponding view functions. For example, when a user visits the product listing page, the URL pattern in urls.py sends that request to the product_list view, which retrieves the data and renders the correct template. This step ensures that users can navigate through different pages of the website.

## 6. PWS Deployment:
To deploy the project on Pacil Web Service (PWS), I had to make sure my application was production-ready. I configured settings such as DEBUG = False, added the PWS domain to ALLOWED_HOSTS, and set up static file handling. After testing everything locally, I pushed the project to PWS.

I also configured my deployment files, including the wsgi.py and requirements.txt, to ensure everything worked smoothly on the server. After deploying, I tested the website to confirm everything was functioning as expected.

## 7. Request-Response Flow Diagram:
To summarize how the system works, here’s a simplified flow of what happens when a client sends a request:

```bash
+--------+        +--------------------+        +--------------------+
| Client | -----> |      urls.py        | -----> |      views.py       |
+--------+        +--------------------+        +--------------------+
      |                                         |
      |                                         |
      V                                         V
  +------------+                           +-------------+
  | HTTP GET/  | <-- models.py <-- HTML <--|   Database   |
  | HTTP POST  |                           +-------------+
  +------------+

```
Here’s how it works:

urls.py: Maps the URL path (like /products/) to the correct view function (like product_list).
views.py: Handles the request, retrieves data from the database using the models, and renders the appropriate HTML template.
models.py: Interacts with the database to perform CRUD operations (like fetching products).
HTML Templates: Display the data fetched by the views in a user-friendly format.

## 8. The Use of Git in Software Development:
Throughout development, I used Git for version control. With Git, I could:

Track all changes in the project, so I could always revert if something broke.
Work on different features in separate branches and merge them when ready.
Integrate with CI/CD pipelines to automatically deploy or test the code after each push to the repository.

```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

I also took advantage of the rebase setting, which helped keep my Git history clean when merging changes.

## 9. Why Django Is a Great Starting Point for Learning Software Development?
Django is a fantastic choice for beginners because:

Batteries-included: It comes with so many built-in tools, like an admin panel, authentication system, and form handling, making it easier to start building real applications.
Clear structure: Django follows the Model-View-Controller (MVC) architecture, which separates the logic, data, and presentation layers, helping to build good habits in software development.
Community and security: There’s extensive documentation, and Django handles security issues like SQL injection and XSS out of the box.

## 10. Why Django’s Model is Called an ORM?
Django’s model system is an Object-Relational Mapping (ORM) tool. This means I can work with the database using Python code instead of SQL. For example, instead of writing a SQL query to fetch all products, I can do this in Python:

```bash
products = Product.objects.all()
```

This abstracts away the complexity of writing raw SQL and makes database operations smoother and more intuitive.





# Assignment 3

## Implementation

1. **Form Input**
   - Added a form to `add_product` view for inputting model objects.

2. **Views and Routing**
   - Implemented views to handle data in JSON and XML formats, including by ID.
   - Configured routing in `urls.py` to map these views.

## Questions

1. **Why We Need Data Delivery**
   - Data delivery is essential for exchanging information between systems and applications, allowing for data to be shared and utilized in different formats.

2. **XML vs. JSON**
   - JSON is generally preferred due to its simplicity, lighter weight, and better integration with modern web technologies. It’s more readable and easier to parse compared to XML.

3. **`is_valid()` Method**
   - The `is_valid()` method validates form data, ensuring it meets the requirements before processing or saving.

4. **CSRF Protection**
   - `csrf_token` prevents CSRF attacks by ensuring form submissions are legitimate and come from the intended site.

## Postman Screenshots

- JSON Response: ![JSON Response](/Users/darren/Desktop/my_ecommerce_project/Assignment3Proof/Assignment3_json.png)
- XML Response: ![XML Response](/Users/darren/Desktop/my_ecommerce_project/Assignment3Proof/Assignment3_xml.png)
- JSON by ID: ![JSON by ID](/Users/darren/Desktop/my_ecommerce_project/Assignment3Proof/Assignment3_jsonwithID.png)
- XML by ID: ![XML by ID](![path/to/xml-by-id-screenshot.png](Assignment3Proof/Assignment3_xmlwithID.png))

## Deployment

- [Link to PWS Application](http://derensh-pandian-ecomproject.pbp.cs.ui.ac.id)

copy this if it doesn't work:
http://derensh-pandian-ecomproject.pbp.cs.ui.ac.id


## Proof
