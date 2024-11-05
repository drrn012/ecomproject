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


# Assignment 4

1. **What is the difference between HttpResponseRedirect() and redirect()?**

   `HttpResponseRedirect()` is a Django class that returns an HTTP response with a 302 status code, which indicates a temporary redirect. It requires a specific URL as an argument. On the other hand, `redirect()` is a shortcut function that simplifies the process of returning a redirect response. It can accept a model object, a view name, or a URL, and it handles the URL resolution for you, making it more versatile and user-friendly.

2. **Explain how the MoodEntry model is linked with User!**

   The `MoodEntry` model is linked with the `User` model through a ForeignKey relationship. This means each `MoodEntry` record is associated with a specific user, allowing the application to keep track of which user created each mood entry. This relationship is typically defined in the model with a line like `user = models.ForeignKey(User, on_delete=models.CASCADE)`.

3. **What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.**

   Authentication is the process of verifying the identity of a user (e.g., confirming a username and password), while authorization determines what an authenticated user is allowed to do (e.g., accessing specific views or performing certain actions). When a user logs in, Django verifies their credentials and creates a session for them, storing their user ID in the session. Django uses middleware to manage authentication and authorization, ensuring that only authenticated users can access certain views.

4. **How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.**

   Django remembers logged-in users by creating a session for them, which is stored on the server and linked to a session ID saved in a cookie on the user's browser. This allows Django to identify the user on subsequent requests. Other uses of cookies include storing user preferences, tracking user behavior, and maintaining shopping cart data. Not all cookies are safe; for example, cookies storing sensitive information should be secured with flags like `HttpOnly` and `Secure` to prevent access by client-side scripts and ensure they're transmitted over secure connections.

5. **Explain how I implemented the checklist step-by-step (apart from following the tutorial).**

   - Implemented user registration by creating a registration form and a corresponding view to handle form submissions.
   - Created login and logout functions to manage user sessions using Django's built-in authentication system.
   - Populated the database with two user accounts and three dummy entries for each using Django's admin interface.
   - Linked the `Product` model to the `User` model by adding a ForeignKey to the `Product` model.
   - Modified the main page template to display the logged-in user's username and last login time using Django's session framework.
   - Tested each function to ensure seamless user experience and functionality.


# Assignment 5

## 1. CSS Selectors Priority

When multiple CSS selectors target the same HTML element, the **priority order** is determined by specificity. CSS selectors are prioritized in the following order:

1. **Inline CSS**: Styles applied directly to an element using the `style` attribute have the highest specificity.
2. **ID Selectors**: Selectors targeting an element by its `id` (e.g., `#header`) take priority over class and element selectors.
3. **Class, Attribute, and Pseudo-class Selectors**: These selectors (e.g., `.class`, `[type="text"]`, or `:hover`) have lower priority than ID selectors but higher than element selectors.
4. **Element Selectors**: Targeting an element by its type (e.g., `p`, `h1`) has the lowest priority.

If two rules have the same specificity, the last one defined in the CSS will take precedence.

### Example:
```css
p {
  color: blue;
}
#myParagraph {
  color: red;
}
```

## 2. Importance of Responsive Design

Responsive design is a crucial concept in web development because it ensures that a website or application functions and appears optimally across different devices and screen sizes, from desktop monitors to mobile phones. With the rise of mobile browsing, having a responsive design improves accessibility and user experience.

### Example of Applications with Responsive Design:
- **Twitter**: Adjusts layout and interface seamlessly for desktops, tablets, and mobile devices.
- **Bootstrap Websites**: Responsive grid system adjusts the layout depending on the screen size.

### Example of Applications without Responsive Design:
- **Old Static Websites**: Many older websites designed for desktop use do not scale or adjust when viewed on smaller devices, leading to poor usability.

## 3. Margin, Border, and Padding

These three properties control the layout and spacing around and inside HTML elements in CSS:

- **Margin**: The space outside the element’s border, creating space between the element and other elements.
- **Border**: A line that surrounds the content and padding of an element. The border can be customized with thickness, color, and style.
- **Padding**: The space inside the element’s border, between the content and the border, pushing the content away from the edge.

### Example of Implementation:
```css
.box {
  margin: 20px;                /* Space around the element */
  border: 2px solid black;      /* The element's border */
  padding: 15px;               /* Space between the content and the border */
}
```

## 4. Flexbox and Grid Layout Concepts

### Flexbox:
Flexbox is a one-dimensional layout model used to create flexible and responsive layouts, aligning and distributing space among elements in a container. Flexbox is particularly useful for creating fluid, responsive layouts such as horizontal navigation bars or aligning elements that need to be organized in a single direction (either row or column).

#### Example of Flexbox:
```css
.container {
  display: flex;
  justify-content: space-around;  /* Distributes space between items */
  align-items: center;            /* Aligns items vertically */
}
```

## Grid Layout

Grid Layout is a two-dimensional system used to design web pages by defining both rows and columns. This system offers greater control over complex layouts where both vertical and horizontal placement matters.

### Example of Grid Layout:
```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* Creates 3 equal columns */
  grid-gap: 10px;                         /* Adds spacing between the grid items */
}
```

## 5. Implementation of Checklist

I started by implementing the functions in `views.py` to handle adding, editing, and deleting features for my Django project. After that, I searched for templates that I could use to edit all the features of my website effectively. 

Next, I added the necessary URLs into `urls.py` to ensure that all the functionalities worked correctly, including static file handling. Once everything was set up, I tested the features to work out any kinks that arose during implementation.

For the navigation bar, I drew inspiration from the tutorial as well as other sites. I aimed to implement a side sliding bar feature using CSS to enhance user experience. After getting that in place, I focused on modifying the overall appearance of the website to make it look nicer and more polished.

In this assignment, I also incorporated Bootstrap to help me implement the CSS styles I desired, which significantly improved the design and responsiveness of my project.

# Assignment 6

## Benefits of Using JavaScript in Developing Web Applications
JavaScript is an essential technology for developing modern web applications. Here are some key benefits of using JavaScript:

- **Client-Side Execution**: JavaScript runs in the browser, which reduces server load and improves user experience by providing faster interactions.
- **Dynamic Content**: JavaScript enables dynamic updates to web pages without requiring a full reload, enhancing interactivity and user engagement.
- **Rich User Interfaces**: JavaScript allows the creation of rich user interfaces with features such as animations, drag-and-drop functionality, and responsive design.
- **Frameworks and Libraries**: JavaScript has a wide range of frameworks (like React, Angular, and Vue.js) and libraries (like jQuery) that simplify development and improve productivity.
- **Community and Resources**: A large community and extensive resources make it easier to find solutions, tools, and support for JavaScript development.

## Why We Need to Use `await` When We Call `fetch()`
Using `await` with the `fetch()` function is crucial because it makes the asynchronous operation more manageable. 

- **Simplified Syntax**: When we use `await`, we can write asynchronous code in a more straightforward, synchronous-looking manner, which improves readability.
- **Handling Promises**: If we don't use `await`, the `fetch()` function will return a Promise, and we would need to use `.then()` and `.catch()` to handle the response and any potential errors, complicating the code. Not using `await` could lead to unexpected behavior since the code following the `fetch()` call would execute before the fetch is complete.

## Why We Need to Use the `csrf_exempt` Decorator on the View Used for AJAX POST
The `csrf_exempt` decorator is necessary for AJAX POST requests when CSRF tokens are not included in the request. 

- **Security**: CSRF tokens are meant to prevent unauthorized actions on behalf of authenticated users. However, when making AJAX requests, especially from third-party sources or when the frontend is not configured to send CSRF tokens, the request may be rejected due to missing or invalid tokens. 
- **Development Convenience**: During development or for specific views where CSRF protection is not a concern, using `csrf_exempt` allows the AJAX request to succeed without requiring token validation.

## Why User Input Sanitization Cannot Be Done Just in the Front-End
User input sanitization is essential on both the front-end and back-end for several reasons:

- **Security Risks**: Relying solely on front-end sanitization exposes the application to security vulnerabilities. Users can bypass client-side validation by disabling JavaScript or manipulating requests.
- **Data Integrity**: Back-end validation ensures that only valid data is processed and stored in the database, maintaining data integrity.
- **Consistent Rules**: Sanitizing input on the back-end ensures consistent validation rules are applied, regardless of how the data is submitted (e.g., via API, form submission, etc.).

## Step-by-Step Implementation of AJAX for Adding Products
1. **Set Up the AJAX Request**: I created a button in the `main.html` file that triggers a modal form for adding a new product. This modal contains input fields for product name, price, and description.

2. **AJAX Function**: I wrote a JavaScript function that sends an AJAX POST request to the `create-ajax/` URL when the form is submitted. This function utilizes `fetch()` to send the form data in JSON format.

3. **Handling Responses**: Upon receiving a response from the server, I checked if the product was successfully created. If it was, I updated the product list dynamically without refreshing the page. If there were errors, I displayed the error messages to the user.

4. **CSRF Protection**: For security, I applied the `csrf_exempt` decorator to the view handling the AJAX POST request. This allowed the AJAX call to succeed even if CSRF tokens were not included, simplifying the development process.

5. **User Experience Enhancements**: After successfully adding a product, I ensured that the input fields in the modal are cleared for the next entry, and I provided visual feedback to the user regarding the success or failure of their submission.

This implementation allows for a smooth and interactive experience when adding products to the application, leveraging the power of AJAX and JavaScript.

# Assignment 7
# E-Commerce App

## Description
This application is designed as part of the Basic Elements of Flutter assignment. It features three buttons for viewing products, adding products, and logging out, complete with Snackbar notifications.

## Explanation of Widgets
- **Stateless Widgets**: Widgets that do not maintain any state. They are immutable, meaning their properties cannot change after they are built. Example: `Icon`, `Text`, `ElevatedButton`.
- **Stateful Widgets**: Widgets that can change their state during their lifecycle. They are mutable and can be redrawn based on state changes. Example: `Form`, `TextField`, and custom widgets that manage their own state.

### Widgets Used
- `MaterialApp`: Sets up the application.
- `Scaffold`: Provides a structure for the app with an AppBar and body.
- `ElevatedButton`: Represents a button that can be pressed.
- `SnackBar`: Displays messages at the bottom of the screen.
- `Column`: Arranges widgets vertically.

## Use-case for `setState()`
The `setState()` method is used in stateful widgets to notify Flutter that the state has changed and that the widget needs to be rebuilt. It affects any variables that are part of the widget's state. For example, if you had a counter, calling `setState()` would update the UI to reflect the new value of the counter.

## Difference between `const` and `final`
- **const**: Used to declare compile-time constants. The value must be known at compile time and cannot change.
- **final**: Used to declare a variable that can only be set once. The value can be set at runtime but cannot be reassigned after that.

## Implementation Steps
1. Created a new Flutter application.
2. Designed a home screen with an AppBar and centered buttons.
3. Implemented three buttons with icons and Snackbar messages.
4. Customized the button colors for better user experience.
5. Tested the application to ensure buttons display correct messages.

## GitHub Repository
Ensure you add your repository link here after pushing your code.
