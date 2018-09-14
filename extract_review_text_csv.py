import csv
filename = 'amazon_review_corpus_75k.csv'
def process_line(line):
  line = line.replace("....", " ")
  line = line.replace("...", " ")
  line = line.replace("..", " ")
  line = line.replace('"', " ")
  line = line.replace(',', " ")
  line = line.replace(':', " ")
  line = line.replace('+', " ")
  line = line.replace('!', " ")
  line = line.replace('@', " ")
  line = line.replace('#', " ")
  line = line.replace('$', " ")
  line = line.replace('^', " ")
  line = line.replace('%', " ")
  line = line.replace('&', " ")
  line = line.replace('*', " ")
  line = line.replace('(', " ")
  line = line.replace(')', " ")
  line = line.replace('{', " ")
  line = line.replace('}', " ")
  line = line.replace('[', " ")
  line = line.replace(']', " ")
  line = line.replace('~', " ")
  line = line.replace('-', " ")
  #print line
  return line

  return line
csvfile = open(filename,'r')
fp=csv.reader(csvfile, delimiter='\t')
for line in fp:
  review = line[3]
  clean_review = process_line(review)
  print clean_review


