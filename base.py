from colorama import init, Fore, Back, Style
from PIL import ImageGrab, ImageOps
import colorMap.mapper as cmap
import pyautogui as pya
import os, time, sys
init(autoreset=True)

class color:
     PURPLE='\033[95m'
     CYAN='\033[96m'
     DARKCYAN='\033[36m'
     BLUE='\033[94m'
     GREEN='\033[92m'
     YELLOW='\033[93m'
     RED='\033[91m'
     BOLD='\033[1m'
     UNDERLINE='\033[4m'
     END='\033[0m'
     PINK='\033[105m'
     TURTLE='\033[106m'
     LIGHT_GRAY="\033[0;37m"
     DARK_GRAY="\033[1;30m"
     BLACK="\033[0;30m"
     FAINT="\033[2m"
     LIGHT_WHITE="\033[1;37m"

height=25
width=100

frameData=[]

def renderFrame():
     frameText=""
     lastColor=""
     for item in frameData:
          try:
               if item=="NEWLINE":
                    frameText=frameText+"\n"+Fore.RESET
               else:
                    colorName=cmap.findName(str(item[0]))
                    colorName=colorName.lower()
                    if colorName=="black":
                         frameText=frameText+" "
                    elif colorName=="dgrey":
                         if lastColor==colorName:
                              frameText=frameText+"■"
                         else:
                              frameText=frameText+color.DARK_GRAY+"■"
                    elif colorName=="grey":
                         frameText=frameText+"■"
                    elif colorName=="lgrey":
                         if lastColor==colorName:
                              frameText=frameText+"■"
                         else:
                              frameText=frameText+color.LIGHT_GRAY+"■"
                    elif colorName=="llgrey":
                         if lastColor==colorName:
                              frameText=frameText+"■"
                         else:
                              frameText=frameText+color.FAINT+"■"
                    elif colorName=="white":
                         if lastColor==colorName:
                              frameText=frameText+"■"
                         else:
                              frameText=frameText+color.LIGHT_WHITE+"■"
                    else:
                         frameText=frameText+" "
                    lastColor=colorName
          except Exception as exep:
               print("Error: "+str(exep))
               frameText=frameText+" "
     os.system("cls")
     print(frameText+color.END)

while True:
     colorsToAdd=[]
     frameData=[]
     image=ImageGrab.grab().convert('LA').load()
     # 1. (192,792,30)
     # 2. (105,1365,20)
     for pixelIdY in range(192,792,15):
          for pixelIdX in range(105,1365,10):
               frameData.append(image[pixelIdX,pixelIdY])
          frameData.append("NEWLINE")
     renderFrame()
     time.sleep(0.1)
