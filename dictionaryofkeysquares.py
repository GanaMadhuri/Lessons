custdict={}
trydict={}
k= int(input("enter the no of ranges"))
for i in range(1,k):
    custdict[i]=i*i
print(custdict)

trialdict={"e":"10","h":"20"}
newdict={"k":"1","J":"10","f":"20"}
print(newdict)
custdict.update(trialdict)
print(custdict)
trialdict.update(custdict)
print(trialdict)

mary={"mary1":"carry","mary2":"carry2"}
lamb={"lamb1":"sfh","lamb2":"ajdkfh"}
mary.update(lamb)
print(mary)