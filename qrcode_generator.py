import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4
)

request = input('Enter the link you wish to generate: ')

qr.add_data(request)

img = qr.make_image()
img.save('qrcode.png')