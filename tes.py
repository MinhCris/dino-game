import pyautogui
import time
import keyboard

while True:
    im = pyautogui.screenshot()
    screen = im.getpixel((300, 300))
    x1 = im.getpixel((610, 262))
    x2 = im.getpixel((550, 262))
    x3 = im.getpixel((640, 262))
    x4 = im.getpixel((500, 262))             
      
    y1 = im.getpixel((570, 240))
    y2 = im.getpixel((600, 240))
    y3 = im.getpixel((575, 240))
    y4 = im.getpixel((535, 300))

    # Điều kiện mới để tránh lỗi
    if (
        screen[0] == 255 and
        any(pixel[0] != 255 for pixel in [x1, x2, x3, x4, y1, y2, y3, y4])
    ) or (
        screen[0] != 255 and
        any(pixel[0] != 0 for pixel in [x1, x2, x3, x4, y1, y2, y3, y4])
    ):
        pyautogui.press("space")
        time.sleep(0.0001)

    if keyboard.is_pressed("s"):    
        break
    else:
        pass
