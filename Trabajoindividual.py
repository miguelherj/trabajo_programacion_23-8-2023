import os 
os.system ('cls')


asig= []
nott = []
var = int(input('cuntas asignaturas desea incluir?: '))
cont = 0
while cont < var:
    asignatura, nota = (input('Ingrese la asignatura: '),float(input('Ingrese la nota: ')))
    asig.append(asignatura)
    nott.append(nota)
    cont += 1
    

for materia, nota in zip(asig,nott):
    print(materia, nota)

print("------------------------------------------------------------------------------------")
persona = {}
var= int(input("cuantas persnas quiere ingresar "))
cont1 = 0
cont2 = 1
while cont1 < var:
    persona[cont2]= (input("ingrese su nombre: "))
    cont1 += 1
    cont2 += 1
for valor in persona.values():
    print ("su nombre es:", valor)

print("------------------------------------------------------------------------------------")
moneda = {'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}
peso = int(input('Ingrese la cantidad de dinero en pesos colombianos: '))
mon= int(input('a cual moneda desea hacer la conversion? (0 = euro, 1 = dolar, 2 = yen): '))

if mon == 0:
    conv = 4*peso
    print('Su cambio es: ',conv, moneda.get('Euro'))
elif mon == 1:
    conv = 4*peso
    print('Su cambio es: ',conv, moneda.get('Dollar'))
elif mon == 2:
    conv = 0.28*peso
    print('Su cambio es: ',conv, moneda.get('Yen'))
else: 
    print ("esa divisa no se encuentra:")

print("------------------------------------------------------------------------------------")
var = 0
valores = (5,5.5,'hello world', ('equis', 3) )
for var, tipo in enumerate(valores):
    print(f"Elemento en la posición {var} es de tipo {type(tipo)}")
