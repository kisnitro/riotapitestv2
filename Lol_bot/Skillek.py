import sys
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *
from Moves import ReleaseKey, PressKey, Q, W, E, R, CTRL




class Coordinates ():
#1980x1080 & medium
#region
    Lvlup_Q = (815, 955)
    Lvlup_W = (865, 967)
    Lvlup_E = (910, 965)
    Lvlup_R = (958, 965)
#endregion

#region
    Toplane_basic = (1681, 855)
    Midlane_basic = (1780, 942)
    Botlane_basic = (1870, 1032)

    Toplane_early = (1735, 832)
    Midlane_early = (1815, 910)
    Botlane_early = (1890, 975)
    
    Toplane_midgame = (1800, 835)
    Midlane_midgame = (1830, 890)

    Midlane_lategame = (1890, 833)
#endregion

#region Skillek
def Skill_levelup_Q ():
            PressKey(CTRL) #Ctrl
            time.sleep(0.5)
            PressKey(Q) #Q
            time.sleep(0.5)
            ReleaseKey(Q)
            time.sleep(0.5)
            ReleaseKey(CTRL)
            print("Skill_Q_leveled")

def Skill_levelup_W ():
            PressKey(CTRL) #Ctrl
            time.sleep(0.5)
            PressKey(W) #Q
            time.sleep(0.5)
            ReleaseKey(W)
            time.sleep(0.5)
            ReleaseKey(CTRL)
            print("Skill_W_leveled")

def Skill_levelup_E ():
            PressKey(CTRL) #Ctrl
            time.sleep(0.5)
            PressKey(E) #Q
            time.sleep(0.5)
            ReleaseKey(E)
            time.sleep(0.5)
            ReleaseKey(CTRL)
            print("Skill_E_leveled")

def Skill_levelup_R ():
            PressKey(CTRL) #Ctrl
            time.sleep(0.5)
            PressKey(R) #Q
            time.sleep(0.5)
            ReleaseKey(R)
            time.sleep(0.5)
            ReleaseKey(CTRL)
            print("Skill_R_leveled")
#endregion

#region ImageGrab

def imageGrab_Q ():
    
    boxq = (808, 957, 833, 975)
    imageq = ImageGrab.grab(boxq)
    grayImageq = ImageOps.grayscale(imageq)
    q = array(grayImageq.getcolors())
    print(q.sum())
    return(q.sum())

def imageGrab_W ():
    
    boxw = (853, 958, 877, 977)
    imagew = ImageGrab.grab(boxw)
    grayImagew = ImageOps.grayscale(imagew)
    w = array(grayImagew.getcolors())
    print(w.sum())
    return(w.sum())

def imageGrab_E ():
    
    boxe = (899, 958, 924, 977)
    imagee = ImageGrab.grab(boxe)
    grayImagee = ImageOps.grayscale(imagee)
    e = array(grayImagee.getcolors())
    print(e.sum())
    return(e.sum())

def imageGrab_R ():
    
    boxr = (945, 958, 970, 977)
    imager = ImageGrab.grab(boxr)
    grayImager = ImageOps.grayscale(imager)
    r = array(grayImager.getcolors())
    print(r.sum())
    return(r.sum())

#endregion


def skillsystem():
        SkillQ = 3
        SkillW = 3
        SkillE = 3
        SkillR = 3
        Kikapcs = 0
        while True:
            if(SkillQ == 1 and SkillW == 1 and SkillE == 1 and SkillR == 1):
                break

            if(imageGrab_Q() == 19117):
                SkillQ = 0
                print("Q can be level up")
            elif(imageGrab_Q() == 1722):
                SkillQ = 1
                print("Q maxed")


            if(imageGrab_W() == 19343 and SkillQ == 1):
                SkillW = 0
                print("W can be level up")
            elif(imageGrab_W() == 1687):
                SkillW = 1
                print ("W maxed")


            if(imageGrab_E() == 19284 and SkillQ == 1 and SkillW == 1):
                SkillE = 0
                print("E can be level up")
            elif(imageGrab_E() == 1773):
                SkillE = 1
                print("E maxed")

            if(imageGrab_R() == 19284 and SkillQ == 1 and SkillW == 1 and SkillE == 1):
                SkillR = 0
                print("R can be level up")
            elif(Kikapcs == 3):
                SkillR = 1
                print("R maxed")


            if (SkillQ == 3 and SkillW == 3 and SkillE == 3 and SkillE == 3 or SkillQ == 0 and SkillW == 3 and SkillE == 3 and SkillR == 3):
                imageGrab_Q()
            if (SkillQ == 1 and SkillW == 3 and SkillE == 3 and SkillE == 3 or SkillQ == 1 and SkillW == 0 and SkillE == 3 and SkillR == 3):
                imageGrab_W()
            if (SkillQ == 1 and SkillW == 1 and SkillE == 3 and SkillE == 3 or SkillQ == 1 and SkillW == 1 and SkillE == 0 and SkillR == 3):
                imageGrab_E()
            if (SkillQ == 1 and SkillW == 1 and SkillE == 1 and SkillR == 3 or SkillQ == 1 and SkillW == 1 and SkillE == 1 and SkillR == 0):
                imageGrab_R()

            if(SkillQ == 0):
                Skill_levelup_Q()
            elif(SkillQ == 1 and SkillW == 0):
                Skill_levelup_W()
            elif(SkillQ == 1 and SkillW == 1 and SkillE == 0):
                Skill_levelup_E()
            elif(SkillQ == 1 and SkillW == 1 and SkillE == 1 and SkillR == 0):
                Skill_levelup_R()
                Kikapcs += 1
            elif(SkillQ == 1 and SkillW == 1 and SkillE == 1 and SkillR == 1):
                print("All skill maxed")

