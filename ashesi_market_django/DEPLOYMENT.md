# Deployment Guide

Guide for deploying Ashesi Market Django to production.

## Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Database migrations up to date
- [ ] Static files collected
- [ ] Media files backed up
- [ ] Environment variables configured
- [ ] Security settings reviewed
- [ ] SSL certificate obtained
- [ ] Domain configured

## Production Settings

### 1. Environment Variables

Create `.env` for production:

```bash
SECRET_KEY=your-very-long-random-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DB_NAME=ashesi_market_prod
DB_USER=ashesi_db_user
DB_PASSWORD=strong-database-password
DB_HOST=localhost
DB_PORT=3306

BASE_URL=https://yourdomain.com
```

### 2. Security Settings

Update `settings.py` for production:

```python
# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

## Deployment Options

### Option 1: Traditional Server (Ubuntu + Nginx + Gunicorn)

#### Step 1: Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3-pip python3-venv nginx mysql-server -y

# Install Gunicorn
pip install gunicorn
```

#### Step 2: Clone Project

```bash
cd /var/www
sudo git clone <your-repo> ashesi_market
cd ashesi_market
```

#### Step 3: Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Step 4: Configure Database

```bash
sudo mysql
CREATE DATABASE ashesi_market_prod CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'ashesi_user'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON ashesi_market_prod.* TO 'ashesi_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

#### Step 5: Run Migrations

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata categories
python manage.py createsuperuser
```

#### Step 6: Configure Gunicorn

Create `/etc/systemd/system/ashesi_market.service`:

```ini
[Unit]
Description=Ashesi Market Gunicorn
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/ashesi_market
Environment="PATH=/var/www/ashesi_market/venv/bin"
ExecStart=/var/www/ashesi_market/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/ashesi_market/ashesi_market.sock \
    ashesi_market.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start service:
```bash
sudo systemctl start ashesi_market
sudo systemctl enable ashesi_market
```

#### Step 7: Configure Nginx

Create `/etc/nginx/sites-available/ashesi_market`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /var/www/ashesi_market/staticfiles/;
    }
    
    location /media/ {
        alias /var/www/ashesi_market/media/;
    }
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/ashesi_market/ashesi_market.sock;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/ashesi_market /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 8: SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### Option 2: Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ashesi_market.wsgi:application"]
```

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: ashesi_market
      MYSQL_ROOT_PASSWORD: rootpassword
    volumes:
      - mysql_data:/var/lib/mysql
  
  web:
    build: .
    command: gunicorn ashesi_market.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

volumes:
  mysql_data:
  static_volume:
  media_volume:
```

Deploy:
```bash
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Option 3: Platform as a Service (Heroku, Railway, etc.)

#### Heroku Deployment

1. Install Heroku CLI
2. Create `Procfile`:
```
web: gunicorn ashesi_market.wsgi
release: python manage.py migrate
```

3. Create `runtime.txt`:
```
python-3.11.0
```

4. Deploy:
```bash
heroku create ashesi-market
heroku addons:create cleardb:ignite
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
git push heroku main
heroku run python manage.py createsuperuser
```

## Post-Deployment

### 1. Monitoring

Setup monitoring with:
- Sentry for error tracking
- New Relic for performance
- Uptime Robot for availability

### 2. Backups

Setup automated backups:

```bash
# Database backup script
#!/bin/bash
mysqldump -u user -p ashesi_market_prod > backup_$(date +%Y%m%d).sql
```

Add to crontab:
```bash
0 2 * * * /path/to/backup.sh
```

### 3. Updates

Update process:

```bash
cd /var/www/ashesi_market
git pull
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart ashesi_market
```

## Performance Optimization

### 1. Database

- Add indexes to frequently queried fields
- Use `select_related()` and `prefetch_related()`
- Enable query caching

### 2. Caching

Install Redis:
```bash
pip install django-redis
```

Configure in `settings.py`:
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### 3. Static Files

Use CDN for static files:
- Cloudflare
- AWS CloudFront
- DigitalOcean Spaces

## Troubleshooting

### Common Issues

1. **502 Bad Gateway**
   - Check Gunicorn is running
   - Check socket file permissions
   - Review Nginx error logs

2. **Static files not loading**
   - Run `collectstatic`
   - Check Nginx static file configuration
   - Verify file permissions

3. **Database connection errors**
   - Verify database credentials
   - Check MySQL is running
   - Test connection manually

### Logs

View logs:
```bash
# Gunicorn logs
sudo journalctl -u ashesi_market

# Nginx logs
sudo tail -f /var/log/nginx/error.log

# Django logs
tail -f /var/www/ashesi_market/logs/django.log
```

## Security Checklist

- [ ] DEBUG=False in production
- [ ] Strong SECRET_KEY
- [ ] HTTPS enabled
- [ ] Firewall configured
- [ ] Database password strong
- [ ] Regular security updates
- [ ] Backup strategy in place
- [ ] Error monitoring setup
- [ ] Rate limiting configured
- [ ] CORS properly configured

## Support

For deployment issues:
- Django deployment docs: https://docs.djangoproject.com/en/4.2/howto/deployment/
- Gunicorn docs: https://docs.gunicorn.org/
- Nginx docs: https://nginx.org/en/docs/
