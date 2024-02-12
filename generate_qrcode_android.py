import os
import qrcode
from PIL import Image

# Define the directory path in the documents folder
directory = "/storage/emulated/0/Documents/QR_Codes/"

# Ensure the directory exists, create it if not
os.makedirs(directory, exist_ok=True)

# The data you want to encode in the QR Code
data = "https://github.com/"

# Generate the QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code
image = qr.make_image(fill="black", back_color="white")
print("QR Code generated!!")

# Save the image to the specified directory
image_path = os.path.join(directory, "github.png")
image.save(image_path)
print("QR Code image saved at:", image_path)

# Open the saved image
Image.open(image_path)