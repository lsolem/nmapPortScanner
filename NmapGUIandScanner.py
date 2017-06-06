#!/usr/bin/env python3

import os
import sys
import time
from tkinter import *



class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        ##Labels
        self.lbl1 = Label(self, text = "Hostname/IP/Range/Subnet to Target")
        self.lbl1.grid(row = 0, column = 0, sticky =W)

        self.lbl2 = Label(self, text = "Number of Ports to Scan Ex(1-65535) or specific port Ex(22)")
        self.lbl2.grid(row = 2, column = 0, sticky = W)

        self.lbl3 = Label(self, text = "Optional Scan Configuration")
        self.lbl3.grid(row = 4, column = 0, sticky = W)
        
        
        ##StatusBar
        self.statusBar = Label(root, text = "Checking the Status", bd = 1, relief = SUNKEN, anchor=W)
        self.statusBar.grid(row = 10, columnspan = 3)


        ##Entries
        self.ent1 = Entry(self, width = 30)
        self.ent1.grid(row = 1, column = 0, sticky = W)

        self.ent2 = Entry(self, width = 30)
        self.ent2.grid(row = 3, column = 0, sticky = W)
        
        ##Variables
        self.checkBox1 = BooleanVar()
        self.checkBox2 = BooleanVar()
        self.checkBox3 = BooleanVar()
        self.checkBox4 = BooleanVar()

        ##Checkboxes
        Checkbutton(self, text = "IPv6 Addressing (-6)", variable = self.checkBox1
                    ).grid(row = 5, column = 0, sticky = W)
        
        Checkbutton(self, text = "Disable Intial Ping (-Pn option)", variable = self.checkBox2
                    ).grid(row = 6, column = 0, sticky = W)
        
        Checkbutton(self, text = "OS Detection (-O option)", variable = self.checkBox3
                    ).grid(row = 7, column = 0, sticky = W)
        
        Checkbutton(self, text = "Perform Tracerout (--traceroute option)", variable = self.checkBox4
                    ).grid(row = 8, column = 0, sticky = W)
        
        ##Buttons
        self.bttn1 = Button(self, text = "Press to run test (-p)", command = self.get_nmap)
        self.bttn1.grid(row = 9, column = 0, sticky = W)
        
        self.bttn2 = Button(self, text = "End Scan", command = self.pauseScan)
        self.bttn2.grid(row = 11, column = 0, sticky = W)
        
        self.bttn3 = Button(self, text = "Press to run fast scan (-F)",  command = self.nmapFast)
        self.bttn3.grid(row = 10, column = 0, sticky = W)
        
        ##TextBox
        self.txt = Text(self, width = 70, height = 12, wrap = WORD)
        self.txt.grid(row = 12)
        
 
    def nmapFast(self):
        #Runs fast scan test
        options = "-F"
        ip = self.ent1.get()
        
        if self.checkBox1.get() == True:
            options += " -6"
        if self.checkBox2.get() == True:
            options += " -Pn"
        if self.checkBox3.get() == True:
            options += " -O"
        if self.checkBox4.get() == True:
            options += " --traceroute"
        
        
        command = "nmap " + options + "  " + ip
        process = os.popen(command)
        print(options)
        
        results = str(process.read())
        
        print(results)
        
        saveData = open("NmapScanData.txt","w")
        saveData.write(results)
        saveData.close()
        
        self.txt.delete(0.0,END)
        self.txt.insert(0.0, results)
        return results
    
    
    def get_nmap(self):
        #Runs test for specific ports identified.
        options = "-p"
        ip = self.ent1.get()
        numPorts = self.ent2.get()
        options += numPorts
        
        if self.checkBox1.get() == True:
            options += " -6"
        if self.checkBox2.get() == True:
            options += " -Pn"
        if self.checkBox3.get() == True:
            options += " -O"
        if self.checkBox4.get() == True:
            options += " --traceroute"
            
        
        
        command = "nmap " + options + "  " + ip
        process = os.popen(command)
        
        print(options)
        
        results = str(process.read())
        print(results)
        
        saveData = open("NmapScanData.txt","w")
        saveData.write(results)
        saveData.close()
        
        self.txt.delete(0.0,END)
        self.txt.insert(0.0, results)
        
        return results
    
    def pauseScan(self):
        #Currently ends the scan and closes the GUI
        sys.exit()
        

        

        
        
        


#Root
root = Tk()
root.title("Lukes Port Scanner")
root.geometry("500x550")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()