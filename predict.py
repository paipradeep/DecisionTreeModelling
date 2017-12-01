import treeBuilder as tb
import draw as dw

def findResult(t,root):
    """To recurrively find the prediction for input tuple 't' based on already Built
       decision Tree"""
    #root = buildTree(my_data)
    if root.prediction != None:
        print root.prediction
    else:
        col = root.column
        val = root.splitValue
        if isinstance(val,int) or isinstance(val,float):
            res = tb.decide1(t,col,val)
        else:
            res = tb.decide2(t,col,val)
        if res:
            findResult(t,root.tChild)
        else:
            findResult(t,root.fChild)

def predictor(dataset,tple,header,title):
    """Builds the decision Tree, generates png and predicts result based upon
       input tuple and training dataset"""
    root = tb.buildTree(dataset)
    dw.drawTree(root,header,title)
    findResult(tple,root)
