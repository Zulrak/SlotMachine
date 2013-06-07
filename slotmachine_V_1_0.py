# Source File Name: slotmachine_V_1_0.py
# Author's Name: Jordan Cooper
# Last Modified By: Jordan Cooper
# Date Last Modified: Friday, June 7, 2013
""" 
  Program Description:  This program will replicate a standard slotmachine with a graphical user interface
                        created using tkinter. The player will be able to choose from 3 levels of betting
                        $10 , $100 , and $1000. 

        Version: 1.0    - Created a background image, placed in in the canvas
                        - Created the betting buttons,spin button and cancle button
                        - Added functionality to the betting buttons (Not all of the functionality)
                        - Completed the Cancle button
"""

# import statements
import random
#import the Tkinter library so that it is available for use
from Tkinter import *

#create the slotMachine Class
class slotMachine():
    #define the attributes of the class
    def __init__(self, parent):
        
        
        self.bet = 0
        
        self.myParent = parent
        #creates a frame whose parent is root
        self.myContainer1 = Canvas(parent, width = 600, height = 1000, bg="white")
        #pack the frame - show it on the screen
        self.myContainer1.pack(expand=YES,fill=BOTH)
        self.myContainer_Image = PhotoImage(file="Images/SlotMachineBackground.gif")
        self.myContainer1.create_image(0,0, image = self.myContainer_Image, anchor = NW)
        
        self.yourBetLabel = Label(self.myContainer1)
        self.yourBetLabel.configure(text="Your Bet: $" + str(self.bet) , background="white")
        #display yourBetLabel
        self.yourBetLabel.pack(side=LEFT)
        
#----------------------------------------------------------------------------------------------------------BUTTONS--       
        #the bet10Button attributes
        self.bet10Button = Button(self.myContainer1)
        self.bet10Button.configure(text="Bet 10", background="green")
        #display bet10Button
        self.bet10Button.pack(side=LEFT)
        #Bind bet10Button with bet10ButtonClick
        self.bet10Button.bind("<Button-1>", self.bet10ButtonClick)
        
        #the bet100Button attributes
        self.bet100Button = Button(self.myContainer1)
        self.bet100Button.configure(text="Bet 100", background="green")
        #display bet100Button
        self.bet100Button.pack(side=LEFT)
        #Bind bet100Button with bet100ButtonClick
        self.bet100Button.bind("<Button-1>", self.bet100ButtonClick)
        
        #the bet1000Button attributes
        self.bet1000Button = Button(self.myContainer1)
        self.bet1000Button.configure(text="Bet 1000", background="green")
        #display bet1000Button
        self.bet1000Button.pack(side=LEFT)
        #Bind bet1000Button with bet1000ButtonClick
        self.bet1000Button.bind("<Button-1>", self.bet1000ButtonClick)
        
        #the spinButton attributes
        self.spinButton = Button(self.myContainer1)
        self.spinButton.configure(text="Spin!", background="green")
        #display spinButton
        self.spinButton.pack(side=LEFT)
        #Bind spinButton with spinButtonClick
        self.spinButton.bind("<Button-1>", self.spinButtonClick)

        #the quitButton attributes
        self.quitButton = Button(self.myContainer1)
        self.quitButton.configure(text="Quit", background="red", state="disabled")
        #display quitButton
        self.quitButton.pack(side=RIGHT)
        #Bind quitButton with quitButtonClick
        self.quitButton.bind("<Button-1>", self.quitButtonClick)
#----------------------------------------------------------------------------------------------------------BUTTONS--     
    #change the default bet (0) to $10
    def bet10ButtonClick(self, bet): 
        self.bet = 10
        self.yourBetLabel.configure(text = "Your Bet: $" + str(self.bet))
        
    #change the default bet (0) to $100
    def bet100ButtonClick(self, bet): 
        self.bet = 100
        self.yourBetLabel.configure(text = "Your Bet: $" + str(self.bet))
        
    #change the default bet (0) to $1000
    def bet1000ButtonClick(self, bet):        
        self.bet = 1000
        self.yourBetLabel.configure(text = "Your Bet: $" + str(self.bet) )
    
    #Let the user Play the game
    def spinButtonClick(self, event):        
        bacon = "filler"
        
    #close GUI 
    def quitButtonClick(self, event):
        self.myParent.destroy()

def main():
    
    canvasDimensions = "512x307"
    #create a top-level window
    root = Tk()    
    #Set your dimensions for the canvas
    
    root.geometry(canvasDimensions)
    
    #call the slotMachine class
    slotmachine = slotMachine(root)
    #execute the mainloop method of the "root" object
    root.mainloop()

if __name__ == "__main__": main()