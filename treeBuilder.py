import math
from data1 import my_data

class Node:
    def __init__(self,prediction=None,column=-1,tChild=None,fChild=None,splitValue=None):
        """constructor for Node class"""
        self.column = column
        self.tChild = tChild
        self.fChild = fChild
        self.prediction = prediction
        self.splitValue = splitValue
        #self.isLeaf = False

def decide1(row,colNo,value):
    """Decide True or false if value is numerical
       >=   indicates True
       <    indicates False"""
    if(row[colNo]>=value):
        return True
    return False


def decide2(row,colNo,value):
    """Decide True or false if value is other than numerical"""
    if(row[colNo] == value):
        return True
    return False

def splitRows(rows,colNo,value):
    """Splitting of Input dataset based upon its value in Particular Column"""
    trueValues = []
    falseValues = []
    for r in rows:
        if isinstance(value,int) or isinstance(value,float):
            result = decide1(r,colNo,value)
        else:
            result = decide2(r,colNo,value)
        if result:
            trueValues.append(r)
        else:
            falseValues.append(r)
    return (trueValues,falseValues)

def resultCount(rows):
    """To count the occurrence of all possible results"""
    result = {}
    if len(rows) == 0:
        return result
    final = len(rows[0]) - 1
    for r in rows:
        result.setdefault(r[final],0)
        result[r[final]] += 1
    return result

def logbase2(x):
    """log(x) base2"""
    return math.log(x)/math.log(2)

def calculateEntropy(rows):
    """Entropy = freq * log2(freq)
       where freq is the frequency of each possible result"""
    result = resultCount(rows)
    entropy = 0
    for r in result:
        freq = result[r]*1.0/len(rows)
        #print freq
        entropy -= freq * logbase2(freq)
    return entropy

def buildTree(rows):
    """To find the current best Split and build the tree until max gain >0"""
    if len(rows) == 0:
        return Node()
    maxGain = -100
    bestCol = -1
    bestSplitvalue = -1
    children = None
    columnCount = len(rows[0])-1 #the result is excluded
    globalEntropy = calculateEntropy(rows)
    for i in range(0,columnCount):
        colValues = []
        for r in rows:
            if r[i] not in colValues:
                colValues.append(r[i])
        for c in colValues:
            (set1,set2) = splitRows(rows,i,c)
            prob = float(len(set1))/len(rows)
            gain = globalEntropy - prob * calculateEntropy(set1) - (1-prob) * calculateEntropy(set2)
            if gain>maxGain:
                maxGain = gain
                bestCol = i
                bestSplitvalue = c
                children = (set1,set2)
    if maxGain > 0:
        trueRows = buildTree(children[0])
        falseRows = buildTree(children[1])
        newNode = Node(None,bestCol,trueRows,falseRows,bestSplitvalue)
        #print bestSplitvalue
        #print bestCol
        return newNode
    else:

        newNode = Node(rows[0][columnCount])
        return newNode



#uncomment the below code to print Tree on terminal
'''def printtree(tree,indent='',header = None):
    # Is this a leaf node?
    if tree.prediction!=None:
        print str(tree.prediction)
    else:
        # Print the criteria
        print str(tree.column)+':'+str(tree.splitValue)+'? '
        # Print the branches
        print indent+'T->',
        printtree(tree.tChild,indent+'  ')
        print indent+'F->',
        printtree(tree.fChild,indent+'  ')'''

'''root = buildTree(my_data)
printtree(root)'''
'''
