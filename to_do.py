#importing package
from tkinter import *

#function for adding an item
def add_item(text: Text,listbox: Listbox):
    
    new_task=text.get(1.0,END)
    listbox.insert(END, new_task)
    with open('tasks.txt','a') as tasks_list_file:
        tasks_list_file.write(new_task)
        tasks_list_file.seek(0)
        tasks_list_file.close()
    text.delete(1.0,END)    
   
#function for deleting all items   
def clear_list(listbox: Listbox):
    listbox.delete(0,END)
    with open('tasks.txt', 'w+') as list_file:
        lines = list_file.readlines()
        list_file.close()
 
#function for deleting an item      
def Delete_item(listbox: Listbox):
    delete_=listbox.curselection() 
    look=listbox.get(delete_)
    with open('tasks.txt','r+') as file:
         lines=file.readlines()
         file.seek(0)
         for line in lines:
            item=str(look)
            if item not in line:
                file.write(line)
         file.truncate()
    listbox.delete(delete_)  

    with open('tasks.txt','r') as tasks_list_file:
      read=tasks_list_file.readlines()
      for i in read:
          ready=i.split()
          listbox.insert(END)
      tasks_list_file.close()    
                     
        
#Initializing TO-DO list GUI Window       
root=Tk()
root.title("To-Do LIST")
root.geometry('400x450')
root.resizable(0,0)
root.config(bg="White")

#Creating a Label for Heading
l1=Label(root,text="To-Do-List",font=("Arial,Bold",15),bg='Orange',fg='Black',wraplength=500,width=35)
l1.place(x=4,y=10)

#Listbox with all the tasks along with a Scrollbar
tasks=Listbox(root,fg='Black',bg='Silver',font=("ArialBaltic",15))

scroller=Scrollbar(root,orient=VERTICAL,command=tasks.yview)
scroller.place(x=382,y=50,height=250)
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=2,y=50,height=250,width=400)

#Adding items to the Listbox
with open('tasks.txt','r+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END,task)
    tasks_list.close()
    

#creating an Entry Widget
text=Text(root,font=('Arial',15),width=25)
text.place(x=50,y=320,height=28)

#Add Button for entering a task into Listbox
add_btn=Button(root,text="Add Task",bg='White',font=('Arial',12),width=15,command=lambda: add_item(text, tasks))
add_btn.place(x=40,y=360)

#clear Button for deleting all the tasks in the Listbox
clear_btn=Button(root,text="Clear List",bg='White',font=('Arial',12),width=15,command=lambda: clear_list(tasks))
clear_btn.pack()
clear_btn.place(x=210,y=360)

#Delete Button for deleting a task in the Listbox
delete_btn=Button(root,text="Delete Task",bg="White",font=('Arial',12),width=15,command=lambda: Delete_item(tasks) )
delete_btn.place(x=40,y=400)

#Finalizing the Window
root.update()
root.mainloop()