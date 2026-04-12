#!/bin/bash

# Ashesi Market Django Setup Script

echo "=== Ashesi Market Django Setup ==="
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Copy environment file
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please edit .env with your database credentials"
fi

# Create media directories
echo "Creating media directories..."
mkdir -p media/products
mkdir -p media/id_images

# Run migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Load initial data
echo "Loading categories..."
python manage.py loaddata categories

# Create superuser
echo ""
echo "Create a superuser account for admin access:"
python manage.py createsuperuser

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "To start the development server:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://localhost:8000"
echo "Admin panel: http://localhost:8000/admin"
