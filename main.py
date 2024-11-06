import qrcode
import qrcode.constants

def create_qr_code(link, output_file="qr_code.png"):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(link)
        qr.make(fit=True)
        
        img = qr.make_image(fill="black", back_color="white")
        
        img.save(output_file)
        print(f"QR Code saved as {output_file}")
    except Exception as e:
        print(f"Error: {e}")

create_qr_code("YOUR_LINK_HERE")