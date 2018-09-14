import json
filename = 'reviews_Books_5.json'
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
fp = open(filename,'r')
for line in fp:
  json_obj = json.loads(line.strip())
  clean_review = process_line(json_obj['reviewText'])
  print clean_review


