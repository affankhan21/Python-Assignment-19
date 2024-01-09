def Converter(x,y,amt):    
    if(x == 'INR' and y == 'USD'):
        amt = amt*0.012
            
    elif(x == 'USD' and y == 'INR'):
        amt = amt*83.12
            
    elif(x == 'INR' and y == 'EUR'):
        amt = amt*0.011
           
    elif(x == 'EUR' and y == 'INR'):
        amt = amt*91.75
            
    elif(x == 'INR' and y == 'RUB'):
        amt = amt*1.11

    elif(x == 'RUB' and y == 'INR'):
        amt = amt*0.90

    elif(x == 'INR' and y == 'JPY'):
        amt = amt*1.71

    elif(x == "JPY" and y == "INR"):
        amt = amt*0.58

    elif(x == "USD" and y == "EUR"):
        amt = amt*0.91

    elif(x == "EUR" and y == "USD"):
        amt = amt*1.10

    elif(x == "USD" and y == "RUB"):
        amt = amt*91.87

    elif(x == "RUB" and y == "USD"):
        amt = amt*0.011

    elif(x == "USD" and y == "JPY"):
        amt = amt*142.2

    elif(x == "JPY" and y == "USD"):
        amt = amt*0.007

    elif(x == "EUR" and y == "RUB"):
        amt = amt*101.35

    elif(x == "RUB" and y == "EUR"):
        amt = amt*0.0098

    elif(x == "EUR" and y == "JPY"):
        amt = amt*156.83
        
    elif(x == "JPY" and y == "EUR"):
        amt = amt*0.0064

    elif(x == "RUB" and y == "JPY"):
        amt = amt*1.54

    elif(x == "JPY" and y == "RUB"):
        amt = amt*0.65

    else:
        amt = amt*1

    return amt
