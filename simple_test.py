#!/usr/bin/env python
"""
Simple test to check if everything is working
"""
import sys
import os

print("🔍 Checking Django setup...")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")

# Check if manage.py exists
if os.path.exists('manage.py'):
    print("✅ manage.py found")
else:
    print("❌ manage.py not found - you're in the wrong directory")
    print("Please navigate to the tourist_qr_project folder")
    sys.exit(1)

# Check if Django is installed
try:
    import django
    print(f"✅ Django {django.get_version()} is installed")
except ImportError:
    print("❌ Django not installed")
    print("Run: pip install Django==4.2.7")
    sys.exit(1)

# Check if we can import settings
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourist_qr_project.settings')
    django.setup()
    print("✅ Django settings loaded successfully")
except Exception as e:
    print(f"❌ Django setup failed: {e}")
    sys.exit(1)

print("\n🎉 Everything looks good!")
print("\nNext steps:")
print("1. Run: python manage.py migrate")
print("2. Run: python manage.py runserver")
print("3. Open: http://127.0.0.1:8000")
