# Tourist QR Booking System

A comprehensive Django web application with MongoDB integration for tourist attraction bookings with QR code generation and validation.

## 🌟 Features

### Core Features
- **User Registration & Authentication**: Secure user accounts with profile management
- **Tourist Attraction Management**: Browse and search attractions by category, location, and price
- **Booking System**: Book tickets with date, time, and visitor count selection
- **QR Code Generation**: Automatic unique QR code creation for each booking
- **QR Code Validation**: Real-time scanning and validation system for staff
- **Email Notifications**: Booking confirmations and QR code delivery
- **Admin Dashboard**: Comprehensive management interface

### Advanced Features
- **Booking History**: Complete booking management and tracking
- **QR Code Expiration**: Time-based validation with automatic expiry
- **Scan Logging**: Detailed logs of all QR code scans for analytics
- **Responsive Design**: Mobile-friendly interface with Bootstrap
- **Search & Filter**: Advanced filtering for attractions
- **Security**: Unique QR codes with anti-fraud measures

## 🛠️ Technology Stack

- **Backend**: Django 5.2, Python 3.8+
- **Database**: MongoDB with djongo ORM
- **QR Code**: qrcode library with PIL
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Authentication**: Django built-in authentication
- **Forms**: Django Crispy Forms with Bootstrap 4

## 📋 Prerequisites

- Python 3.8 or higher
- MongoDB 4.0 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd tourist_qr_project
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install MongoDB
Download and install MongoDB from [official website](https://www.mongodb.com/try/download/community)

Start MongoDB service:
```bash
# On Windows
net start MongoDB

# On Linux/Mac
sudo systemctl start mongod
```

### 4. Quick Setup (Recommended)
```bash
python setup.py
```

### 5. Manual Setup (Alternative)
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create sample data
python manage.py create_sample_data

# Collect static files
python manage.py collectstatic

# Start development server
python manage.py runserver
```

## 🎯 Usage

### 1. Start the Application
```bash
python manage.py runserver
```

### 2. Access the Application
- **Main Site**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin

### 3. Default Admin Credentials
- **Username**: admin
- **Password**: admin123

### 4. User Journey
1. **Register/Login**: Create account or login
2. **Browse Attractions**: Explore available tourist attractions
3. **Make Booking**: Select date, time, and number of visitors
4. **Get QR Code**: Receive unique QR code instantly
5. **Visit Attraction**: Present QR code for entry validation

## 📱 Key Pages

- **Home**: Featured attractions and system overview
- **Attractions**: Browse and search all attractions
- **Booking**: Make new bookings
- **Dashboard**: User profile and booking history
- **QR Scanner**: Staff interface for validating QR codes
- **Admin**: Complete system management

## 🔧 Configuration

### Database Settings
```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'tourist_booking_db',
        'CLIENT': {
            'host': 'mongodb://localhost:27017',
        }
    }
}
```

### QR Code Settings
```python
QR_CODE_EXPIRY_HOURS = 24  # QR codes expire after 24 hours
QR_CODE_SIZE = 10
QR_CODE_BORDER = 4
```

### Email Configuration
Update settings.py for production email:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## 🗂️ Project Structure

```
tourist_qr_project/
├── qrapp/                  # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin configuration
│   └── management/        # Custom commands
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── qrapp/            # App templates
│   └── registration/     # Auth templates
├── static/               # Static files
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript
│   └── images/          # Images
├── media/               # User uploads
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## 🔒 Security Features

- **Unique QR Codes**: Each booking generates a unique QR code
- **Time-based Expiration**: QR codes expire automatically
- **Usage Tracking**: Prevents QR code reuse
- **Scan Logging**: Complete audit trail
- **User Authentication**: Secure login system
- **CSRF Protection**: Django built-in security

## 🧪 Testing

Run tests:
```bash
python manage.py test
```

## 📈 Future Enhancements

- [ ] Payment gateway integration
- [ ] Mobile app development
- [ ] Real-time notifications
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] API development for third-party integration
- [ ] Capacity management system
- [ ] Weather integration for outdoor attractions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team

## 🙏 Acknowledgments

- Django community for the excellent framework
- MongoDB for the flexible database solution
- Bootstrap for the responsive UI components
- QR code library contributors

---

**Happy Booking! 🎫✨**
