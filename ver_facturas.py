import xml.etree.ElementTree as ET

tree = ET.parse("facturas.xml")
root = tree.getroot()

print("FACTURAS REGISTRADAS")

for factura in root.findall("factura"):
    print("-------------------")
    print("Cliente:", factura.find("cliente").text)
    print("Producto:", factura.find("producto").text)
    print("Cantidad:", factura.find("cantidad").text)
    print("Precio:", factura.find("precio").text)
    print("Total:", factura.find("total").text)