import os
import math
import globales

def producto_mas_valor_alto():
    todos_los_productos = globales.leer_archivo_json('productos.json')
    productos_ordenados = sorted(todos_los_productos, key=lambda x: x['valor'],reverse=True )

    print("| Nombre producto | Valor")
    for valor in productos_ordenados[:1]:
        for productos in todos_los_productos:
            if productos['nombre'] == valor['nombre']:
                nombre_producto = "f{productos['nombre']}"

        print(f"|{nombre_producto['nombre']} | {valor['valor']}")


def producto_valor_mas_bajo():
    todos_los_productos = globales.leer_archivo_json('productos.json')
    productos_ordenados = sorted(todos_los_productos, key=lambda x: x['valor'],reverse=False)

    print("| Nombre producto | Valor")
    for valor in productos_ordenados[:1]:
        for productos in todos_los_productos:
            if productos['nombre'] == valor['nombre']:
                nombre_producto = "f{productos['nombre']}"

        print(f"|{nombre_producto['nombre']} | {valor['valor']}")




def promedio_valor_productos():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    suma_productos = 0
    cant_productos = 0

    for productos in todos_los_productos:
        suma_productos += productos['valor']
        cant_productos += 1

        promedio_valor = suma_productos/cant_productos

    print(f"El promedio del valor de los productos es ${int(promedio_valor)}")






def media_geometrica(): 
    todos_los_productos = globales.leer_archivo_json('productos.json')

    suma_productos = 0
    cant_productos = 0

    for productos in todos_los_productos:
        suma_productos += math.log(productos['valor'])
        cant_productos += 1

        promedio_valor = math.exp(suma_productos/cant_productos)

    print(f"La media geometrica es ${int(promedio_valor)}")