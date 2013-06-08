# Source File Name: slotmachine_V_1_0.py
# Author's Name: Jordan Cooper
# Last Modified By: Jordan Cooper
# Date Last Modified: Friday, June 7, 2013
""" 
  Program Description:  This program will replicate a standard slotmachine with a graphical user interface
                        created using tkinter. The player will be able to choose from 3 levels of betting
                        $10 , $100 , and $1000. 

        Version: 1.1    -properly placed buttons
                        -placed and created lables to display jackpot,balance, and bet
                        -bet now subtracts from money (upon spin)
                        -created a second frame to hold the buttons
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
        self.credit = 1000
        self.jackpot = 500
        
        button_width = 6 
        button_padx = "2m" 
        button_pady = "1m" 
        buttons_frame_padx = "7m" 
        buttons_frame_pady = "3m" 
        buttons_frame_ipadx = "0m" 
        buttons_frame_ipady = "0m"

        self.myParent = parent
        #creates a frame whose parent is root
        self.myContainer1 = Canvas(parent, width = 600, height = 1000, bg="white")
        #pack the frame - show it on the screen
        self.myContainer1.pack(expand=YES,fill=BOTH)
        self.myContainer_Image = PhotoImage(file="Images/SlotMachineBackground.gif")
        self.myContainer1.create_image(0,0, image = self.myContainer_Image, anchor = NW)
        

        self.button_Frame = Frame(self.myContainer1) 
        self.button_Frame.pack(side=BOTTOM, 
                               ipadx=buttons_frame_ipadx,
                               ipady=buttons_frame_ipady,
                               padx=buttons_frame_padx,
                               pady=buttons_frame_pady,
                              )
         
        
#        add the user's lables to visually show current bet, current jackpot, current
        self.yourBetLabel = Label(self.myContainer1)
        self.yourBetLabel.configure(text="Your Bet: $" + str(self.bet) , background="white", width=12, anchor = NW)
        #display yourBetLabel
        self.yourBetLabel.place(x= 200, y= 450)
        
        self.yourMoneyLabel = Label(self.myContainer1)
        self.yourMoneyLabel.configure(text="Money: $" + str(self.credit) , background="white", width=12, anchor = NW)
        #display yourMoneyLabel
        self.yourMoneyLabel.place(x= 300, y= 450)
        
        self.yourJackpotLabel = Label(self.myContainer1)
        self.yourJackpotLabel.configure(text="Jackpot: $" + str(self.jackpot) , background="white", width=12, anchor = NW)
        #display yourJackpotLabel
        self.yourJackpotLabel.place(x= 100, y= 450)
        
#----------------------------------------------------------------------------------------------------------BUTTONS--       
        #the bet10Button attributes
        self.bet10Button = Button(self.button_Frame)
        self.bet10Button.configure(text="Bet 10", background="green")
        self.bet10Button.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        self.bet10Button.pack(side=LEFT)
        #Bind bet10Button with bet10ButtonClick
        self.bet10Button.bind("<Button-1>", self.bet10ButtonClick)
#-------------------------------------------------------------------------------------------Bet 10


        #the bet100Button attributes
        self.bet100Button = Button(self.button_Frame)
        self.bet100Button.configure(text="Bet 100", background="green")
        self.bet100Button.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        #display bet100Button
        self.bet100Button.pack(side=LEFT)
        #Bind bet100Button with bet100ButtonClick
        self.bet100Button.bind("<Button-1>", self.bet100ButtonClick)
#------------------------------------------------------------------------------------------Bet 100       

 
        #the bet1000Button attributes
        self.bet1000Button = Button(self.button_Frame)
        self.bet1000Button.configure(text="Bet 1000", background="green")
        #display bet1000Button
        self.bet1000Button.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        self.bet1000Button.pack(side=LEFT)
        #Bind bet1000Button with bet1000ButtonClick
        self.bet1000Button.bind("<Button-1>", self.bet1000ButtonClick)
#------------------------------------------------------------------------------------------Bet 1000
        
        
        
        #the spinButton attributes
        self.spinButton = Button(self.button_Frame)
        self.spinButton.configure(text="Spin!", background="green")
        self.spinButton.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        #display spinButton
        self.spinButton.pack(side=LEFT)
        #Bind spinButton with spinButtonClick
        self.spinButton.bind("<Button-1>", self.spinButtonClick)
#------------------------------------------------------------------------------------------SPIN        
        

        #the quitButton attributes
        self.quitButton = Button(self.button_Frame)
        self.quitButton.configure(text="Quit", background="red", state="disabled")
        self.quitButton.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        #display quitButton
        self.quitButton.pack(side=RIGHT)
        #Bind quitButton with quitButtonClick
        self.quitButton.bind("<Button-1>", self.quitButtonClick)
#----------------------------------------------------------------------------------------------------------BUTTONS--     


    #change the default bet (0) to $10
    def bet10ButtonClick(self,bet): 
        self.bet = 10
        self.yourBetLabel.configure(text = "Your Bet: $" + str(self.bet))
        
        return self.bet
        
    #change the default bet (0) to $100
    def bet100ButtonClick(self,bet): 
        self.bet = 100
        self.yourBetLabel.configure(text = "Your Bet: $" + str(self.bet))
        
        return self.bet
        
    #change the default bet (0) to $1000
    def bet1000ButtonClick(self,bet):        
        self.bet = 1000
        self.yourBetLabel.configure(text = "Your Bet: $" + str(self.bet) )
        
        return self.bet
    
    #Let the user Play the game
    def spinButtonClick(self, bet):   
        self.credit = self.credit - self.bet
        self.yourMoneyLabel.configure(text = "Money: $" + str(self.credit) )
        
    #close GUI 
    def quitButtonClick(self, event):
        self.myParent.destroy()

def main():
    
    canvasDimensions = "600x800"
    #create a top-level window
    root = Tk()    
    #Set your dimensions for the canvas
    
    root.geometry(canvasDimensions)
    
    #call the slotMachine class
    slotmachine = slotMachine(root)
    #execute the mainloop method of the "root" object
    root.mainloop()

if __name__ == "__main__": main()