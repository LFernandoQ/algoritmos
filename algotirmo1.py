'''La langosta ahumada” es una empresa dedicada a ofrecer banquetes; sus
tarifas son las siguientes: el costo de platillo por persona es de $95.00,
pero si el número de personas es mayor a 200 pero menor o igual a 300,
el costo es de $85.00. Para más de 300 personas el costo por platillo es de
$75.00'''

cantidadPersonas = int(input("Ingrese la cantidad de personas"))
if cantidadPersonas <= 200:
    ValorTotal = cantidadPersonas * 95 
    print("El valor total es de:  " + str(ValorTotal))
elif 200<=cantidadPersonas<=300:
    ValorTotal = cantidadPersonas * 85 
    print("El valor total es de: " + str (ValorTotal))
else:
    ValorTotal = cantidadPersonas * 75 
    print ("El valor total es de:  " + str (ValorTotal))