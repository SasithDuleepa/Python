import barcode
from barcode.writer import ImageWriter
print(barcode.PROVIDED_BARCODES)
#type = input("enter barcode type : ")
number = '978442511368'
barcode_format = barcode.get_barcode_class('isbn')
my_barcode = barcode_format(number, writer=ImageWriter())

my_barcode.save(number+"_barcode")
