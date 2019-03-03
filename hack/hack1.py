#from Tkinter import *
#for V2
#import datetime
from time import gmtime, strftime
from tkinter import *

root =Tk()
root.title("MCI sceern")
root.geometry("200x200")



app=Frame(root)

app.grid()
#label1=Label(app,text=
#label1.grid()



#the file ----------
handle=open("r.txt").read()

a=handle.strip().replace('\n',' ').replace('{',' ').replace(',',' ').replace('<',' ').replace('>',' ').replace(':',' ').replace('}',' ').replace('/',' ').split(" ")

c=set(a)

#-----------------------------------------------
#print the Status
#-----------------------------------------------
critical1=["lightly","Slight","slight", "Easy", "easy"] 
critical2=["moderate","medium"]
critical3=["hard","difficult"]
critical4=["critical","criti"]


if not c.isdisjoint(critical1):
    label1=Label(app,text="Status: easy", height = 2,bg="green")
    label1.pack(side = "left")
    app.configure(bg = "green")
    print("----GREEN SCREEN---")
    print("Status: easy")
    color="green"
   
elif not c.isdisjoint(critical2):
    label1=Label(app,text="Status: medium", height = 2,bg="yellow")
    app.configure(bg = "yellow")
    label1.pack(side = "left")
    print("----YELLOW SCREEN---")
    print("Status: medium")
    color="yellow"

elif not c.isdisjoint(critical3):
    label1=Label(app,text="Status: hard", height = 2,bg="orange")
    app.configure(bg = "orange")
    label1.pack(side = "left")
    print("----ORANGE SCREEN---")
    print("Status: hard")
    color="orange"

elif not c.isdisjoint(critical4):
    label1=Label(app,text="Status: critical", height = 2,bg="red")
    label1.pack(side = "left")
    app.configure(bg = "red")
    print("----RED SCREEN---")
    print("Status: critical")
    color="red"
    
else:    
    print("")
    label1=Label(app,text="", height = 2,bg="white")
    label1.pack(side = "left")
    app.configure(bg = "white")
    color="white"
    
label1.grid()   


#-----------------------------------------------
#print the Treatment
#-----------------------------------------------
treatment1=["tourniquet"]
treatment2=["infusion"]
treatment3=["dressing","bandage"]
treatment4=["resuscitation"]

print("Treatment:",end="")
tex="Treatment:"

if not c.isdisjoint(treatment1):
    tex+=" tourniquet,"
    print(" tourniquet,",end="")

if not c.isdisjoint(treatment2):
    tex+=" infusion,"
    print(" infusion,",end="")


if not c.isdisjoint(treatment3):
    tex+=" bandage,"
    print(" bandage,",end="")


if not c.isdisjoint(treatment4):
    tex+=" resuscitation,"
    print(" resuscitation,",end="")

else:    
    print()
    
label2=Label(app,text=tex, height = 2,bg=color)
label2.grid()
print()


#-----------------------------------------------
#Location injury:
#-----------------------------------------------

injury1=["head","headache"]
injury2=["hand","arm"]
injury3=["internal"]# Internal organs
injury4=["lung","lungs"]
injury5=["foot","leg"]

tex2="Injury Location:"
print("Injury Location:",end="")

if not c.isdisjoint(injury1):
    tex2+=" head,"
    print(" head,",end="")

if not c.isdisjoint(injury2):
    tex2+=" hand,"
    print(" hand,",end="")

if not c.isdisjoint(injury3):
    tex2+=" Internal organs,"
    print(" Internal organs,",end="")

if not c.isdisjoint(injury4):
    tex2+=" lungs,"
    print(" lungs,",end="")

if not c.isdisjoint(injury5):
    tex2+=" leg,"
    print(" leg,",end="")

else:    
    print()
label3=Label(app,text=tex2, height = 2,bg=color)
label3.grid()
print()

#-----------------------------------------------
#print time
#-----------------------------------------------

label5=Label(app,text= str( strftime("%Y-%m-%d %H:%M:%S", gmtime())),height = 2,bg=color)
label5.grid()
print(str( strftime("%Y-%m-%d %H:%M:%S", gmtime())))


root.mainloop()

