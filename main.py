import os
import globales
import productos
import estadisticas

def menu_estadisticas():
    while True:
        os.system("cls")
        print("1. Producto con valor más alto")
        print("2. Producto con valor del IVA más bajo")
        print("3. Promedio del valor de los productos")
        print("4. Media geométrica del valor de los productos")

        opcion = globales.seleccionar_opcion(4)

        if opcion == 1:
            print("Producto con valor más alto")
            estadisticas.producto_mas_valor_alto()
        elif opcion == 2:
            print("Producto con valor del IVA más bajo")
            estadisticas.producto_valor_mas_bajo()
        elif opcion == 3:
            print("Promedio del valor de los productos")
            estadisticas.promedio_valor_productos()
        elif opcion == 4:
            print("Media geométrica del valor de los productos")
            estadisticas.media_geometrica()

        input()



def menu_general():
    while True:
        os.system("cls")
        print("1. Asignar montos aleatorios")
        print("2. Ver estadísticas")
        print("3. Salir del programa")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("Asignar montos aleatorios")
            productos.montos_aleatorios()
        elif opcion == 2:
            print("Ver estadisticas")
            menu_estadisticas()
        elif opcion == 3:
            return

        input()

if __name__ == "__main__":
    menu_general()