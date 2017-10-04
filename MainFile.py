from node import Node
from dfs import call_dfs
from bfs import call_bfs
'''
Worked by Siddharath Muthukumaran (SME0261) & Santhosh Subramanian (SSL4520)
This file calls following search techniques
	1. Depth First Search
	2. Breadth First Search
	3. Best First Search

Fields:
ip - input state - list of list [[],[],[]]
op - output state - list of list [[],[],[]]
'''

#dfs - input
#ip = [[1,2],[3],[]]
#end = [[],[],[1,2,3]]

#bfs - input
ip = [[1,2,],[3,4],[]]
end = [[],[],[1,2,3,4]]

#call dfs
call_dfs(ip, end)

#call bfs
#call_bfs(ip, end)

#call best first seach method
#toh.bestfs(root,op)

