#!/usr/bin/env python3
"""
Generate test payment QR codes for scanning
"""
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generate_payment_qr_codes():
    # Different payment QR codes to test
    payment_qrs = [
        {
            'name': 'PayPal Payment',
            'data': 'https://paypal.me/touristbooking/25.00',
            'filename': 'paypal_payment_qr.png',
            'color': '#0070ba'
        },
        {
            'name': 'Venmo Payment',
            'data': 'venmo://paycharge?txn=pay&recipients=touristbooking&amount=25&note=Tourist%20Booking',
            'filename': 'venmo_payment_qr.png',
            'color': '#3d95ce'
        },
        {
            'name': 'Bitcoin Payment',
            'data': 'bitcoin:1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa?amount=0.0005&label=Tourist%20Booking',
            'filename': 'bitcoin_payment_qr.png',
            'color': '#f7931a'
        },
        {
            'name': 'UPI Payment',
            'data': 'upi://pay?pa=touristbooking@paytm&pn=Tourist%20Booking&am=25.00&cu=USD',
            'filename': 'upi_payment_qr.png',
            'color': '#00bcd4'
        },
        {
            'name': 'Generic Digital Wallet',
            'data': 'WALLET_PAY:touristbooking:25.00:USD:Tourist_Booking_Payment',
            'filename': 'wallet_payment_qr.png',
            'color': '#4caf50'
        }
    ]
    
    for payment in payment_qrs:
        generate_single_payment_qr(payment)
    
    print("✅ All payment QR codes generated successfully!")
    print("📱 Test these QR codes with the payment scanner:")
    for payment in payment_qrs:
        print(f"   - {payment['name']}: /static/images/{payment['filename']}")

def generate_single_payment_qr(payment_info):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )
    qr.add_data(payment_info['data'])
    qr.make(fit=True)

    # Create QR code image with custom color
    qr_img = qr.make_image(fill_color=payment_info['color'], back_color="white")
    
    # Create a larger image with text
    final_img = Image.new('RGB', (350, 450), 'white')
    
    # Paste QR code in the center
    qr_img = qr_img.resize((250, 250))
    final_img.paste(qr_img, (50, 80))
    
    # Add text
    draw = ImageDraw.Draw(final_img)
    
    try:
        # Try to use a nice font
        font_title = ImageFont.truetype("arial.ttf", 20)
        font_text = ImageFont.truetype("arial.ttf", 14)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        # Fallback to default font
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Add title
    title = payment_info['name']
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((350 - title_width) // 2, 20), title, fill=payment_info['color'], font=font_title)
    
    # Add amount
    amount = "$25.00"
    amount_bbox = draw.textbbox((0, 0), amount, font=font_title)
    amount_width = amount_bbox[2] - amount_bbox[0]
    draw.text(((350 - amount_width) // 2, 45), amount, fill="black", font=font_title)
    
    # Add instruction
    instruction = "Scan to pay with " + payment_info['name'].split()[0]
    inst_bbox = draw.textbbox((0, 0), instruction, font=font_text)
    inst_width = inst_bbox[2] - inst_bbox[0]
    draw.text(((350 - inst_width) // 2, 350), instruction, fill="black", font=font_text)
    
    # Add test note
    test_note = "TEST QR CODE - For Demo Only"
    test_bbox = draw.textbbox((0, 0), test_note, font=font_small)
    test_width = test_bbox[2] - test_bbox[0]
    draw.text(((350 - test_width) // 2, 380), test_note, fill="gray", font=font_small)
    
    # Add data preview (truncated)
    data_preview = payment_info['data'][:40] + "..." if len(payment_info['data']) > 40 else payment_info['data']
    data_bbox = draw.textbbox((0, 0), data_preview, font=font_small)
    data_width = data_bbox[2] - data_bbox[0]
    draw.text(((350 - data_width) // 2, 400), data_preview, fill="lightgray", font=font_small)
    
    # Save the image
    output_path = os.path.join(os.path.dirname(__file__), 'static', 'images', payment_info['filename'])
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_img.save(output_path)
    
    print(f"✅ Generated: {payment_info['name']} QR code")

if __name__ == "__main__":
    generate_payment_qr_codes()
