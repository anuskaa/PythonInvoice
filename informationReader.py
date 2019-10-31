informationFile=open('ProductInformation.txt','r')
lines=informationFile.readlines()
stocklist=[]
for items in lines:
    d=items.replace('\n','').replace(' ','').split(',')
    stocklist.append(d)
    
informationFile.close
 
for i in stocklist:
    print(i)
    


