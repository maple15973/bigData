import sqlite3,gc,time
from multiprocessing import Process

class Record:
  productId=""
  userId=""
  score=0
  def __init__(self):
    self.productId=""
    self.userId=""
    self.score=0.0
  def assign_data(self,data):
    split= data.split()
    if split:
      if split[0].find('product/productId:')!=-1:
        self.productId = split[1];
      elif split[0].find('review/userId:')!=-1:
        self.userId = split[1]
      elif split[0].find('review/score:')!=-1:
        self.score = float(split[1])
  def printRecord(self):
    print("ProductId: "+ self.productId)
    print("UserId: "+ self.userId)
    print("Score: "+ str(self.score)) 

def processing(head,conn,c):
  r = Record()
  for data in head:
    r.assign_data(data)
  r.printRecord()
  c.execute('INSERT INTO MOVIE(USERID, PRODUCTID, SCORE) VALUES("'+r.userId+'","'+str(r.productId)+'","'+str(r.score)+'")')
  conn.commit()

def check_first(myfile):
  counter = 1
  for line in myfile:
    split = line.split()
    if split:
      if split[0].find('product/productId')!=-1:
        return counter
      else:
        counter+=1

def open_file(index):
  conn = sqlite3.connect('movies_test.db')
  c=conn.cursor()
  head =[]
  counter=0
  maxcounter=0
  checkfirst=False
  filename = 'movie_split/movie'+str(index)+'.txt'
  with open(filename, "r",encoding='utf-8', errors='ignore') as myfile:
    num = check_first(myfile)
  with open(filename, "r",encoding='utf-8', errors='ignore') as myfile:
    for line in myfile:
      maxcounter+=1
      if maxcounter<=num:
        continue
      head.append(line)
      counter+=1
      if counter%9==0:
        processing(head,conn,c)
        gc.collect()
        head=[]
    c.close()
    del c
    conn.close()

conn = sqlite3.connect('movies_test.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS MOVIE(USERID TEXT, SCORE decimal(3,1) , PRODUCTID TEXT)''')
print("Connect table successfully!")
c.close()
del c
conn.close()

for i in range(0, 1):
  p = Process(target = open_file, args=(i,))
  p.start()

