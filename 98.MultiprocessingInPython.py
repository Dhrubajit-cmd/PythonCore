# In this class we shall learn about MultiProcessing in Python.
'''
Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel. It allows you to take advantage of multiple cores or processors on your
system and can significantly improve the performance of your code. In this class ,we'll take a closer look at the multiprocessing module and its various functions and how they
can be used in Python.
'''

import multiprocessing
import requests
def downloadFile(url,name):
  print(f"Started downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
url =  "https://picsum.photos/id/1/200/300"
pros = []
for i in range(5000000):
    # downloadFile(url,i)
    p = multiprocessing.Process(target = downloadFile , args = [url , i])
    p.start()
    pros.append(p)
for p in pros :
    p.join()