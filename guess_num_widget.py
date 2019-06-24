

from tkinter import *

class Application(Frame):
    """ GUI application which could reveal the secret number. """ 
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label
        self.inst_lbl = Label(self, text = "Enter a number (0-99)")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create label for password      
        self.guess_lbl = Label(self, text = "My guess is: ")
        self.guess_lbl.grid(row = 1, column = 0, sticky = W)

        # create entry widget to accept password      
        self.guess_ent = Entry(self, text = " ")
        #sself.guess_ent.bind("<return>",self.reveal)
        self.guess_ent.grid(row = 1, column = 1, sticky = W)
        
        self.guess_ent.focus()

        # create submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        

        # create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        self.number = self.extract_Number()
        #self.reveal()

    def reveal(self):
        """ Display message based on guess. """
        contents = self.guess_ent.get()
        
        contents = int(contents)
        if contents == self.number:
            message = "CORRECT!"
                                
        else:
            if contents > self.number:
                message = "Too high... "
                self.guess_ent.delete(0, END)
        
            else:
                message = "Too low... "
                self.guess_ent.delete(0, END)        
             
                      
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)
        
    def extract_Number(self):

        import random  
        self.number = random.randint(0, 100)
        return self.number



# main
root = Tk()
root.title("Guess My Number")
root.geometry("300x150")


app = Application(root)

root.mainloop()






