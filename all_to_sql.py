import sqlite3,gc,time
from multiprocessing import Process

#q = Queue.Queue()
class Record:
  productId=""
  userId=""
  score=0
  productTitle=""
  def __init__(self):
    self.productId=""
    self.userId=""
    self.score=0.0
    self.productTitle=""
  def assign_data(self,data):
    split= data.split()
    if split:
      if split[0].find('product/productId:')!=-1:
        self.productId = split[1];
      elif split[0].find('review/userId:')!=-1:
        self.userId = split[1]
      elif split[0].find('review/score:')!=-1:
        self.score = float(split[1])
      elif split[0].find('product/title:')!=-1:
        self.productTitle = ' '.join(split[1:])
  def printRecord(self):
    print("ProductId: "+ self.productId)
    print("UserId: "+ self.userId)
    print("Score: "+ str(self.score))
    print("Title: "+ self.productTitle)
  def productId():
    return self.productId
  def userId():
    return self.userId
  def score():
    return self.score

def processing(head):
  r = Record()
  for data in head:
    r.assign_data(data)
  #q.put(r)
  r.printRecord()
  c.execute('INSERT INTO PRODUCT(USERID, PRODUCTID, SCORE, PRODUCTTITLE) VALUES("'+r.userId+'","'+str(r.productId)+'","'+str(r.score)+'","'+str(r.productTitle)+'")')
  conn.commit()

conn = sqlite3.connect('all.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS PRODUCT(USERID TEXT, SCORE decimal(3,1) , PRODUCTID TEXT, PRODUCTTITLE TEXT)''')
print("Connect table successfully!")

head=[]
counter=0
maxcounter=0
with open("all.txt", "r",encoding='utf-8', errors='ignore') as myfile:
  for line in myfile:
    head.append(line)
    counter+=1
    maxcounter+=1
    if counter%11==0:
      p = Process(target=processing, args=(head,))
      p.start()
      counter=0
      head=[]
    if maxcounter==11000:
      break
