import time
import webbrowser
i = 0

print("This program started on " +time.ctime())

while i < 3:
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=PXkLmHw8bJU")
    i = i + 1
