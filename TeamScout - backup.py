from tkinter import *
import os
import csv

def main(Team_Num):
    def csvGet():
        global filename
        Team_File = Team_Num + ".tab"
        filename = os.path.abspath(os.path.join("TeamScout Teams",Team_File))
        global Team_Attrib
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile,delimiter="\t")
            for row in readCSV:
                pass#print(row)
        Team_Attrib = row
    csvGet()

    print("Opening",filename)

    window = Tk()
    window.title("TeamScout")
    window.geometry("1000x300")

    A1 = Team_Attrib[1]
    A2 = Team_Attrib[2]
    B1 = Team_Attrib[3]
    B2 = Team_Attrib[4]
    C1 = Team_Attrib[5]
    C2 = Team_Attrib[6]
    D1 = Team_Attrib[7]
    D2 = Team_Attrib[8]
    LB = Team_Attrib[9]

    AR = Team_Attrib[10]#Auto Reach
    AC = Team_Attrib[11]#Auto Cross
    AB = Team_Attrib[12]#Auto Boulder

    LG = Team_Attrib[13]#Teleop Low Goal
    HG = Team_Attrib[14]#Teleop High Goal
    ST = Team_Attrib[15]#Teleop Scale Tower
    DAA1 = Team_Attrib[16]
    DAA2 = Team_Attrib[17]
    DAC1 = Team_Attrib[18]
    DAC2 = Team_Attrib[19]
    

    Team_Focus = Team_Attrib[20]
    global regFoul
    regFoul = Team_Attrib[21]
    global techFoul
    techFoul = Team_Attrib[22]
    global yelFoul
    yelFoul = Team_Attrib[23]
    global redFoul
    redFoul = Team_Attrib[24]
    Strategy = Team_Attrib[25]
    Comments = Team_Attrib[26]

    def save(Team_Attrib):
        print("Saving",filename)
        print("Saved!")
        #Defense Crossings
        Team_Attrib[1] = A1.get()
        Team_Attrib[2] = A2.get()
        Team_Attrib[3] = B1.get()
        Team_Attrib[4] = B2.get()
        Team_Attrib[5] = C1.get()
        Team_Attrib[6] = C2.get()
        Team_Attrib[7] = D1.get()
        Team_Attrib[8] = D2.get()
        Team_Attrib[9] = LB.get()
        #Autonomous
        Team_Attrib[10] = AR.get()
        Team_Attrib[11] = AC.get()
        Team_Attrib[12] = AB.get()
        #Teleoperated
        Team_Attrib[13] = LG.get()
        Team_Attrib[14] = HG.get()
        Team_Attrib[15] = ST.get()
        #DA = str(DAA1.get())+str(DAA2.get())+str(DAC1.get())+str(DAC2.get())
        Team_Attrib[16] = DAA1.get()
        Team_Attrib[17] = DAA1.get()
        Team_Attrib[18] = DAA1.get()
        Team_Attrib[19] = DAA1.get()
        #General Team
        Team_Attrib[20] = TF.get()
        Team_Attrib[21] = regFoul
        Team_Attrib[22] = techFoul
        Team_Attrib[23] = yelFoul
        Team_Attrib[24] = redFoul
##        Team_Attrib[18] = str(regFoul)+str(techFoul)+str(yelFoul)+str(redFoul)         #string/list?
##        Team_Attrib[18] = str(regFoul.get())+str(techFoul.get())+str(yelFoul.get())+str(redFoul.get())         #string/list?
        if entStrategy.get() != "":
            Team_Attrib[25] += entStrategy.get()      #string
        if entComments.get() != "":
            Team_Attrib[26] += entComments.get()      #string
        print(Team_Attrib)
        #with open(filename,"w") as csvfile:
        csvfile = open(filename,"w")
        for i in range(0,27):
            k = str(Team_Attrib[i])
            csvfile.write(k)
            if i != 27:
                csvfile.write('\t')
        csvfile.close()
        window.destroy()
        
        

    lblTeamNum = Label(window, text="Team "+Team_Num)
    #Defenses
    A1 = IntVar()
    A1.set(Team_Attrib[1])
    cA1 = Checkbutton(window, text="Portcullis", var=A1)
    A2 = IntVar()
    A2.set(Team_Attrib[2])
    cA2 = Checkbutton(window, text="Cheval de Frise", var=A2)
    B1 = IntVar()
    B1.set(Team_Attrib[3])
    cB1 = Checkbutton(window, text="Moat", var=B1)
    B2 = IntVar()
    B2.set(Team_Attrib[4])
    cB2 = Checkbutton(window, text="Ramparts", var=B2)
    C1 = IntVar()
    C1.set(Team_Attrib[5])
    cC1 = Checkbutton(window, text="Drawbridge", var=C1)
    C2 = IntVar()
    C2.set(Team_Attrib[6])
    cC2 = Checkbutton(window, text="Sally Port", var=C2)
    D1 = IntVar()
    D1.set(Team_Attrib[7])
    cD1 = Checkbutton(window, text="Rock Wall", var=D1)
    D2 = IntVar()
    D2.set(Team_Attrib[8])
    cD2 = Checkbutton(window, text="Rough Terrain", var=D2)
    LB = IntVar()
    LB.set(Team_Attrib[9])
    cLB = Checkbutton(window, text="Low Bar", var=LB)
    #Autonomous
    AR = IntVar()
    AR.set(Team_Attrib[10])
    cAR = Checkbutton(window, text="Autonomous Reach", var=AR)
    AC = IntVar()
    AC.set(Team_Attrib[11])
    cAC = Checkbutton(window, text="Autonomous Cross", var=AC)
    lblAB = Label(window, text="Boulder in ___ goal")
    AB = IntVar()
    AB.set(Team_Attrib[12])
    ABList = [("None","0"),("Low","1"),("High","2")]
    row = 5
    for (text,mode) in ABList:
        rbAB = Radiobutton(window, text=text, variable=AB, value=mode)
        rbAB.grid(row=row,column=1,sticky=W)
        row += 1
    #Teleop
    lblLG = Label(window, text="Low Goal Capabilities")
    LG = IntVar()
    LG.set(Team_Attrib[13])
    LGList = [("Incapable","0"),("Capable","1"),("Often","2")]
    row = 2
    for (text,mode) in LGList:
        rbHG = Radiobutton(window, text=text, variable=LG, value=mode)
        rbHG.grid(row=row,column=2,sticky=W)
        row += 1
    lblHG = Label(window, text="High Goal Capabilities")
    HG = IntVar()
    HG.set(Team_Attrib[14])
    HGList = [("Incapable","0"),("Capable","1"),("Often","2"),("Accurate","3")]
    row = 6
    for (text,mode) in HGList:
        rbHG = Radiobutton(window, text=text, variable=HG, value=mode)
        rbHG.grid(row=row,column=2,sticky=W)
        row += 1
    ST = IntVar()
    ST.set(Team_Attrib[15])
    cST = Checkbutton(window, text="Scale Tower", var=ST)
    
    lblDA = Label(window, text="Assisted others with defenses:")
    DAA1 = IntVar()
    DAA1.set(Team_Attrib[16])
    cDAA1 = Checkbutton(window, text="Portcullis", var=DAA1)
    DAA2 = IntVar()
    DAA2.set(Team_Attrib[17])
    cDAA2 = Checkbutton(window, text="Cheval de Frise", var=DAA2)
    DAC1 = IntVar()
    DAC1.set(Team_Attrib[18])
    cDAC1 = Checkbutton(window, text="Drawbridge", var=DAC1)
    DAC2 = IntVar()
    DAC2.set(Team_Attrib[19])
    cDAC2 = Checkbutton(window, text="Sally Port", var=DAC2)

    lblTF1 = Label(window, text="Team's Primary Focus")
    lblTF2 = Label(window, text="(what they are best at overall)")
    TF = IntVar()
    TF.set(Team_Attrib[17])
    TFList = [("Boulders","0"),("Defenses","1"),("Offense","2"),("Defense","3")]
    row = 3
    for (text,mode) in TFList:
        rbTF = Radiobutton(window, text=text, variable=TF, value=mode)
        rbTF.grid(row=row,column=4,sticky=W)
        row += 1

    def regFoulChange(var,num):
        global regFoul
        regFoul = int(var)
        if regFoul >= 1 or num == 1:
            regFoul += num
        lblRegFoulNum.configure(text=regFoul)
        
    def techFoulChange(var,num):
        global techFoul
        techFoul = int(var)
        if techFoul >= 1 or num == 1:
            techFoul += num
        lblTechFoulNum.configure(text=techFoul)
        
    def yelFoulChange(var,num):
        global yelFoul
        yelFoul = int(var)
        if yelFoul >= 1 or num == 1:
            yelFoul += num
        lblYelFoulNum.configure(text=yelFoul)
        
    def redFoulChange(var,num):
        global redFoul
        redFoul = int(var)
        if redFoul >= 1 or num == 1:
            redFoul += num
        lblRedFoulNum.configure(text=redFoul)
    
    text = "Fouls ("+str(regFoul)+")"
    lblRegFoul = Label(window, text=text)
    sub1 = Button(window, text="-1", command= lambda: regFoulChange(regFoul,-1))
    lblRegFoulNum = Label(window, text=regFoul)
    add1 = Button(window, text="+1", command= lambda: regFoulChange(regFoul,1))
    lblRegFoul.grid(row=1,column=5,columnspan=3)
    sub1.grid(row=2,column=5,sticky=W)
    lblRegFoulNum.grid(row=2,column=6)
    add1.grid(row=2,column=7,sticky=W)
    
    text = "Tech Fouls ("+str(techFoul)+")"
    lblTechFoul = Label(window, text=text)
    sub1 = Button(window, text="-1", command= lambda: techFoulChange(techFoul,-1))
    lblTechFoulNum = Label(window, text=techFoul)
    add1 = Button(window, text="+1", command= lambda: techFoulChange(techFoul,1))
    lblTechFoul.grid(row=3,column=5,columnspan=3)
    sub1.grid(row=4,column=5,sticky=W)
    lblTechFoulNum.grid(row=4,column=6)
    add1.grid(row=4,column=7,sticky=W)

    text = "Yellow Cards ("+str(yelFoul)+")"
    lblYelFoul = Label(window, text=text)
    sub1 = Button(window, text="-1", command= lambda: yelFoulChange(yelFoul,-1))
    lblYelFoulNum = Label(window, text=yelFoul)
    add1 = Button(window, text="+1", command= lambda: yelFoulChange(yelFoul,1))
    lblYelFoul.grid(row=5,column=5,columnspan=3)
    sub1.grid(row=6,column=5,sticky=W)
    lblYelFoulNum.grid(row=6,column=6)
    add1.grid(row=6,column=7,sticky=W)

    text = "Red Cards ("+str(redFoul)+")"
    lblRedCard = Label(window, text=text)
    sub1 = Button(window, text="-1", command= lambda: redFoulChange(redFoul,-1))
    lblRedFoulNum = Label(window, text=redFoul)
    add1 = Button(window, text="+1", command= lambda: redFoulChange(redFoul,1))
    lblRedCard.grid(row=7,column=5,columnspan=3)
    sub1.grid(row=8,column=5,sticky=W)
    lblRedFoulNum.grid(row=8,column=6)
    add1.grid(row=8,column=7,sticky=W)

    lblStrategy = Label(window,text="Strategy")
    lblStrategy.grid(row=1,column=8)
    entStrategy = Entry(window)
    entStrategy.grid(row=2,column=8)
    lblComments = Label(window,text="Comments")
    lblComments.grid(row=3,column=8)
    entComments = Entry(window)
    entComments.grid(row=4,column=8)

    btnSave = Button(window, text="Save", command= lambda: save(Team_Attrib))

    #entLowBar = Entry(window)

    lblTeamNum.grid(row=0,column=0,sticky=W)

    cA1.grid(row=1,column=0,sticky=W)
    cA2.grid(row=2,column=0,sticky=W)
    cB1.grid(row=3,column=0,sticky=W)
    cB2.grid(row=4,column=0,sticky=W)
    cC1.grid(row=5,column=0,sticky=W)
    cC2.grid(row=6,column=0,sticky=W)
    cD1.grid(row=7,column=0,sticky=W)
    cD2.grid(row=8,column=0,sticky=W)
    cLB.grid(row=9,column=0,sticky=W)

    cAR.grid(row=1,column=1,sticky=W)
    cAC.grid(row=2,column=1,sticky=W)
    lblAB.grid(row=4,column=1,sticky=W)

    lblLG.grid(row=1,column=2,sticky=W)
    lblHG.grid(row=5,column=2,sticky=W)

    cST.grid(row=1,column=3,sticky=W)
    lblDA.grid(row=2,column=3,sticky=W)
    cDAA1.grid(row=3,column=3,sticky=W)
    cDAA2.grid(row=4,column=3,sticky=W)
    cDAC1.grid(row=5,column=3,sticky=W)
    cDAC2.grid(row=6,column=3,sticky=W)

    lblTF1.grid(row=1,column=4)
    lblTF2.grid(row=2,column=4,sticky=W)

    #lblStrat.grid(row=

    #entLowBar.pack()
    btnSave.grid(row=0,column=5)
    
    window.mainloop()

Team_Num = str(input("Enter Team Number: "))
while Team_Num != "0":
    main(Team_Num)
    Team_Num = str(input("Enter Team Number: "))
