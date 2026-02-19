#!/usr/bin/env python3
"""
Setup script for Tourist QR Booking System
This script helps set up the Django project with MongoDB
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during {description}:")
        print(f"Command: {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("=" * 60)
    print("Tourist QR Booking System - Setup Script")
    print("=" * 60)
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: You're not in a virtual environment!")
        print("It's recommended to create and activate a virtual environment first:")
        print("python -m venv venv")
        print("venv\\Scripts\\activate  # On Windows")
        print("source venv/bin/activate  # On Linux/Mac")
        
        response = input("\nDo you want to continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing Python packages"):
        print("Failed to install requirements. Please check your internet connection and try again.")
        return
    
    # Check if MongoDB is running (optional check)
    print("\n📋 MongoDB Setup Instructions:")
    print("1. Make sure MongoDB is installed and running on your system")
    print("2. Default connection: mongodb://localhost:27017")
    print("3. Database name: tourist_booking_db")
    
    # Run migrations
    if not run_command("python manage.py makemigrations", "Creating database migrations"):
        print("Failed to create migrations.")
        return
    
    if not run_command("python manage.py migrate", "Applying database migrations"):
        print("Failed to apply migrations. Make sure MongoDB is running.")
        return
    
    # Create sample data
    if run_command("python manage.py create_sample_data", "Creating sample data"):
        print("\n🎉 Sample data created successfully!")
        print("Admin credentials:")
        print("  Username: admin")
        print("  Password: admin123")
    
    # Collect static files
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    print("\n" + "=" * 60)
    print("🚀 Setup completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Start the development server: python manage.py runserver")
    print("2. Open your browser and go to: http://127.0.0.1:8000")
    print("3. Login with admin credentials or register a new account")
    print("4. Start booking attractions and generating QR codes!")
    print("\nAdmin panel: http://127.0.0.1:8000/admin")
    print("\nEnjoy your Tourist QR Booking System! 🎫")

if __name__ == "__main__":
    main()
