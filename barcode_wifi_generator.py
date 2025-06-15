import wifi_qrcode_generator.generator

from PIL import Image

ssid = "SFSOFTWARES TECH"
password = "SFSOFTWARES@3366"
security = "WPA"

from wifi_qrcode_generator import wifi_qrcode
qr = wifi_qrcode(ssid, False, security, password)

qr.make_image().save("tech_wifi.png")
Image.open("tech_wifi.png").show()