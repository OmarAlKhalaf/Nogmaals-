# name of student: Omar Al Khalaf
# number of student: 99047548
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # The amount that he have to pay
paid = int(float(input('Paid amount: ')) * 100) # The amount that he did pay 
change = paid - toPay # Payment results

if change > 0: # if the change ( Results ) biger then 0 
  coinValue = 50 # Coin value is 50
  
  while change > 0 and coinValue > 0: # While the change is greater than 0 and the coin value is greater than 0
    nrCoins = change // coinValue # NrCoins is change share coin value

    if nrCoins > 0: # If nr coins is greater than 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Write return maximum (number of coins) and coins value in cents
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Input how many coins did you return?
      change -= nrCoinsReturned * coinValue # Change parts nrCoins Returned and multiply coin Value

# comment on code below: 
    if coinValue == 500:    # If Coin value is ( 500 ) cents 
        coinValue = 300     # Dan Coin value is ( 300 ) cents 
    elif coinValue == 300:  #If Coin value is ( 300 ) cents 
      coinValue = 200       #Dan Coin value is ( 200 ) cents 
    elif coinValue == 200:  #If Coin value is ( 200 ) cents 
      coinValue = 100       #Dan Coin value is ( 100 ) cents 
    elif coinValue == 100:  #If Coin value is ( 100 ) cents 
      coinValue = 50        #Dan Coin value is ( 50 ) cents 
    elif coinValue == 50:   #If Coin value is ( 50 ) cents 
      coinValue = 20        #Dan Coin value is ( 20 ) cents 
    elif coinValue == 20:   #If Coin value is ( 20 ) cents 
        coinValue = 10      #Dan Coin value is ( 10 ) cents 
    elif coinValue == 10:   #If Coin value is ( 20 ) cents 
        coinValue = 5       #Dan Coin value is ( 5 ) cents 
    elif coinValue == 5:    #If Coin value is ( 5 ) cents 
        coinValue = 2       #Dan Coin value is ( 2 ) cents 
    elif coinValue == 2:    #If Coin value is ( 2 ) cents 
        coinValue = 1       #Dan Coin value is ( 1 ) cents 
    elif coinValue == 1:    #If Coin value is ( 1 ) cents 
        coinValue = 0       #Dan Coin value is ( 0 ) cents
elif change > 0: #If change is greater than zero
    print('Change not returned: ', str(change) , ' cents')#write change not returned + change(results)
elif toPay > paid:
    #if the amount the user has to pay is greater than the amount the user has paid
    print("Payment is not enough! you have to pay:", str(change) + "cents")
    #write 'Paying is not enough' and the amount he has to pay
    while True: #loop
        toPay = int(float(input("Paid amount")))
        #enter the amount he still has to pay
        if toPay == change : #if the user has paid the amount he has to pay
            print("Done")#write done
            break # stop the loop
        else:
            print("Payment is not enough! you have to pay:", str(change) + "cents")
else:
    #Otherwise write "done" and list all returned coins
    print('done') 
    treugGegeven = toPay - paid
    print("Treug gegeven met munten" , treugGegeven , "cents")