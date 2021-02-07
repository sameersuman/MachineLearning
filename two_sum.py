#!/usr/bin/env python
def two_sum():

    #a = [2,7,11,15]

    #target = 9

    a = [-3,6,7,10]

    target = 4

    for i in range(len(a)):
      
        #print(a[i])
        f= target - a[i]
        #print(f)
        for j in range(i+1,len(a)):
            print(a[j])
            if f == a[j]:
                print(f"Value found two sum : {j},{i}")
                return
               
       

two_sum()    