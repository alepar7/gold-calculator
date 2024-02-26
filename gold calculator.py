from tkinter import *

window = Tk()
window.title('Gold Calculator')


# Def:
# def eny():
#     Entry().pack()



# main frame:
lab_price = LabelFrame(window, text='Price', height=50, width=200)
lab_price.grid(row=0, column=0)

lab_cal = LabelFrame(window, text='Calculator', height=50, width=200)
lab_cal.grid(row=1, column=0)

lab_acount = LabelFrame(window, text='Acounter', height=50, width=200)
lab_acount.grid(row=2, column=0)

lab_carat = LabelFrame(window, text='carat', height=50, width=200)
lab_carat.grid(row=3, column=0)





price_eny = Entry(lab_price)
price_eny.pack()






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





labals = ['Weight:','carat:','Vacume:','Result:']


for n , i in enumerate(labals): # Entry name
    Label(lab_parsian, text=i).grid(row=n, column=0)

for n , i in enumerate(labals): # Entry
    Entry(lab_parsian).grid(row=n, column=1)






window.geometry('800x600')
window.mainloop()