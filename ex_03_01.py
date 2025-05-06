hrs = input("Enter Hours:")

      hrspay= input("Enter Hourspay:")

     hrs=float(hrs)


    hrspay=float(hrspay)

if hrs<= 40:
    
    brut_ucret=hrs*hrspay
else:
    brut_ucret = (40 * hrspay) + ((hrs - 40) * (hrspay * 1.5))
                            
print(brut_ucret)

print( )
