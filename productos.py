import random
import globales

def montos_aleatorios():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    productos = [
        "Café Americano",
        "Té Chai",
        "Croissant",
        "Jugo Naranja",
        "Panini de Pavo y Queso",
        "Pastel de Zanahoria",
        "Espresso Doble",
        "Batido de Frutas",
        "Muffin",
        "Ensalada",
        "Chocolate Caliente",
        "Tarta de Frambuesa",
        "Sándwich de Huevo",
        "Galletas de Avena",
        "Frappé de Caramelo"
    ]

    for i in range(15):
        lista = len(todos_los_productos) % len(productos)
        nombre = productos[lista]
        valor = random.randint(200, 1000) *0.1
        iva = valor * 19 /100

        nuevo_producto = {
            "nombre":nombre,
            "valor":valor,
            "iva": iva
        }

        todos_los_productos.append(nuevo_producto)
    globales.guardar_archivo_json('productos.json', todos_los_productos)
