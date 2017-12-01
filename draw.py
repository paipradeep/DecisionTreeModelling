from graphviz import Digraph
import treeBuilder as tree
h = []
def drawTreeRecur(root,string,d):
	
	if root == None:
		return
	if root.prediction != None:
		return
	else:
		T = root.tChild
		F = root.fChild
		stringT = " "
		stringF = " "
		if T.prediction != None:
			stringT = T.prediction
			d.edge(string,stringT,color="green")

		else:
			if(isinstance(T.splitValue,int) or isinstance(T.splitValue,float)):
				stringT = h[T.column] + ">=" + str(T.splitValue) + "?"
			else:
				stringT = h[T.column] + "=" + str(T.splitValue) + "?"
			d.edge(string,stringT,color="green")
			drawTreeRecur(T,stringT,d)


		if F.prediction != None:
			stringF = F.prediction
			d.edge(string,stringF,color="red")

		else:
			if(isinstance(F.splitValue,int) or isinstance(F.splitValue,float)):
				stringF = h[F.column] + ">=" + str(F.splitValue) + "?"
			else:
				stringF = h[F.column] + "=" + str(F.splitValue) + "?"
			d.edge(string,stringF,color="red")
			drawTreeRecur(F,stringF,d)




def drawTree(root,headers,title):
	global h
	h = headers
	#root = tree.buildTree(data)
	d = Digraph(format="png")
	if root != None:
		d.name = "Decision Tree"
		d.filename = title + ".gv"
		string = " "
		if(isinstance(root.splitValue,int) or isinstance(root.splitValue,float)):
			string = headers[root.column] + ">=" + str(root.splitValue) + "?"
		else:
			string = headers[root.column] + "=" + root.splitValue + "?"
		d.node(string)
		drawTreeRecur(root,string,d)
		d.render()
