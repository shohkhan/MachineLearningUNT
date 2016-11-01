#COMMAND: python3 HW2.py
import math
import collections

dl = ['Origin','Manufacturer','Color','Model']
nodes = []

def readAllData():
    dict = collections.defaultdict()
    ori = []
    man = []
    col = []
    mod = []
    tag = []
    f = open('decision_tree_input', 'r')
    for l in f.readlines():
        i = l.split(" ")
        ori.append(i[0])
        man.append(i[1])
        col.append(i[2])
        mod.append(i[3])
        tag.append(i[4][0])
    dict['Origin'] = ori
    dict['Manufacturer'] = man
    dict['Color'] = col
    dict['Model'] = mod
    dict['Tag'] = tag
    return dict
    
def getCount(arr, text):
    count = 0
    for i in arr:
        if str(i) == str(text):
            count += 1
    return count
    
def getUniques(arr):
    a = []
    for i in arr:
        if i in a: pass
        else: a.append(i)
    return a
    
def getTag(arr, text, tag):
    tag1 = []
    for i in range(len(arr)):
        if str(arr[i]) == str(text):
            tag1.append(tag[i])
    return tag1
    
    
def entropy(tag):
    pos = getCount(tag,'+')
    neg = getCount(tag,'-')
    t = pos + neg
    d1 = pos/t
    d2 = neg/t
    lg1 = 0
    if (pos > 0): lg1 = math.log((pos/t),2)
    lg2 = 0
    if (neg > 0): lg2 = math.log((neg/t),2)
    ent = -d1*lg1 - d2*lg2
    if ent != 0:
        return ent
    else:
        return 0

    
def getIG(tag, ori, debbb= False):
    cval = []
    S = tag
    if debbb: print(S)
    Hs = entropy(S)
    if debbb: print(Hs)
    uniques = getUniques(ori)
    for u in uniques:
        Su = getTag(ori, u, tag)
        Hu = entropy(Su)
        print ("Entropy for '" + str(u) + "': " + str(Hu))
        cval.append(Hu * len(Su) / len(S))

    IGi = Hs
    for i in cval:
        IGi -= i

    return IGi
    

def getNextNode(ds, dl, debbb = False):
    name = ''
    maxval = 0
    for n in dl:
        print("Considering the feature: '" + str(n) + "'")
        igo = getIG(ds['Tag'], ds[n], debbb)
        if igo == maxval:
            name += ", " + n
        elif igo > maxval:
            maxval = igo
            name = n
        print ("Information Gain (IG) for '"+ n +"' is: " + str(igo))
        print("----------------------------------------------")
    print ("Maximum IG for this node is " + str(maxval) + " (" + name +")")
    return name

dataset = readAllData()

print ("Calculations for Root Node:")
print("----------------------------------------------")
rootnode = getNextNode(dataset, dl)
sa = dataset[rootnode] #selectedarray


print("----------------------------------------------")
toconsider = []
for v in getUniques(sa):
    if getCount(sa, v) > 1:
        toconsider.append(v)
    else:
        print("Only one possible label for '" + str(v) + "', which will be considered as a leaf.")
print("----------------------------------------------")
for t in toconsider:
    print("Branches will be considered for " + str(rootnode) + ": " + str(t))
print("----------------------------------------------")

dl2 = []
for d in dl:
    if d == rootnode: pass
    else: dl2.append(d)

for tc in toconsider:
    dataset2 = collections.defaultdict()
    ori = []
    col = []
    mod = []
    tag = []
    for m in range(len(sa)):
        if sa[m] == tc:
            ori.append(dataset['Origin'][m])
            col.append(dataset['Color'][m])
            mod.append(dataset['Model'][m])
            tag.append(dataset['Tag'][m])

    dataset2['Origin'] = ori
    dataset2['Color'] = col
    dataset2['Model'] = mod
    dataset2['Tag'] = tag
    print("Considering " + str(tc))
    print("----------------------------------------------")
    nnode = getNextNode(dataset2, dl2)













