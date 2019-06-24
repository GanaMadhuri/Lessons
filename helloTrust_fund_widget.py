# Trust Fund Buddy - Good
# Demonstrates type conversion


from tkinter import *

class Application(Frame):
    """GUI application that creates a story based on user input."""
    def __init__(self, master):
        """initialization frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """Create widgets for story"""
        Label(self,
              text = "Trust Fund Buddy"
              ).grid()
        
        #create a label and text for name of person
        Label(self,
              text = """Totals your monthly spending so that your trust fund doesn't run out
              (and you're forced to get a real job).
              
              Please enter the requested, monthly costs.  Since you're rich, ignore pennies
              and use only dollar amounts.\n
              
              """
              ).grid()
        #self.person_ent = Entry(self)
        #self.person_ent.grid()

        Label(self,
              text = "Lamborghini Tune-Ups:  "
              ).grid(row = 8, column = 0, sticky = W)
        self.car_ent = Entry(self)
        self.car_ent.grid(row = 8, column = 1, sticky = W)
        
        #create a label and entry for verb
        Label(self,
              text = "Manhattan Apartment: "
              ).grid(row = 15, column = 0, sticky = W)
        self.apt_ent = Entry(self)
        self.apt_ent.grid(row = 15, column = 1, sticky = W)
        
        #create a label and entry for adjectibe
        Label(self,
              text = "Private Jet Rental: "
              ).grid(row = 25, column = 0, sticky = W)
        self.jet_ent = Entry(self)
        self.jet_ent.grid(row = 25, column = 1, sticky = W)
        
        Label(self,
              text = "Gifts: "
              ).grid(row = 45, column = 0, sticky = W)
        self.gift_ent = Entry(self)
        self.gift_ent.grid(row = 45, column = 1, sticky = W)
       
        Button(self,
               text = "CLICK FOR THE TOTAL",
               command = self.tell_story
               ).grid(row=55, column = 0, sticky =W)
         
        self.story_txt = Text(self, width = 75, height = 10, wrap= WORD)
        self.story_txt.grid(row=65, column = 0, columnspan = 4)
        
    def tell_story(self):
        """Fill text boxes with new story input."""
         #get values from GUI
        car = int(self.car_ent.get())
        apt = int(self.apt_ent.get())
        jet = int(self.jet_ent.get())
        gift = int(self.gift_ent.get())
        #story = "TOTAL: "
        story = 0
        story += car
        story += apt
        story += jet 
        story += gift 
         
        #self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)   
        self.story_txt.insert(10.0, " all is well that ends well")    
       
# car = input("Lamborghini Tune-Ups: ")
# car = int(car)
# 
# rent = int(input("Manhattan Apartment: "))
# jet = int(input("Private Jet Rental: "))
# gifts = int(input("Gifts: "))
# food = int(input("Dining Out: "))
# staff = int(input("Staff (butlers, chef, driver, assistant): "))
# guru = int(input("Personal Guru and Coach: ") )
# games = int(input("Computer Games: "))
# expense=int(input("Tuition: "))

#total = car + rent + jet + gifts + food + staff + guru + games + expense

#print("\nGrand Total:", total)

       
#main
root = Tk()
root.title("RICH MAN PROBLEMS")
app = Application(root)
root.mainloop()
