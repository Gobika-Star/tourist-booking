#!/usr/bin/env python
"""
Simple test script to check if Django is working
"""
import os
import sys

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourist_qr_project.settings')

try:
    import django
    print(f"✅ Django version: {django.get_version()}")
    
    django.setup()
    print("✅ Django setup successful")
    
    from django.contrib.auth.models import User
    print("✅ Django models imported successfully")
    
    from qrapp.models import TouristAttraction
    print("✅ Custom models imported successfully")
    
    print("\n🎉 Django is working correctly!")
    print("\nNext steps:")
    print("1. Run: python manage.py makemigrations")
    print("2. Run: python manage.py migrate")
    print("3. Run: python manage.py createsuperuser")
    print("4. Run: python manage.py runserver")
    print("5. Open: http://127.0.0.1:8000")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install Django: pip install Django==4.2.7")
except Exception as e:
    print(f"❌ Error: {e}")
    print("Please check your Django installation and settings")
