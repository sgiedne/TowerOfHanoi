from node import Node
import toh
'''
Worked by Siddharath Muthukumaran (SME0261) & Santhosh Subramanian (SSL4520)
This file calls following search techniques
	1. Depth First Search
	2. Breadth First Search
	3. Best First Search
'''
ip = [[1,2,3,4],[],[]]
op = [[],[4],[1,2,3]]

root = Node()
root.state = ip
toh.bestfs(root,op)