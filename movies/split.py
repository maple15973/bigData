SIZE_HINT = 100000000

fileNumber = 0
with open("movie_split/movies.txt", "rt", encoding='utf-8', errors='ignore') as f:
  while True:
    buf = f.readlines(SIZE_HINT)
    if not buf:
      # we've read the entire file in, so we're done
      break
    outFile = open("movie_split/movie%d.txt" % fileNumber, "wt")
    outFile.write(''.join(buf))
    outFile.close()
    fileNumber += 1 
    print(str(fileNumber))
