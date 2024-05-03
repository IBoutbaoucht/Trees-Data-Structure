print("")
Tree = [7,[5,[4,None,None],[6,None,None]],[9,[8,None,None],[10,None,None]]]
A = Tree
while A : 
  col = A.pop()
  print(col[0])
  A.append(col[1])
  A.append(col[2])
  
