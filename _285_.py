################################################################### calculator

from tkinter import *
def logic(operator):
   if operator == "C":
       label['text']='0'
   elif operator == 'DEL':
       label['text']=label['text'][0:-1]
       if label['text'] == '':
           label['text'] = '0'
   elif operator == '=':
       label['text']=str(eval(label['text']))
   elif operator == 'X^2':
       label['text']=str(eval(label['text'])**2)
   else:
       if label['text'] == '0':
           label['text'] = ''
       label['text']=label['text']+operator

root = Tk()
list = ['C','DEL','*','=','1','2','3','/','4','5','6','+','7','8','9','-','(','0',')','X^2']
root.title('Сложный калькулятор')
root['bg'] = 'black'
root.geometry('485x550')
root.resizable(False, False)
label = Label(text = '0', font=('consolas', 21, 'bold'), fg = 'white', bg = 'black')
label.place(x=10,y=50)
x =  10
y = 140
for lis in list:
   com = lambda x=lis: logic(x)
   Button(text = lis, background = 'white', foreground = 'black',
          font = ('consolas', 15), command = com).place(x = x, y = y, width = 115, height = 79)
   x+=117
   if x > 400:
       x = 10
       y += 81
root.mainloop()

