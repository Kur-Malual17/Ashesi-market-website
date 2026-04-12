# Quick Start Guide

Get Ashesi Market Django running in 5 minutes!

## Prerequisites

- Python 3.9 or higher
- MySQL 8.0 or higher
- pip (Python package manager)

## Step 1: Clone/Navigate to Project

```bash
cd ashesi_market_django
```

## Step 2: Create Virtual Environment

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Setup Database

Create MySQL database:
```sql
CREATE DATABASE ashesi_market CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Step 5: Configure Environment

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` with your database credentials:
```
DB_NAME=ashesi_market
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
```

## Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 7: Load Initial Data

```bash
python manage.py loaddata categories
```

## Step 8: Create Admin User

```bash
python manage.py createsuperuser
```

Follow prompts to create admin account.

## Step 9: Run Development Server

```bash
python manage.py runserver
```

## Access the Application

- **Homepage**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **API Root**: http://localhost:8000/api/

## Quick Test

1. Visit http://localhost:8000
2. Click "Register" to create an account
3. Login with your credentials
4. Click "Sell" to list a product
5. Browse products and add to cart

## Automated Setup (Optional)

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```bash
setup.bat
```

## Common Issues

### MySQL Connection Error
- Verify MySQL is running
- Check credentials in `.env`
- Ensure database exists

### Import Error
- Activate virtual environment
- Reinstall requirements: `pip install -r requirements.txt`

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

## Next Steps

- Explore the admin panel
- Create test products
- Test the shopping cart
- Review API documentation
- Customize templates and styles

## Development Tips

- Use `python manage.py shell` for interactive testing
- Check logs for errors
- Use Django Debug Toolbar for optimization
- Run tests: `python manage.py test`

## Production Deployment

For production deployment, see Django deployment documentation:
https://docs.djangoproject.com/en/4.2/howto/deployment/

Remember to:
- Set `DEBUG=False`
- Use strong `SECRET_KEY`
- Configure proper database
- Setup static file serving
- Use HTTPS
- Configure allowed hosts
