userReply = input("¿Necesitas lleva un paquete?(Ingresa SI o NO)")

if userReply == "si":
    print("Nosotros podemos ayudarte a llevar ese paquete!")

else:
    print("Please come to back when you need to ship a package. Thank you.")
    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy?(Enter stamps, envelope orcopy)")
if userReply == "stamps":
    print("We have many stamp design to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How mny copies would you like? ( Enter a number)")
    print("Here are {} copies".format(copies))
else:
    print("Thank you, please come again.")