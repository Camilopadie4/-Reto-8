class Menu:  # Clase padre. Sus hijos(Bebida, aperitivo, plato_principal...) tienen atributos adicionales como tamaño o cantidad
    def __init__(self, nombre: str, precio: float):
        self.nombre= nombre
        self.precio= precio 
    def calcular_precio(self):
        return self.precio
    def __str__(self):
        return f"{self.nombre} : ${self.precio}"

class Bebidas(Menu):
    def __init__(self, nombre: str, precio: float, tamaño: str):
        super().__init__(nombre, precio)
        self.tamaño= tamaño
    def __str__(self):
        return f"{self.nombre} {self.tamaño} : ${self.precio}"
    
class Aperitivo(Menu):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio)
    def __str__(self):
        return f"{self.nombre} : ${self.precio}"
    
class Plato_principal(Menu):
    def __init__(self, nombre: str, precio: float, cantidad: str):
        super().__init__(nombre, precio)
        self.cantidad= cantidad
    def __str__(self):
        return f"{self.nombre} Porc:{self.cantidad} = ${self.precio}"

class Orden:   # Guarda los elementos(productos) que el usuario ha pedido y hace otras operaciones 
    def __init__(self):
        self.elementos= []
        
    def agregar_elemento(self, elemento: Menu):
        self.elementos.append(elemento)

    def calcular_factura(self):
        return sum(elemento.calcular_precio() for elemento in self.elementos)
    
    def hacer_descuento(self):
        platos_principales = sum(1 for elemento in self.elementos if isinstance(elemento, Plato_principal))
        if platos_principales >= 3:
            return self.calcular_total() * 0.9 
        return self.calcular_factura()
    
    def mostrar_pedido(self):
        print("Orden y resumen de pago:")
        for elemento in self.elementos:
            print(f"{elemento}")
        print(f"Total:${self.calcular_factura()}")
        print(f"Total con descuento: ${self.hacer_descuento()}")

    def __iter__(self): # Modificacion para que sea iterable 
        return iteracion(self.elementos)

class iteracion:    # Nueva clase 
    def __init__(self, elementos):
        self.elementos= elementos
        self.indicador= 0   # Para saber donde va la iteracion 

    def __iter__(self):
        return self
    
    def __next__(self):
         if self.indicador < len(self.elementos):
            elemento = self.elementos[self.indicador]
            self.indicador += 1
            return elemento 
         else:
             return StopIteration # Cuando la iteracion termina, es decir, cuando ya no hay mas elementos  para recorrer 



Menú= [
    Bebidas("Pepsi", 2.500, "Pequeña"),
    Bebidas("Limonada", 2.000, "Grande"),
    Bebidas("Té Helado", 3.000, "Pequeño"),
    Aperitivo("Papitas", 5.500 ),
    Aperitivo("Yuca Frita", 5.000,),
    Aperitivo("Tajadas de platano", 4.000,),
    Plato_principal("Bistec a Caballo", 20.000, "Mediana"),
    Plato_principal("Arroz paisa", 25.000 , "Grande"),
    Plato_principal("Changua", 15.000, "Pequeña"),
    Plato_principal("Carne asada", 18.000, "Mediana"),
]

print("\nMenu:")
for a, elemento in enumerate(Menú, 1):
    print(f"{a}. {elemento}")
orden= Orden()

while True:
    Eleccion= input("\nDigite el número del producto que desea agregar (0 para finalizar): ")
    if Eleccion== "0":
        break
    if Eleccion.isdigit() and 1 <= int(Eleccion) <= len(Menú):
        orden.agregar_elemento(Menú[int(Eleccion) - 1])
        print(f"{Menú[int(Eleccion) - 1].nombre} añadido a la orden.")
    else:
        print("Por favor digite un numero valido")

print("\nElementos de la orden:")  # Para probar la nueva clase 
for a in orden:
    print(f"- {a.nombre} | Precio: ${a.precio}")

orden.mostrar_pedido()
