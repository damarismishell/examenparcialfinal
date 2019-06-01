from tkinter import*



#logica
#semestre1
#Dámaris Mishell Rojas Ceballos
#0907-19-5664
raiz= Tk()

suma=0
almacenar=0
resta=0
multiplicar=0
miframe=Frame(raiz,width=500,height=300)
miframe.pack


caja1=Entry(raiz)
caja1.place(x="10", y="20")
caja2=Entry(raiz)
caja2.place(x="10", y="60")
caja3=Entry(raiz)
caja3.place(x="10", y="100")


def buton1event():
    global suma
    global resta
    global multiplicar
    

    val1=int(caja1.get())
    val2=int(caja2.get())
    val3=int(caja3.get())

    if val1<val3:
        multiplicar=val1*val2*val3
        label1=Label(raiz,text="Multiplicacion:"+str(multiplicar),font=15,fg="green")
        label1.place(x="10",y="150")

    if val1==val3:
        suma=val1+val2+val3
        label1=Label(raiz,text="Suma:"+str(suma),font=15,fg="green")
        label1.place(x="10",y="150")

    if val2==0:
        if val1>val3:
            resta=val1-val3
            label1=Label(raiz,text="Resta:"+str(resta),font=15,fg="green")
            label1.place(x="10",y="150")
        else:
            resta=val3-val1
            label1=Label(raiz,text="Resta:"+str(resta),font=15,fg="green")
            label1.place(x="10",y="150")


def segundoboton():

    val1=int(caja1.get())
    val2=int(caja2.get())
    val3=int(caja3.get())

    global suma
    global resta
    global multiplicar
    
    almacenar=val1*val2+val3

   
    
    Impresiontex=Label(raiz,text="SUMA: "+str(suma)+"Resta: "+str(resta)+"Multiplicar: "+str(multiplicar))
    Impresiontex.place(x="10",y="170")









boton1=Button(raiz,text="tocar1",command=buton1event)
boton1.place(x="70",y="130")
boton2=Button(raiz,text="tocar2",command=segundoboton)
boton2.place(x="120",y="130")


raiz.mainloop()
