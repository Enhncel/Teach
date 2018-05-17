import webbrowser
import time
total_break = 3
break_count = 0
print("This Program start on"+time.ctime())
while(break_count<total_break):
    time.sleep(5)
    webbrowser.open('www.baidu.com')
    break_count+=1
