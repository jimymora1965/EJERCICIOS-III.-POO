#crear un juego que lso personajes puedan fusionarse para formar personajes que sean mas poderosos. para ello debemos cambiar el comportamiento del operador "+" para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas. una posible formula es: el promedio de las habilidades de ambos, al cuadrado.

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.n = nombre
        self.f = fuerza
        self.v = velocidad

    def __repr__(self):
        return f"{self.n} = Fuerza:{self.f}, Velocidad: {self.v}"
    
    def __add__(self, nuevo_heroe):
        nuevo_nombre = self.n + "-" + nuevo_heroe.n
        nueva_fuerza = round(((self.f + nuevo_heroe.f)/2)**1.5)
        nueva_velocidad = round(((self.v + nuevo_heroe.v)/2)**1.5)
        return Personaje(nuevo_nombre, nueva_fuerza,nueva_velocidad)
    
goku = Personaje("Goku",100,100)
vegeta = Personaje("Vegeta", 99,99)
jiren = Personaje("Jiren",130,140)
gogeta = goku + vegeta
jireta = vegeta + jiren
print(goku)
print(vegeta)
print(jiren)
print(gogeta)
print(jireta)
