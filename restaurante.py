while True:
    print("\n--- Bienvenido al sistema de pedidos del restaurante ---")
    
    # Preguntar el tipo de servicio una sola vez al iniciar
    tipo_pedido = input("¿Desea comer en el restaurante o desea llevar? (COMER/LLEVAR): ").lower()
    
    if tipo_pedido == "comer":
        print("¡Perfecto! Puede disfrutar de su comida en nuestro restaurante.")
    elif tipo_pedido == "llevar":
        print("¡Perfecto! Su pedido será preparado para llevar.")
    else:
        print("Opción no válida, por defecto se tomará como 'llevar'.")
        tipo_pedido = "llevar"

    productos_c = {
        "1": {"nombre": "Pasticho", "precio": 10.99},
        "2": {"nombre": "Pizza", "precio": 12.99},
        "3": {"nombre": "Ramen", "precio": 8.99},
        "4": {"nombre": "Pasta", "precio": 9.99},
        "5": {"nombre": "Pollo", "precio": 5.50},
        "6": {"nombre": "Milanesa", "precio": 7.99}
    }

    productos_f = {
        "1": {"nombre": "Tortas", "precio": 1.99},
        "2": {"nombre": "Quesillo", "precio": 2.50},
        "3": {"nombre": "Beso de Angel", "precio": 3.99},
        "4": {"nombre": "Tres Leches", "precio": 4.50},
        "5": {"nombre": "Pie de limón", "precio": 2.99},
        "6": {"nombre": "Flan", "precio": 3.50}
    }

    carrito = []
    
    # Bucle para agregar productos al carrito
    while True:
        print("\n--- Menu de opciones ---")
        pedido = input("Una vez finalice el pedido, escriba 'ordenar' para mostrar la factura \n¿Qué tipo de comida desea ordenar? (frio/caliente/ordenar): ").lower()
        
        if pedido == "ordenar":
            break    
        elif pedido == "frio":
            print("\n--- Menu de comida fria ---")
            for key, value in productos_f.items():
                print(f"{key}. {value['nombre']} - ${value['precio']}")

            #numero de productos que desea ordenar
            orden = input("\nIngrese el número del producto que desea ordenar: ")
            if orden in productos_f:
                producto = productos_f[orden]
                try:
                    cantidad = int(input(f"¿Cuántas porciones de '{producto['nombre']}' desea?: "))
                    if cantidad > 0:
                        # Guardamos el producto junto con su cantidad
                        item_carrito = {
                            "nombre": producto["nombre"],
                            "precio": producto["precio"],
                            "cantidad": cantidad
                        }
                        carrito.append(item_carrito)
                        print(f"¡Agregado al carrito: {cantidad}x {producto['nombre']}!")
                    else:
                        print("\nLa cantidad debe ser mayor a 0.")
                except ValueError:
                    print("\nPor favor, ingrese un número válido.")
            else:
                print("\nProducto no válido.")
                
        elif pedido == "caliente":
            print("\n--- Menu de comida caliente ---")
            for key, value in productos_c.items():
                print(f"{key}. {value['nombre']} - ${value['precio']}")
                
            orden = input("\nIngrese el número del producto que desea ordenar: ")
            if orden in productos_c:
                producto = productos_c[orden]
                try:
                    cantidad = int(input(f"¿Cuántas porciones de '{producto['nombre']}' desea?: "))
                    if cantidad > 0:
                        # producto mas cantidad
                        item_carrito = {
                            "nombre": producto["nombre"],
                            "precio": producto["precio"],
                            "cantidad": cantidad
                        }
                        carrito.append(item_carrito)
                        print(f"¡Agregado al carrito: {cantidad}x {producto['nombre']}!")
                    else:
                        print("\nLa cantidad debe ser mayor a 0.")
                except ValueError:
                    print("\nPor favor, ingrese un número válido.")
            else:
                print("\nProducto no válido.")
        else:
            print("\nOpción no válida. Escriba 'frio', 'caliente' o 'ordenar'.")

        if carrito:
            print("\n--- Carrito de compras actual ---")
            for item in carrito:
                subtotal_item = item['precio'] * item['cantidad']
                print(f"- {item['cantidad']}x {item['nombre']}: ${subtotal_item:.2f}")

    # Validación por si el carrito está vacío
    if not carrito:
        print("\nNo ha agregado ningún producto a su pedido.")
    else:
        # Factura final calculando precios por cantidades
        print("\n" + "="*30)
        print("          FACTURA FINAL")
        print(f"tipo:  {tipo_pedido.upper()}")
        print("="*30)

        total = 0
        for item in carrito:
            subtotal_item = item['precio'] * item['cantidad']
            print(f"- {item['cantidad']}x {item['nombre']}: ${subtotal_item:.2f}")
            total += subtotal_item

        print("="*30)
        print(f"Total a pagar: ${total:.2f}")
        print("¡Gracias por su compra!")

    # Preguntar si desea realizar otro pedido general o salir
    continuar = input("\n¿Desea realizar otro pedido? (si/no): ").lower()
    if continuar == "no":
        print("¡Gracias por visitar nuestro restaurante! ¡Hasta pronto!")
        break
    elif continuar == "si":
        print("¡Perfecto! Iniciando nuevo sistema...\n")
    else:
        print("Opción no reconocida, saliendo del sistema...")
        break