import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/@juiceearthhh7225"
url = pyqrcode.create(s)
url.svg("myyoutube.svg", scale=8)