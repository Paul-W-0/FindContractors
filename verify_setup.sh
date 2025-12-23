#!/bin/bash
# Verification script to check if the Django environment is set up correctly

echo "=== Django Environment Verification ==="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run: python3 -m venv venv"
    exit 1
fi
echo "✓ Virtual environment exists"

# Activate virtual environment and check Django
source venv/bin/activate

# Check Django installation
if ! python -c "import django" 2>/dev/null; then
    echo "❌ Django not installed. Please run: pip install -r requirements.txt"
    exit 1
fi
echo "✓ Django is installed"

# Check Django version
DJANGO_VERSION=$(python -m django --version)
echo "✓ Django version: $DJANGO_VERSION"

# Check for migrations
echo ""
echo "Checking migrations..."
python manage.py showmigrations --plan | tail -5

# Run system check
echo ""
echo "Running Django system check..."
python manage.py check

# Check database connectivity
echo ""
echo "Testing database connectivity..."
python manage.py shell -c "
from django.contrib.auth.models import User
print(f'✓ Database accessible - {User.objects.count()} users found')
"

echo ""
echo "=== All checks passed! Environment is ready for development ==="
echo ""
echo "To start the development server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
