def increment(n):
    return n+1
def square(n):
    return n*n
def imperative (initial, goal):
    list_functions=[(" increment", increment),(" square", square)]
    candidates=[(str(initial), initial)]
    for x in range (goal-initial+1):
        newCandidates=[]
        for (action,result) in candidates:
            for (a, r) in list_functions:
                newCandidates.append((action+a,r(result)))
                if newCandidates[-1][1]==goal:
                    return newCandidates[-1][0]
        candidates=newCandidates
        
class Node:
    def __init__(self, parent, action, result):
        self.parent=parent
        self.action=action
        self.result=result
    def path(self):
        if self.parent==None:
            return [(self.action, self.result)]
        else:
            return self.parent.path()+[(self.action, self.result)]

def objective(initial, goal):
    start=[Node(None, None, initial)]
    for x in range (goal-initial+1):
            parent=start[0]
            start=start[1:]
            for (a,r) in [(" increment", increment), (" square", square)]:
                newNode=Node(parent,a, r(parent.result))
                if newNode.result==goal:
                    return newNode.path()
                else:
                    start=start+[newNode]
