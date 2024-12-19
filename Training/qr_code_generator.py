import qrcode

url = input('Enter url to be converted to QR code: ')

img = qrcode.make(url)

img.save('MyQRCode2.png')

