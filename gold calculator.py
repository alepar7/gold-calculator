from tkinter import *
from decimal import Decimal
window = Tk()
window.title('Gold Calculator')


def price():
    p = float(gold_price.get())
    return p


def carat(w,c):
    a = (w * c) / 750
    return a


def summ():
    result_1 = []
    
    for i in range(3):
        a = float(e_list[i].get()) if e_list[i].get() else 0
        result_1.append(a)
    
    # Perform calculations here using the retrieved values
    # For demonstration purposes, let's just display the values entered
                    # jam = sum(result_1) + price()
    
    


    w = carat(result_1[0], result_1[1])
    result_final = int((w * price()) + (result_1[2]))
    result_final= (f"{result_final:,}")
    # Display the result
    Label(lab_parsian, text=result_final).grid(row=3, column=1)





# main frame:
lab_price = LabelFrame(window, text='Price', height=50, width=200)
lab_price.grid(row=0, column=0)

lab_cal = LabelFrame(window, text='Calculator', height=50, width=200)
lab_cal.grid(row=1, column=0)

lab_acount = LabelFrame(window, text='Acounter', height=50, width=200)
lab_acount.grid(row=2, column=0)

lab_carat = LabelFrame(window, text='carat', height=50, width=200)
lab_carat.grid(row=3, column=0)

gold_price = Entry(lab_price)
gold_price.pack()



# inside Frames:
lab_parsian = LabelFrame(lab_cal, text='Parsian', height=50, width=200)
lab_parsian.pack(fill='none',side=LEFT)

lab_notax = LabelFrame(lab_cal, text='None Tax', height=50, width=200)
lab_notax.pack(fill='none',side=LEFT)

lab_tax = LabelFrame(lab_cal, text='With Tax', height=50, width=200)
lab_tax.pack(fill='none',side=LEFT)

lab_ac = LabelFrame(lab_acount, text='A/B', height=50, width=200)
lab_ac.pack(fill='none',side=LEFT)

lab_sum = LabelFrame(lab_acount, text='Weight Sum', height=50, width=200)
lab_sum.pack(fill='none',side=LEFT)

lab_par = LabelFrame(lab_acount, text='Parsian', height=50, width=200)
lab_par.pack(fill='none',side=LEFT)




# main parsian label
labals = ['Weight:','carat:','Vacume:','Result:']
e_list = []

for n , i in enumerate(labals): # Entry name
    Label(lab_parsian, text=i).grid(row=n, column=0)

for i in range(3): 
    if i == 1:
        v = StringVar(lab_parsian,value=750) # default value for Entry
        
    else:
        v = StringVar(lab_parsian,value='')
    e_parsian = Entry(lab_parsian, textvariable=v)
    e_parsian.grid(row=i,column=1)
    e_list.append(e_parsian)

# main parsian objects
main_parsian_btn = Button(lab_parsian,text='OK', command=summ)
main_parsian_btn.grid(row=4, column=1)




# none tax label
labals_1 = ['Weight:','carat:','Found:','Result:']

for n , i in enumerate(labals_1):
    Label(lab_notax, text=i).grid(row=n, column=0)

for i in range(3):
    Entry(lab_notax).grid(row=i,column=1)



# With tax label
labals_2 = ['Weight:','carat:','Pay','Tax','Found:','Result:']

for n , i in enumerate(labals_2):
    Label(lab_tax, text=i).grid(row=n, column=0)

for i in range(5):
    Entry(lab_tax).grid(row=i,column=1)


# A/B labels
Label(lab_ac, text='Creditor').grid(row=0, column=0)
Label(lab_ac, text='Debtor').grid(row=0, column=1)

for i in range(1,20):
    for j in range(2):
        Entry(lab_ac).grid(row=i, column=j)

Label(lab_ac, text='result:').grid(row=21, column=0)


# Weight sum labels
for i in range(20):
    Entry(lab_sum).grid(row=i, column=0)

Label(lab_sum, text='SUM:').grid(row=21, column=0)



# parsian labels:
labels_2 = ['Row sum','Weight','Number']
for i , n in enumerate(labels_2):
    Label(lab_par, text=n).grid(row=0, column=i)

for i in range(3):
    for j in range(1,20):
        Entry(lab_par).grid(row=j, column=i)

Label(lab_par, text='SUM: ').grid(row=21, column=0)
Label(lab_par, text='SUM: ').grid(row=21, column=2)



# carat label
labels_3 = ['Carat','Weight']
for i,n in enumerate(labels_3):
    Label(lab_carat, text=n).grid(row=0, column=i+1)


Label(lab_carat, text='Weight 750:           ').grid(row=1, column=0)
Entry(lab_carat).grid(row=1, column=1)
Entry(lab_carat).grid(row=1, column=2)



# window.geometry('800x800')
window.mainloop()