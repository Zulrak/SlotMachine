# Source File Name: slotmachine_V_1_0.py
# Author's Name: Jordan Cooper
# Last Modified By: Jordan Cooper
# Date Last Modified: Friday, June 7, 2013
""" 
  Program Description:  This program will replicate a standard slotmachine with a graphical user interface
                        created using tkinter. The player will be able to choose from 3 levels of betting
                        $10 , $100 , and $1000. 

        Version: 1.2    -Created the reel lables, they now output the BLANK option by default 
                        -worked on the spinn function to output reward
                        - correct output displayed in text form
                        - pictures not linked to reel
                        - reset button created
                        
                        
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
        buttons_frame_padx = "0m" 
        buttons_frame_pady = "67m" 
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
        self.yourbetLabel = Label(self.myContainer1)
        self.yourbetLabel.configure(text="Your bet: $" + str(self.bet) , background="white", width=12, anchor = NW)
        #display yourbetLabel
        self.yourbetLabel.place(x= 200, y= 450)
        
        self.yourMoneyLabel = Label(self.myContainer1)
        self.yourMoneyLabel.configure(text="Money: $" + str(self.credit) , background="white", width=12, anchor = NW)
        #display yourMoneyLabel
        self.yourMoneyLabel.place(x= 300, y= 450)
        
        self.yourJackpotLabel = Label(self.myContainer1)
        self.yourJackpotLabel.configure(text="Jackpot: $" + str(self.jackpot) , background="white", width=12, anchor = NW)
        #display yourJackpotLabel
        self.yourJackpotLabel.place(x= 100, y= 450)
        
        self.reel1 = Label(self.myContainer1)
        self.reel1.configure(height = 113, width = 84)
        self.reel1Image = PhotoImage(file="Images/blank.gif")
        self.reel1.configure(image=self.reel1Image)
        #display reel1
        self.reel1.place(x= 155, y= 300)
        
        self.reel2 = Label(self.myContainer1)
        self.reel2.configure(height = 113, width = 84)
        self.reel2Image = PhotoImage(file="Images/blank.gif")
        self.reel2.configure(image=self.reel2Image)
        #display reel1
        self.reel2.place(x= 255, y= 300)
        
        self.reel3 = Label(self.myContainer1)
        self.reel3.configure(height = 113, width = 84)
        self.reel3Image = PhotoImage(file="Images/blank.gif")
        self.reel3.configure(image=self.reel3Image)
        #display reel1
        self.reel3.place(x= 355, y= 300)
        
        
        
#----------------------------------------------------------------------------------------------------------BUTTONS--       
        #the bet10Button attributes
        self.bet10Button = Button(self.button_Frame)
        self.bet10Button.configure(text="bet 10", background="green")
        self.bet10Button.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        self.bet10Button.pack(side=LEFT)
        #Bind bet10Button with bet10ButtonClick
        self.bet10Button.bind("<Button-1>", self.bet10ButtonClick)
#-------------------------------------------------------------------------------------------bet 10


        #the bet100Button attributes
        self.bet100Button = Button(self.button_Frame)
        self.bet100Button.configure(text="bet 100", background="green")
        self.bet100Button.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        #display bet100Button
        self.bet100Button.pack(side=LEFT)
        #Bind bet100Button with bet100ButtonClick
        self.bet100Button.bind("<Button-1>", self.bet100ButtonClick)
#------------------------------------------------------------------------------------------bet 100       

 
        #the bet1000Button attributes
        self.bet1000Button = Button(self.button_Frame)
        self.bet1000Button.configure(text="bet 1000", background="green")
        #display bet1000Button
        self.bet1000Button.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        self.bet1000Button.pack(side=LEFT)
        #Bind bet1000Button with bet1000ButtonClick
        self.bet1000Button.bind("<Button-1>", self.bet1000ButtonClick)
#------------------------------------------------------------------------------------------bet 1000
        
        
        
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
        
        #the resetButton attributes
        self.resetButton = Button(self.button_Frame)
        self.resetButton.configure(text="Reset", background="red", state="disabled")
        self.resetButton.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )
        #display resetButton
        self.resetButton.pack(side=RIGHT)
        #Bind resetButton with quitButtonClick
        self.resetButton.bind("<Button-1>", self.resetButtonClick)



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
        self.yourbetLabel.configure(text = "Your bet: $" + str(self.bet))
        
        return self.bet
        
    #change the default bet (0) to $100
    def bet100ButtonClick(self,bet): 
        self.bet = 100
        self.yourbetLabel.configure(text = "Your bet: $" + str(self.bet))
        
        return self.bet
        
    #change the default bet (0) to $1000
    def bet1000ButtonClick(self,bet):        
        self.bet = 1000
        self.yourbetLabel.configure(text = "Your bet: $" + str(self.bet) )
        
        return self.bet
    
    #Let the user Play the game
    def spinButtonClick(self, win):   
        
        if (self.bet> self.credit):
            self.spinButton.configure(state="disabled")
        else:
            self.spinButton.configure(state="normal")
            self.credit = self.credit - self.bet
            self.yourMoneyLabel.configure(text = "Money: $" + str(self.credit) )
            
            self.jackpot +=(int(self.bet*.15))
            self.yourJackpotLabel.configure(text = "Jackpot: $" + str(self.jackpot) )
            pullthehandle(self.bet, self.credit, self.jackpot)
            
            if win: 
                self.yourMoneyLabel.configure(text = "Money: $" + str(self.credit) )
    
    #rest GUI 
    def resetButtonClick(self, event):
        self.bet = 0
        self.credit = 1000
        self.jackpot = 500
        
        self.yourbetLabel.configure(text = "Your bet: $" + str(self.bet) )
        self.yourJackpotLabel.configure(text = "Jackpot: $" + str(self.jackpot) )
        self.yourMoneyLabel.configure(text = "Money: $" + str(self.credit) )
        
        self.reel1.configure(image=self.reel2Image)
        self.reel2.configure(image=self.reel2Image)
        self.reel3.configure(image=self.reel2Image)
        
        return(self.bet,self.credit,self.jackpot)
    
    #close GUI 
    def quitButtonClick(self, event):
        self.myParent.destroy()
        

#Tom's Code------------------------------------------------      
def Reels():
    """ When this function is called it determines the bet_Line results.
        e.g. Bar - Orange - Banana """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            bet_Line[spin] = "Blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            bet_Line[spin] = "Grapes"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            bet_Line[spin] = "Banana"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            bet_Line[spin] = "Orange"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            bet_Line[spin] = "Cherry"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            bet_Line[spin] = "Bar"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            bet_Line[spin] = "Bell"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            bet_Line[spin] = "Seven"    

    
    return bet_Line

def pullthehandle(bet, credit, jackpot):
    """ This function takes the Player's bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    credit -= bet
    jackpot += (int(bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    Fruit_Reel = Reels()
    Fruits = Fruit_Reel[0] + " - " + Fruit_Reel[1] + " - " + Fruit_Reel[2]
    
    # Match 3
    if Fruit_Reel.count("Grapes") == 3:
        winnings,win = bet*20,True
    elif Fruit_Reel.count("Banana") == 3:
        winnings,win = bet*30,True
    elif Fruit_Reel.count("Orange") == 3:
        winnings,win = bet*40,True
    elif Fruit_Reel.count("Cherry") == 3:
        winnings,win = bet*100,True
    elif Fruit_Reel.count("Bar") == 3:
        winnings,win = bet*200,True
    elif Fruit_Reel.count("Bell") == 3:
        winnings,win = bet*300,True
    elif Fruit_Reel.count("Seven") == 3:
        print("Lucky Seven!!!")
        winnings,win = bet*1000,True
    # Match 2
    elif Fruit_Reel.count("Blank") == 0:
        if Fruit_Reel.count("Grapes") == 2:
            winnings,win = bet*2,True
        if Fruit_Reel.count("Banana") == 2:
            winnings,win = bet*2,True
        elif Fruit_Reel.count("Orange") == 2:
            winnings,win = bet*3,True
        elif Fruit_Reel.count("Cherry") == 2:
            winnings,win = bet*4,True
        elif Fruit_Reel.count("Bar") == 2:
            winnings,win = bet*5,True
        elif Fruit_Reel.count("Bell") == 2:
            winnings,win = bet*10,True
        elif Fruit_Reel.count("Seven") == 2:
            winnings,win = bet*20,True
    
        # Match Lucky Seven
        elif Fruit_Reel.count("Seven") == 1:
            winnings, win = bet*10,True
            
        else:
            winnings, win = bet*2,True
    if win:    
        print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
        credit += int(winnings)
        
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(jackpot) + "prize! \n")
            jackpot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
    else:
        print(Fruits + "\nPlease try again. \n")
    
    return credit, jackpot, win
#Tom's Code -----------------------------------------------------------------------------------------------

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