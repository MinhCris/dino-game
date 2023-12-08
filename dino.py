# import pyautogui
# pyautogui.displayMousePosition()


import pyautogui
import time
import keyboard

while True:
	im = pyautogui.screenshot()
    screen = im.getpixel((300,300))
     x1= im.getpixel((610,262))
    x2= im.getpixel((550,262))
    x3= im.getpixel((640,262))
    x4=im.getpixel((500,262))
    
    y1=im.getpixel((570,240))
    y2= im.getpixel((600,240))
    y3=im.getpixel((575,240))
    y4=im.getpixel((535,300))
    
    if screen[0]== 255:
        if x1[0]!= 255 or x2[0] != 255 or x3[0]!=255 or x4[0] != 255 or y1[0] != 255 or y2[0] != 255 or y3[0] != 255  or y4[0] != 255 :
            pyautogui.press("space")
            time.sleep(0.0001)
            
    else:
        if x1[0]!=0 or x2[0] != 0 or x3[0] != 0 or x4[0] != 0 or y1[0] != 0 or y2[0] != 0 or y3[0] != 0 or y4[0] != 0:
            pyautogui.press("space")
            time.sleep(0.0001)
            
            
    if keyboard.is_pressed('s'):
		break
	else:
    	pass