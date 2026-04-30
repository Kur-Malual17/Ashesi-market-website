# CI/CD Workflows

This directory contains GitHub Actions workflows for continuous integration and deployment.

## Workflows

### 1. Backend CI/CD (`backend-ci.yml`)
**Triggers:** Push or PR to `main` or `develop` branches with changes in `ashesi_market_django/`

**Jobs:**
- **Test**
  - Sets up Python 3.11 and PostgreSQL
  - Installs dependencies
  - Runs linting (flake8)
  - Checks code formatting (black)
  - Checks import sorting (isort)
  - Runs Django tests
  - Checks for missing migrations
  
- **Deploy**
  - Runs only on push to `main`
  - Railway auto-deploys from GitHub (no action needed)

### 2. Frontend CI/CD (`frontend-ci.yml`)
**Triggers:** Push or PR to `main` or `develop` branches with changes in `ashesi_market_frontend/`

**Jobs:**
- **Lint**
  - Validates HTML files
  - Checks JavaScript syntax
  - Validates CSS files
  
- **Security**
  - Scans for hardcoded secrets
  - Checks for potential security issues
  
- **Deploy**
  - Runs only on push to `main`
  - Vercel auto-deploys from GitHub (no action needed)

### 3. Full Stack CI/CD (`full-stack-ci.yml`)
**Triggers:** Push or PR to `main` branch

**Jobs:**
- **Check Changes**
  - Detects which parts of the codebase changed
  
- **Integration Test**
  - Starts Django server
  - Tests API endpoints
  
- **Deploy Status**
  - Shows deployment summary
  - Provides links to deployment dashboards

## Setup Instructions

### Prerequisites
1. GitHub repository connected to Railway and Vercel
2. Railway and Vercel configured for auto-deployment

### Railway Setup
1. Go to Railway dashboard
2. Connect your GitHub repository
3. Enable auto-deploy from `main` branch
4. Set environment variables in Railway dashboard

### Vercel Setup
1. Go to Vercel dashboard
2. Import your GitHub repository
3. Set root directory to `ashesi_market_frontend`
4. Enable auto-deploy from `main` branch

### GitHub Secrets (Optional)
If you want to add deployment notifications or custom deployment logic:

1. Go to GitHub repository → Settings → Secrets and variables → Actions
2. Add secrets:
   - `RAILWAY_TOKEN` (optional, for custom deployment)
   - `VERCEL_TOKEN` (optional, for custom deployment)

## Workflow Status Badges

Add these to your README.md:

```markdown
![Backend CI](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Backend%20CI%2FCD/badge.svg)
![Frontend CI](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Frontend%20CI%2FCD/badge.svg)
![Full Stack CI](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Full%20Stack%20CI%2FCD/badge.svg)
```

## Local Development

### Run Backend Tests Locally
```bash
cd ashesi_market_django
python -m pip install -r requirements.txt
python -m pip install flake8 black isort
python manage.py test
```

### Run Linting Locally
```bash
cd ashesi_market_django
flake8 .
black --check .
isort --check-only .
```

### Auto-format Code
```bash
cd ashesi_market_django
black .
isort .
```

## Troubleshooting

### Tests Failing
- Check the Actions tab in GitHub for detailed logs
- Run tests locally to reproduce the issue
- Ensure all environment variables are set correctly

### Deployment Not Triggering
- Verify Railway/Vercel is connected to GitHub
- Check that auto-deploy is enabled
- Ensure changes are pushed to the `main` branch

### Linting Errors
- Run `black .` and `isort .` to auto-fix formatting
- Fix flake8 errors manually
- Some errors can be ignored by updating `.flake8` config

## Best Practices

1. **Always create a PR** for changes (don't push directly to main)
2. **Wait for CI to pass** before merging PRs
3. **Review test results** in the Actions tab
4. **Keep dependencies updated** regularly
5. **Monitor deployment logs** in Railway and Vercel dashboards

## Continuous Improvement

To improve the CI/CD pipeline:
- Add more comprehensive tests
- Add code coverage reporting
- Add performance testing
- Add automated security scanning
- Add automated dependency updates (Dependabot)
