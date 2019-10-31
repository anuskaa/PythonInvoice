def update_(updateList):
    file=open("ProductInformation.txt",'w')
    for each in updateList:
        update=str(each).replace('[',"").replace(']',"").replace("'","")
        file.write(update)
        file.write('\n')
    file.close()
        
    
