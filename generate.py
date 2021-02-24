import barcode
from barcode.writer import ImageWriter
EAN = barcode.get_barcode_class('ean13')
for i in range(100000000000, 100000000005):
    ean = EAN(str(i), writer=ImageWriter())
    ean.save(str(i)+'_code128_barcode')
    print('Generate Barcode of: '+str(i))