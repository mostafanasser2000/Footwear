# FootWear

👟️ Footwear a Django-based e-commerce project aims to provide shoe enthusiasts the ultimate online shopping experience, combining a powerful backend with a beautiful and user-friendly frontend. 
## Video Preview
[![FootWear Preivew](https://img.youtube.com/vi/DEevoUPlKTU/0.jpg)](https://www.youtube.com/watch?v=DEevoUPlKTU)

## Features

- User Authentication and social authentication
- Product Management
- Product Browsing and Search
- Shopping Cart Management
- Checkout and Order Processing
- Responsive Design

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ecommerce-website.git
cd ecommerce-website
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3.Install Dependencies

```bash
pip install -r requirements.txt
```

### 4.Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

now access admin dashboard to create products website at `http://127.0.0.1:8000/admin`

## Further Improvement

- improve dashboard for admins
- allow online payments through stripe
- add copouts and discounts for products
