def invoiceDetail(customer,p,q,final,d):
    import random
    import datetime
    n=str(random.randint(1,100))
    no=(n+".txt")
    file=open(no,"w")
    file.write("\t\t ELECTRONICS")
    file.write("\n \t\t\tKamal Pokhari,Nepal ")
    file.write("\n-------------------------------------------------------------")
    file.write("\nInvoice"+"\t\t\t Invoice No: "+n)
    file.write("\nCustomer Name: "+str(customer))
    file.write("\nPurchased Product:"+str(p))
    file.write("\nPurchased quantity:"+str(q))
    file.write("\nDiscount amount:"+str(d))
    file.write("\nYour Total: "+str(final))
    file.write("\nDate and Time: "+datetime.datetime.now().strftime("%y:%m:%d %H:%M"))
    file.close()

