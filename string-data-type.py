theString = "this is a string"
print(theString)
print(type(theString))
print(theString + " es un tipo de dato " + str(type(theString)))
 
string1 = "pollo"
string2 = "papas fritas"
string3 = string1 + string2
print(string3)

nombre = input("¿Cuál es tu nombre?")
print(nombre)

mascota = input("¿Cómo se llama tu mascota?")
pais = input("¿De dóńde eres?")
print("{} tienes un {} de {} fenomenal !".format(nombre,mascota,pais))