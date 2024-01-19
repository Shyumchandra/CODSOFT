import tkinter as tk 
from tkinter import messagebox

class Contact_List:
    
    def __init__(self,name,phone,email,address):
        self.name=name 
        self.phone=phone
        self.email=email
        self.address=address
        
class contact:
    
    def __init__(self,root):
        self.root=root
        self.root.title("---CONTACT BOOK---")
        self.contacts=[]
        self.Layout()
        
    def Layout(self):
        
        self.Name_Label=tk.Label(root,text="NAME",font=("Arial,Bold",15))
        self.Name_Label.grid(row=0, column=0)
        
        self.Name_Entry=tk.Entry(root,width=25,font=("Arial,Bold"))
        self.Name_Entry.grid(row=0, column=20)
        
        self.Phone_Label=tk.Label(root,text="PHONE NUMBER",font=("Arial,Bold",15))
        self.Phone_Label.grid(row=1, column=0)
        
        self.Phone_Entry=tk.Entry(root,width=25,font=("Arial,Bold"))
        self.Phone_Entry.grid(row=1, column=20)
        
        self.Email_Label=tk.Label(root,text="EMAIL",font=("Arial,Bold",15))
        self.Email_Label.grid(row=2, column=0)
        
        self.Email_Entry=tk.Entry(root,width=25,font=("Arial,Bold"))
        self.Email_Entry.grid(row=2, column=20)
        
        self.Address_Label=tk.Label(root,text="ADDRESS",font=("Arial,Bold",15))
        self.Address_Label.grid(row=3, column=0)
        
        self.Address_Entry=tk.Entry(root,width=25,font=("Arial,Bold"))
        self.Address_Entry.grid(row=3, column=20)
        
        self.Add_Button=tk.Button(root,text="ADD CONTACT",bg="orange",command=self.Add)
        self.Add_Button.place(x=10, y=150)
        
        self.View_Button=tk.Button(root,text="VIEW CONTACT",bg="orange",command=self.View)
        self.View_Button.place(x=120, y=150)
        
        self.Search_Button=tk.Button(root,text="SEARCH CONTACT",bg="orange",command=self.Search)
        self.Search_Button.place(x=235, y=150)
        
        self.Update_Button=tk.Button(root,text="UPDATE CONTACT",bg="orange",command=self.Update)
        self.Update_Button.place(x=365, y=150)
        
        self.Delete_Button=tk.Button(root,text="---------DELETE CONTACT---------",bg="yellow",command=self.Delete)
        self.Delete_Button.place(x=150, y=200)
        
    def Add(self):
        name=self.Name_Entry.get()
        phone=self.Phone_Entry.get()
        email=self.Email_Entry.get()
        address=self.Address_Entry.get()
        
        contact=Contact_List(name,phone,email,address)
        self.contacts.append(contact)
        self.Clear()
        messagebox.showinfo("Message",">>CONTACT ADDED<<")
        
    def View(self):
        if not self.contacts:
            messagebox.showinfo("ERROR",">>NO CONTACTS ARE IN THE LIST<<")
        else:
            list="CONTACT LIST :: \n"
            for contact in self.contacts:
                list +=f"Name = {contact.name}  PhoneNumber = {contact.phone}\n"
                
        messagebox.showinfo("CONTACTS",list)
        
    def Search(self):
        name=self.Name_Entry.get()
        found=[]
        for contact in self.contacts:
            if name in contact.name:
                found.append(contact)
        if found:
            list_s="Searched Contacts \n"
            for contact in found:
                list_s +=f"Name = {contact.name}  PhoneNumber = {contact.phone}\n"
                messagebox.showinfo("CONTACTS",list_s)    
        else:
            messagebox.showinfo("ERROR",">>CONTACT NOT FOUND<<")
        
    def Update(self):
        email=self.Email_Entry.get()
        found = None
        for contact in self.contacts:
            if email in contact.email:
                found=contact
                break
            
        if found:
            name=self.Name_Entry.get()
            phone=self.Phone_Entry.get()
            email=self.Email_Entry.get()
            address=self.Address_Entry.get()
            
            found.name=name
            found.phone=phone
            found.email=email
            found.address=address
            
            self.Clear()
            messagebox.showinfo("Message",">>CONTACT UPDATED<<")
        else:
            messagebox.showinfo("ERROR",">>CONTACT NOT FOUND<<")
    
    def Delete(self):
        email=self.Email_Entry.get()
        found=None
        
        for contact in self.contacts:
            if email in contact.email:
                found=contact
                break
            
        if found:
            self.contacts.remove(found)
            self.Clear()
            messagebox.showinfo("Message",">>CONTACT DELETED<<")
        else:
            messagebox.showinfo("ERROR",">>CONTACT NOT FOUND<<")

    def Clear(self) :
        self.Name_Entry.delete(0, tk.END)
        self.Phone_Entry.delete(0, tk.END)
        self.Email_Entry.delete(0, tk.END)
        self.Address_Entry.delete(0, tk.END)
    
    
if __name__ =="__main__":
    root=tk.Tk()
    app=contact(root)
    root.geometry("530x250")
    root.mainloop()    