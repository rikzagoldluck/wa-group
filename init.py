import webbrowser as web
import pyautogui as pg
import time
import calendar

def sendwhatmsg_to_group(group_id: str) -> None:

    curr = time.localtime()
    date = "%s, %s-%s-%s" % (calendar.day_name[curr.tm_wday], curr.tm_mday, curr.tm_mon, curr.tm_year)
    time_write = "%s:%s:%s" % (curr.tm_hour, curr.tm_min, curr.tm_sec)

    
    whats = pg.getWindowsWithTitle("WhatsApp")
    
    if (len(whats) == 0):
        web.open('https://web.whatsapp.com/accept?code=' + group_id)
        time.sleep(5)
        whats = pg.getWindowsWithTitle("WhatsApp")[0]
        time.sleep(5)
    else:
        whats = whats[0]
    
    width, height = pg.size()

    whats.maximize()
    whats.activate()
    time.sleep(1)
    pg.click(width / 2, height - height / 10)
    pg.typewrite("Tanggal : " + date)
    pg.hotkey('shift', 'enter') 
    pg.typewrite("Jam : " + time_write)
    pg.hotkey('shift', 'enter') 
    pg.typewrite('Mesin E24 : *Mati*\n')

sendwhatmsg_to_group("F5s3eZzMEOhKMBJI70XTCL")