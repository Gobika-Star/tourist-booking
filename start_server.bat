@echo off
echo Starting Tourist QR Booking System...
echo.

echo Installing Django...
pip install Django==4.2.7

echo Installing QR Code library...
pip install qrcode[pil]==7.4.2

echo Installing Pillow...
pip install Pillow==10.2.0

echo Installing Crispy Forms...
pip install django-crispy-forms==2.1
pip install crispy-bootstrap4==2024.1

echo.
echo Creating migrations...
python manage.py makemigrations

echo.
echo Applying migrations...
python manage.py migrate

echo.
echo Creating superuser (if needed)...
echo from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None | python manage.py shell

echo.
echo Starting development server...
echo Open your browser and go to: http://127.0.0.1:8000
echo Admin login: admin / admin123
echo.
python manage.py runserver
