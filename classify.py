import os
import re
import sys
import json
import numpy as np
from tqdm import tqdm
import pickle

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import svm
from sklearn import linear_model
from sklearn.utils import shuffle

from sklearn.model_selection import KFold
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_fscore_support

import libword2vec as emb
import tf_idf
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


def main():
  max_reviews = 20000
  i = 0
  X_raw_all=[]
  rating_all=[]
  helpful_all=[]


  fp = open(filename,'r')
  for line in fp:
    json_obj = json.loads(line.strip())
    review = process_line(json_obj['reviewText'])
    rating = json_obj['overall']
    helpful = json_obj['helpful']
    if(helpful[1]==0):
      helpful_fraction = 0.0
    else:
      helpful_fraction = 1.0*helpful[0]/helpful[1]

    X_raw_all.append(review)
    rating_all.append(rating)
    helpful_all.append(helpful_fraction)
    i = i+1
    if i == max_reviews:break

  #End of the for loop
  fp.close()

  X_all = emb.get_vectors(X_raw_all)
  y_all = [ 0 if i<0.5 else 1 for i in helpful_all ]

  X_all, y_all = shuffle(X_all, y_all)
  X_all = np.array(X_all)
  y_all = np.array(y_all)
  #X_raw_all = np.array(X_raw_all)

  
  print "Total #reviews=", len(X_raw_all), len(helpful_all), len(rating_all)
  kf = KFold(n_splits=10)
  total_f1s=0.0
  total_pre = 0.0
  total_rec = 0.0
  i=0
  for train_index, test_index in kf.split(X_all):
    X_train, X_test = X_all[train_index], X_all[test_index]
    y_train, y_test = y_all[train_index], y_all[test_index]
    #X_raw_train, X_raw_test = X_raw_all[train_index], X_raw_all[test_index]
  
    y_pred = logistic_regression(X_train, y_train, X_test, y_test)
    #y_pred = tf_idf.fit_predict(X_train, y_train, X_test, y_test)
    cm = confusion_matrix(y_test, y_pred)
    print cm
    print( classification_report(y_test, y_pred, digits=4))
    f1s = f1_score(y_test, y_pred, average='macro')
    (pre, rec, f1s,_) = precision_recall_fscore_support(y_test, y_pred, average='weighted')
    print "Iter=", i, "Precision=", pre, "Recall=", rec, "F1-Score=", f1s
    total_f1s += f1s
    total_pre +=pre
    total_rec +=rec
    i += 1
  print "FINAL: P:", round(total_pre/10.0,4), ",R:", round(total_rec/10.0,4), ",F1:", round(total_f1s/10.0,4)


def generate_features(title):
  features=[]
  vecs = emb.get_vector(title)
  features += vecs.tolist()
  return features

def logistic_regression(X_train, y_train, X_test, y_test):
  print("Try logistic regression")
  logistic = linear_model.LogisticRegression()
  logistic.fit(X_train, y_train)
  y_pred = logistic.predict(X_test)
  pickle_file = 'lr_clickbait_model.pickle'
  pickle.dump(logistic, open(pickle_file,"wb"))
  return y_pred

if __name__ == "__main__":
  main()
