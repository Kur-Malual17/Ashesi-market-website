# PHP to Python/Django Conversion Reference

Complete reference for converting PHP code to Python/Django.

## Basic Syntax

| PHP | Python |
|-----|--------|
| `<?php ... ?>` | No tags needed |
| `$variable` | `variable` |
| `$array = array()` | `list = []` or `dict = {}` |
| `echo "text"` | `print("text")` |
| `.` (concatenation) | `+` or f-strings |
| `->` (object) | `.` (dot notation) |
| `=>` (array) | `:` (dict) |
| `//` or `#` | `#` |
| `/* */` | `""" """` |

## Variables & Types

**PHP:**
```php
$name = "John";
$age = 25;
$price = 99.99;
$active = true;
$items = array(1, 2, 3);
$user = array('name' => 'John', 'age' => 25);
```

**Python:**
```python
name = "John"
age = 25
price = 99.99
active = True
items = [1, 2, 3]
user = {'name': 'John', 'age': 25}
```

## String Operations

**PHP:**
```php
$full = $first . " " . $last;
$msg = "Hello $name";
$upper = strtoupper($text);
$lower = strtolower($text);
$trimmed = trim($text);
```

**Python:**
```python
full = first + " " + last
msg = f"Hello {name}"
upper = text.upper()
lower = text.lower()
trimmed = text.strip()
```

## Control Structures

### If Statements

**PHP:**
```php
if ($age >= 18) {
    echo "Adult";
} elseif ($age >= 13) {
    echo "Teen";
} else {
    echo "Child";
}
```

**Python:**
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

### Loops

**PHP:**
```php
for ($i = 0; $i < 10; $i++) {
    echo $i;
}

foreach ($items as $item) {
    echo $item;
}

while ($x < 10) {
    $x++;
}
```

**Python:**
```python
for i in range(10):
    print(i)

for item in items:
    print(item)

while x < 10:
    x += 1
```

## Functions

**PHP:**
```php
function greet($name, $title = "Mr.") {
    return "Hello $title $name";
}

$result = greet("Smith");
```

**Python:**
```python
def greet(name, title="Mr."):
    return f"Hello {title} {name}"

result = greet("Smith")
```

## Classes

**PHP:**
```php
class User {
    private $name;
    
    public function __construct($name) {
        $this->name = $name;
    }
    
    public function getName() {
        return $this->name;
    }
}

$user = new User("John");
```

**Python:**
```python
class User:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

user = User("John")
```

## Database Operations

### PHP (MySQLi)
```php
$stmt = $conn->prepare('SELECT * FROM users WHERE email = ?');
$stmt->bind_param('s', $email);
$stmt->execute();
$result = $stmt->get_result();
$user = $result->fetch_assoc();

$stmt = $conn->prepare('INSERT INTO users (name, email) VALUES (?, ?)');
$stmt->bind_param('ss', $name, $email);
$stmt->execute();
```

### Django ORM
```python
# SELECT
user = User.objects.get(email=email)
users = User.objects.filter(is_active=True)
users = User.objects.all()

# INSERT
user = User.objects.create(name=name, email=email)

# UPDATE
user.name = "New Name"
user.save()

# DELETE
user.delete()
```

## Form Handling

### PHP
```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
    
    if (!$name) {
        $errors[] = 'Name required';
    }
}
```

### Django
```python
if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        # Process data
```

## File Uploads

### PHP
```php
if (!empty($_FILES['image']['name'])) {
    $ext = pathinfo($_FILES['image']['name'], PATHINFO_EXTENSION);
    $name = bin2hex(random_bytes(12)) . '.' . $ext;
    move_uploaded_file($_FILES['image']['tmp_name'], 'uploads/' . $name);
}
```

### Django
```python
# In model
class Product(models.Model):
    image = models.ImageField(upload_to='products/')

# In view
if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()  # Handles upload automatically
```

## Sessions

### PHP
```php
session_start();
$_SESSION['user_id'] = $user['id'];
$user_id = $_SESSION['user_id'] ?? null;
unset($_SESSION['user_id']);
session_destroy();
```

### Django
```python
# Set
request.session['user_id'] = user.id

# Get
user_id = request.session.get('user_id')

# Delete
del request.session['user_id']

# Clear all
request.session.flush()
```

## Authentication

### PHP
```php
$hash = password_hash($password, PASSWORD_BCRYPT);
if (password_verify($password, $hash)) {
    $_SESSION['user_id'] = $user['id'];
}
```

### Django
```python
from django.contrib.auth import authenticate, login

# Create user
user = User.objects.create_user(username=email, password=password)

# Login
user = authenticate(username=email, password=password)
if user:
    login(request, user)

# Check if logged in
if request.user.is_authenticated:
    # User is logged in
```

## Redirects

**PHP:**
```php
header('Location: /page.php');
exit;
```

**Python/Django:**
```python
from django.shortcuts import redirect
return redirect('page-name')
```

## JSON

**PHP:**
```php
$json = json_encode($data);
$data = json_decode($json, true);
```

**Python:**
```python
import json
json_str = json.dumps(data)
data = json.loads(json_str)
```

## Common Functions

| PHP | Python |
|-----|--------|
| `count($array)` | `len(list)` |
| `in_array($val, $arr)` | `val in list` |
| `array_push($arr, $val)` | `list.append(val)` |
| `implode(',', $arr)` | `','.join(list)` |
| `explode(',', $str)` | `str.split(',')` |
| `isset($var)` | `var is not None` |
| `empty($var)` | `not var` |
| `die($msg)` | `raise Exception(msg)` |
| `time()` | `import time; time.time()` |
| `date('Y-m-d')` | `from datetime import date; date.today()` |

## Django-Specific Patterns

### Views

**Function-based:**
```python
from django.shortcuts import render

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
```

**Class-based:**
```python
from django.views.generic import ListView

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
```

### Templates

**PHP:**
```php
<?php foreach ($products as $p): ?>
    <h2><?= htmlspecialchars($p['title']) ?></h2>
    <p><?= htmlspecialchars($p['description']) ?></p>
<?php endforeach; ?>
```

**Django:**
```django
{% for product in products %}
    <h2>{{ product.title }}</h2>
    <p>{{ product.description }}</p>
{% endfor %}
```

### URL Routing

**PHP:**
```php
// product.php?id=123
$id = $_GET['id'];
```

**Django:**
```python
# urls.py
path('products/<int:pk>/', views.product_detail, name='product-detail')

# views.py
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
```

## Best Practices

1. **Use Django ORM** instead of raw SQL
2. **Use forms** for validation
3. **Use class-based views** for common patterns
4. **Use Django's auth system** instead of custom
5. **Use migrations** for database changes
6. **Use Django templates** with auto-escaping
7. **Use Django's built-in security features**
8. **Follow PEP 8** style guide for Python
9. **Use virtual environments** for dependencies
10. **Use Django's testing framework**
