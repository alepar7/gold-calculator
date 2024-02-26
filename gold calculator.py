from tkinter import *

window = Tk()
window.title('Gold Calculator')

lab_price = LabelFrame(window, text='Price', height=50, width=200)
lab_price.pack(fill='none',side=LEFT)

lab_cal = LabelFrame(window, text='Calculator', height=50, width=200)
lab_cal.pack(fill='none',side=LEFT)

lab_acount = LabelFrame(window, text='Acounter', height=50, width=200)
lab_acount.pack(fill='none',side=LEFT)


price_eny = Entry(lab_price)
price_eny.pack()




lab_parsian = LabelFrame(lab_cal, text='A/b', height=50, width=200)
lab_parsian.pack(fill='none',side=LEFT)

lab_notax = LabelFrame(lab_cal, text='Calculator', height=50, width=200)
lab_notax.pack(fill='none',side=LEFT)

lab_tax = LabelFrame(lab_cal, text='Calculator', height=50, width=200)
lab_tax.pack(fill='none',side=LEFT)




lab_ac = LabelFrame(lab_acount, text='Calculator', height=50, width=200)
lab_ac.pack(fill='none',side=LEFT)

lab_sum = LabelFrame(lab_acount, text='Calculator', height=50, width=200)
lab_sum.pack(fill='none',side=LEFT)

lab_par = LabelFrame(lab_acount, text='Calculator', height=50, width=200)
lab_par.pack(fill='none',side=LEFT)




# window.geometry('800x600')
window.mainloop()