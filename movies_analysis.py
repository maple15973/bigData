import sqlite3

conn = sqlite3.connect('movies.db')
c = conn.cursor()

#Each userId avg_var
def user():
  sql = "SELECT USERID, AVG(SCORE),AVG(SCORE*SCORE)-AVG(SCORE)*AVG(SCORE) FROM MOVIE GROUP BY USERID"
  c.execute(sql)
  results = c.fetchall()
  print("========EACH USERID AVG, VAR========")
  for row in results:
    print("USERID: "+str(row[0])+", AVG: "+str("%.3f " % row[1])+", VAR: "+str("%.3f " % row[2]))

#Each productId avg
def product():
  sql = "SELECT PRODUCTID, AVG(SCORE),AVG(SCORE*SCORE)-AVG(SCORE)*AVG(SCORE) FROM MOVIE GROUP BY PRODUCTID"
  c.execute(sql)
  results = c.fetchall()
  print("\n========EACH PRODUCTID AVG, VAR========")
  for row in results:
    print("PRODUCTID: "+str(row[0])+", AVG: "+str("%.3f " % row[1])+", VAR: "+str("%.3f " % row[2]))

#All score Avg, Var
def score():
  sql = "SELECT AVG(SCORE),AVG(SCORE*SCORE)-AVG(SCORE)*AVG(SCORE) FROM MOVIE"
  c.execute(sql)
  results = c.fetchall()
  print("\n========SCORE's AVG, VAR========")
  for row in results:
    print("AVG: "+str("%.3f" % row[0])+", VAR: "+str("%.3f " % row[1]))


user()
product()
score()
