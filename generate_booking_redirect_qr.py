#!/usr/bin/env python3
"""
Generate QR code that redirects to booking page
"""
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generate_booking_redirect_qr():
    # QR code data - URL to booking page
    booking_url = "http://127.0.0.1:8000/booking/"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(booking_url)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill_color="#007bff", back_color="white")
    
    # Create a larger image with text
    final_img = Image.new('RGB', (400, 500), 'white')
    
    # Paste QR code in the center
    qr_img = qr_img.resize((300, 300))
    final_img.paste(qr_img, (50, 50))
    
    # Add text
    draw = ImageDraw.Draw(final_img)
    
    try:
        # Try to use a nice font
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_text = ImageFont.truetype("arial.ttf", 16)
        font_small = ImageFont.truetype("arial.ttf", 14)
    except:
        # Fallback to default font
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Add title
    title = "Start Booking"
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((400 - title_width) // 2, 10), title, fill="#007bff", font=font_title)
    
    # Add instruction
    instruction = "Scan to go to booking page"
    inst_bbox = draw.textbbox((0, 0), instruction, font=font_text)
    inst_width = inst_bbox[2] - inst_bbox[0]
    draw.text(((400 - inst_width) // 2, 370), instruction, fill="black", font=font_text)
    
    # Add URL info
    url_info = "Redirects to: /booking/"
    url_bbox = draw.textbbox((0, 0), url_info, font=font_small)
    url_width = url_bbox[2] - url_bbox[0]
    draw.text(((400 - url_width) // 2, 400), url_info, fill="gray", font=font_small)
    
    # Add tourist info
    tourist_info = "Tourist Booking System"
    tourist_bbox = draw.textbbox((0, 0), tourist_info, font=font_small)
    tourist_width = tourist_bbox[2] - tourist_bbox[0]
    draw.text(((400 - tourist_width) // 2, 430), tourist_info, fill="#007bff", font=font_small)
    
    # Save the image
    output_path = os.path.join(os.path.dirname(__file__), 'static', 'images', 'booking_redirect_qr.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_img.save(output_path)
    
    print(f"✅ Booking redirect QR code generated: {output_path}")
    print(f"🔗 QR code URL: {booking_url}")
    print("📱 This QR code will redirect users to the booking page")

if __name__ == "__main__":
    generate_booking_redirect_qr()
