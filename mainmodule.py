from informationReader import stocklist #reads the stocklist from information reader
import datetime

boughtList=[] #creates an empty list
d=0           
tot=0
total=0
p=[]
purchasedProduct=[] #empty list
q=[]                #empty list
quanti=[]           #empty list
print("--------------------------------------------------------")
print("\n\t\tWelcome to ELECTRONICS")
customer=str(input("Enter customer name:"))         #ask to enter customer name

print("HELLO"+" "+customer+" "+"Welcome to our shop.")

print("--------------------------------------------------------------")


purchaseproduct=str(input("If you would like to purchase product:(y/n)?"))  #askes if you wan to purchase any product
while purchaseproduct=='y':                                                 # if yes then executes the program
    product=input("Enter product you want to purchase?")                    # product to purchase
    p.append(product)
    purchasedProduct.append(p)
    for i in range(len(purchasedProduct)):
        a=str(purchasedProduct[i])

            
    success = False
    while success == False:
        quantity=int(input("How much do you want sir/madam??\n"))           #quantity to purchase
        q.append(quantity)
        for i in range(len(quanti)):
            quanti.append(quanti[i])
        try:
            for i in range(len(stocklist)):
                if quantity<=int(stocklist[i][2]) and quantity>0: #comparing the available products quantity
                    success = True
            if success ==False:
                print("Not in stock or invalid quantity")
        except:
            print("Invalid value")
        
    count=0
    f= False                                
    for i in range(len(stocklist)):
        products=stocklist[i][0]
        if products.upper()==product.upper():               #checking if the product is available or not
            count+=1
            f= True
            if stocklist[i][2]!=0:
                amount=stocklist[i][1]
                newQuantity=int(stocklist[i][2])- quantity      #updates the list with new quantity
                stocklist[i][2]=str(newQuantity)
                tot=int(amount)*quantity
                nlist=[]
                nlist.append(products)
                nlist.append(amount)
                nlist.append(quantity)
                boughtList.append(nlist)
                print(boughtList)
            else:
                print("The product is out of stock.")
    if f== False:
        print("Sorry, the product is not avaialble")
        
       
    print("-----------------------------------------------------------------")
    print("Total no of "+" "+product+" "+"purchased is"+str(quantity)+" "+"at"+" "+str(tot))
    
    total=total+tot
    print("Amount to be paid till now.",total)
    anotherpurchase=input("Continue to buy another product:(y/n)?:")        #for purchasing any other product
    if anotherpurchase=='y':
        purchaseproduct=anotherpurchase
    elif anotherpurchase=='n':
        print("Thank you.")
        purchaseproduct=anotherpurchase
    else:
        print("Invalid entry")
        anotherpurchase=input("Continue to buy another product:(y/n)?:")


discountAmt=0
discountAvailable='y'
while discountAvailable=='y':
    check=input("Is discount available:(y/n)?:")    #for discount available
    if check=='y':
        try:
            discountAmt=int(input("\nEnter discount rate:"))
            final=0
            d=((discountAmt/100)*total)
            final=total-d
            print("Amount you have to pay after discount is",final)
            break
        except:
            print("Invalid value entered")
            break
            
    else:
        final=total
        print("Sorry no discount is available so you have to pay",final)
        break
updateList=stocklist        


from invoice import invoiceDetail
invoiceDetail(customer,p,q,final,d)

from updater import update_
update_(updateList)

print("total product purchased",boughtList)
print("total amount after discount :"+str(final))
print("Date and Time:"+datetime.datetime.now().strftime("%y:%m:%d %H:%M"))

print("THANK YOU")



        
    
            

            
        
        
        



    
    

    
                
            
                
                          
                

 
      

