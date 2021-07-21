import easyocr

reader = easyocr.Reader(['pt']) #Define the language to be used

resultado = reader.readtext('images.png',paragraph=False)#Run the image reading

for resultado in resultado:
    x = resultado[1]# transfer the obtained data to a variable
    if(x[2]=="+"):#identifies the operation that will be performed
        y = x.split(" + ")#Run a treatment on the list and keep only the numbers that will be part of the calculation
        for i in range(0, len(y)):#Convert string list to integer
            y[i] = int(y[i])
        a=y[0]+y[1]#Perform the operation
        print(y[0],'+',y[1],"=",a)#Show the result
    elif(x[2]=="-"):
        y = x.split(" - ")
        for i in range(0, len(y)):
            y[i] = int(y[i])
        a=y[0]-y[1]
        print(y[0],'-',y[1],"=",a)
    elif(x[2]=="x"):
        y = x.split(" x ")
        for i in range(0, len(y)):
            y[i] = int(y[i])
        a=y[0]*y[1]
        print(y[0],'x',y[1],"=",a)
    elif(x[2]=="/"):
        y = x.split(" / ")
        for i in range(0, len(y)):
            y[i] = int(y[i])
        a=y[0]/y[1]
        print(y[0],'/',y[1],"=",a)