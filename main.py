import xml.etree.ElementTree as ET
from version import VERSION

print(f"FactSyst v{VERSION}")

cliente = input("Nombre del cliente: ")
producto = input("Producto: ")

cantidad = int(input("Cantidad: "))
precio = float(input("Precio: "))

total = cantidad * precio

try:
    tree = ET.parse("facturas.xml")
    root = tree.getroot()
except:
    root = ET.Element("facturas")

factura = ET.SubElement(root, "factura")

ET.SubElement(factura, "cliente").text = cliente
ET.SubElement(factura, "producto").text = producto
ET.SubElement(factura, "cantidad").text = str(cantidad)
ET.SubElement(factura, "precio").text = str(precio)
ET.SubElement(factura, "total").text = str(total)

tree = ET.ElementTree(root)
tree.write("facturas.xml")

print("Factura guardada correctamente.")