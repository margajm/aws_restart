frase = input("Ingrese una frase")
letra = input("Ingresa una letra")

contador = 0

for i in frase:
    if i == letra:
        contador +=1
        
        
print("La letra %s aparece %2i veces en lafrase "%s"." %(letra, contador, frase))
    
    