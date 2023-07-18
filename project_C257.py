from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")

frame = Frame(
    root,
    bg='white',
    padx=5,
    pady=5
)
# create the labels to hold the account numbers







#Create entry elements to get the use input for account addresses 






#place the entry elements on the root window






#create the text box


#define a function CHECK_BALANCE() and add the code inside it.

    
   
  
    

    




       
     
        
      

frame.pack()

#Create a button element to call the CHECK_BALANCE()


    

result.pack(pady=5)
root.mainloop()

