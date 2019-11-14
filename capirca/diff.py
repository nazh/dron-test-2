import sys
import re

listnew=[]
listold=[]
listnewi=[]
listoldi=[]
newacl=sys.argv[1]
oldacl=sys.argv[2]
acldiff=sys.argv[3]

with open (newacl, 'r') as newacl:
    for line in newacl:
        if not line.strip(): continue
        listnew.append(line)

with open (oldacl, 'r') as oldacl:
    for line in oldacl:
        if not line.strip(): continue
        listold.append(line)

i=1
for line in listnew:
    newline=line.replace('access-list GLOBAL_ACL', 'access-list GLOBAL_ACL line '+str(i))
    listnewi.append(newline)
    i+=1
#print(listnewi)
i=1
for line in listold:
    newline=line.replace('access-list GLOBAL_ACL', 'access-list GLOBAL_ACL line '+str(i))
    listoldi.append(newline)
    i+=1
#print(listoldi)

#print('==========')

with open (acldiff, 'w') as acetar:

    acetar.write('Lines to remove on ASA: \n')
    for lineold in listold:
        if lineold not in listnew:
#            print('Line to remove: ',lineold, end =" ")
            lntorm=re.match('access-list GLOBAL_ACL (.*)',lineold).group(1)
            for line in listoldi:
                if lntorm in line:
                    rmline=line.replace('access-list', 'no access-list')
#                    print('Run on asa to remove below ACE: ', rmline )
                    acetar.write(rmline)

    acetar.write('Lines to add on ASA: \n')
    for linenew in listnew:
        if linenew not in listold:
#            print('Lines to add on ASA: ',linenew, end =" ")
            lntoadd=re.match('access-list GLOBAL_ACL (.*)',linenew).group(1)
            for addline in listnewi:
                if lntoadd in addline:
#                    print('Run on asa to add below ACE: ', addline )
                    acetar.write(addline)



