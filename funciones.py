print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")
def chat(mensa):
    print(f"Chat: {mensa}")
def elcontesta(mensa):
    print(f"Chat el: {mensa}")
def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")
def suma(a,b):
    s = a+b 
    return s
def resta(c,d):
    r = c-d
    return r
def mult(e,f):
    m = e*f
    return m
def div(g,h):
    d = g/h
    return d
# llamar funcion
hola()
chat("Que bonito estas")
elcontesta("Gracias")
escribenombre("Ramirez" ,"Daniel")
print("Operacion suma")
c1 = int(input("Ingresa un numero:"))
c2 = int(input("Ingresa un numero:"))
damesuma = suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")
print("Operacion resta")
c3 = int(input("Ingresa un numero:"))
c4 = int(input("Ingresa un numero:"))
dameresta = resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")
print("Operacion multiplicacion")
c5 = int(input("Ingresa un numero:"))
c6 = int(input("Ingresa un numero:"))
damamult = mult(c5,c6)
print(f"La multiplicacion de {c5} * {c6} = {damamult}")
print("Operacion divide")
c7 = int(input("Ingresa un numero:"))
c8 = int(input("Ingresa un numero:"))
damediv = div(c7,c8)
print(f"La division de {c7} / {c8} = {damediv}")