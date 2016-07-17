import sqlite3
import gc

RECORD_NUM=10
RECORD_SIZE=8
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
  def productId():
    return self.productId
  def userId():
    return self.userId
  def score():
    return self.score

def processing(r,raw):
  for data in raw:
    r.assign_data(data)

def separate_data(data):
  print(data.split())

conn = sqlite3.connect('movies.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS MOVIE(USERID TEXT, SCORE decimal(3,1) , PRODUCTID TEXT)''')
print("Connect table successfully!")

head=[]
counter=0
maxcounter=0
with open("movies.txt", "r",encoding='utf-8', errors='ignore') as myfile:
  for line in myfile:
    print(str(counter)+"  "+line)
    head.append(line)
    counter+=1
    maxcounter+=1
    if counter%9==0:
      r = Record()
      processing(r,head)
      #r.printRecord()
      c.execute('INSERT INTO MOVIE(USERID, PRODUCTID, SCORE) VALUES("'+r.userId+'","'+str(r.productId)+'","'+str(r.score)+'")')
      conn.commit()
      counter=0
      del head
      gc.collect()
      head=[]
    if maxcounter==8000:
      break
