from tkinter import *
from tkinter import messagebox

import time

root = Tk()

root.withdraw()

root.attributes("-topmost", True)

while(True):
    time.sleep(2)
    pipeline = open("pipeline.txt", 'r')

    message = pipeline.read()


    # If the text is 'stop' then turn off microservice and clear text file
    if message == 'stop':
        pipeline.close()
        pipeline = open("pipeline.txt", 'w')
        break

    # If there is text in the text file, display text as a notification
    # Then clear text file.
    if message != '':
        messagebox.showinfo("Notification", message)
        pipeline.close()
        pipeline = open("pipeline.txt", 'w')
    
    


