

# install pip ; sudo apt-get install python-pip javac n3-pip

import os
import os.path
import math
import sys
import numpy
import random

def main():
    if os.path.exists('mydata.csv'):
        f = open('mydata.csv')
        md = f.readlines()
        rl =(list(map(lambda l: list(map(float, l.split(',')[2:3])), md)))
        xval =(list(map(lambda l: list(map(float, l.split(',')[:2])), md)))
        xs= numpy.matrix(xval)
        ys= numpy.matrix(rl)
        w = [random.uniform(0,1),random.uniform(0,1)]
        w = numpy.matrix(w)
        kappa = 1
        temp = 0
        n = 0
        print (ys)
        
        for j in range(1000):
            x = 0;
            if(j>0):
                temp = error
            error = 0;
            for i in range(len(rl)):
                 x +=numpy.multiply(ys[i]-w.dot(xs[i].transpose()),xs[i])
                 error += math.pow(ys[i]-w.dot(xs[i].transpose()),2)
                 
            error = error/2*len(rl)
            w=w+(kappa*x/len(rl))
            print(temp)
            if(round(error,5) == round(temp,5)):
                break
            n += 1
        
        print (w)
        print (n)
        
main()
