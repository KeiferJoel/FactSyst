import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET


VERSION = "1.1.0"
CREATOR = "Joel Pichardo"
ITBIS = 0.18


# FUNCIONES
def calcular_total():
    try:
        cantidad = int(entry_cantidad.get())
        precio = float(entry_precio.get())

        subtotal = cantidad * precio
        impuesto = subtotal * ITBIS
        total = subtotal + impuesto

        label_total.config(
            text=f"Total: RD$ {total:.2f}"
        )

        return total

    except ValueError:
        messagebox.showerror(
            "Error",
            "Cantidad y precio deben ser números."
        )
        return None


def guardar_factura():

    cliente = entry_cliente.get().strip()
    producto = entry_producto.get().strip()

    if not cliente or not producto:
        messagebox.showwarning(
            "Campos vacíos",
            "Debe completar todos los campos."
        )
        return

    total = calcular_total()

    if total is None:
        return

    cantidad = entry_cantidad.get()
    precio = entry_precio.get()

    # Intentar abrir el XML existente
    try:
        tree = ET.parse("facturas.xml")
        root = tree.getroot()

    except FileNotFoundError:
        root = ET.Element("facturas")

    # Crear la factura
    factura = ET.SubElement(root, "factura")

    ET.SubElement(factura, "cliente").text = cliente
    ET.SubElement(factura, "producto").text = producto
    ET.SubElement(factura, "cantidad").text = cantidad
    ET.SubElement(factura, "precio").text = precio
    ET.SubElement(factura, "total").text = f"{total:.2f}"

    # Guardar el XML

    ET.indent(tree, space="    ", level=0)
    tree = ET.ElementTree(root)

    tree.write(
        "facturas.xml",
        encoding="utf-8",
        xml_declaration=True
    )

    messagebox.showinfo(
        "Éxito",
        "Factura guardada correctamente."
    )

    limpiar_campos()


def limpiar_campos():
    entry_cliente.delete(0, tk.END)
    entry_producto.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

    label_total.config(
        text="Total: RD$ 0.00"
    )


# =====================
# VENTANA PRINCIPAL
# =====================

ventana = tk.Tk()

ventana.title(
    f"Sistema de Facturación XML v{VERSION}"
)

ventana.geometry("400x420")
ventana.resizable(False, False)


# =====================
# TÍTULO
# =====================

titulo = tk.Label(
    ventana,
    text="Sistema de Facturación XML",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=10)


autor = tk.Label(
    ventana,
    text=f"Developed by {CREATOR}"
)

autor.pack(pady=5)



# CLIENTE

tk.Label(
    ventana,
    text="Cliente"
).pack()

entry_cliente = tk.Entry(
    ventana,
    width=40
)

entry_cliente.pack()



# PRODUCTO

tk.Label(
    ventana,
    text="Producto"
).pack()

entry_producto = tk.Entry(
    ventana,
    width=40
)

entry_producto.pack()



# CANTIDAD

tk.Label(
    ventana,
    text="Cantidad"
).pack()

entry_cantidad = tk.Entry(
    ventana,
    width=40
)

entry_cantidad.pack()


# PRECIO

tk.Label(
    ventana,
    text="Precio"
).pack()

entry_precio = tk.Entry(
    ventana,
    width=40
)

entry_precio.pack()


# TOTAL

label_total = tk.Label(
    ventana,
    text="Total: RD$ 0.00",
    font=("Arial", 12, "bold")
)

label_total.pack(pady=15)


# BOTONES

btn_calcular = tk.Button(
    ventana,
    text="Calcular Total",
    width=20,
    command=calcular_total
)

btn_calcular.pack(pady=5)


btn_guardar = tk.Button(
    ventana,
    text="Guardar Factura",
    width=20,
    command=guardar_factura
)

btn_guardar.pack(pady=5)


# INICIAR APP

ventana.mainloop()