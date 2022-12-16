import qrcode  
# generating a QR code using the make() function  
id= input("Enter the Studnet id:\t")
name=input("Enter the Studnet Name:\t")
qr_img = qrcode.make(f"Student id={id}\nStudnet Name={name}")  
# saving the image file  
qr_img.save("qr-img.jpg")  