import qrcode
name = input("enter your name:")
age = input("enter your age:")
ed_class = input("enter your class:")
section = input("enter your section:")
data = {'name:name', 'age:age', 'class:class', 'section:section',}
qr = qrcode .QRCode(version=5,box_size=5,border=2)
qr.add_data(data)
qr.make(fit=True)
            

img = qr.make_image(fill_color="green",back_color='black')
img.save("Hello.png")
img.show()