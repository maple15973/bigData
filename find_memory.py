import sqlite3,gc,time

head=[]
counter=0
with open("movies.txt", "r",encoding='utf-8', errors='ignore') as myfile:
  for line in myfile:
    head.append(line)
    counter+=1
    if counter%9==0:
      s=''.join(head)
      f= open('test.txt','w')
      f.write(s)
      f.close()
      break
