#Create a function that moves n number of rings 
#from source to destination using helper tower

def hanoi(n, source, destination, helper):
    if n > 0:
        #print "before step1", (source,destination,helper)
        hanoi(n-1, source, helper, destination)
        #print ("After step 1"), (source,destination,helper)
        destination.append(source.pop())
        #print ("After step 2"), (source,destination,helper)
        hanoi((n-1), helper,destination,source)
        #print ("After step 3"), (source,destination,helper)
        pass



T1 = [ 1,2,3,4,5]
T2 = []
T3 = []
hanoi(5, T1,T2,T3)
print "T1, T2, T3 are" , (T1,T2,T3)