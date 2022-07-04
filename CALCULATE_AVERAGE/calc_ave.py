inplist = open('inpls.txt', 'r').read()
inplist=list(map(int, inplist.split()))
average = sum(inplist)/len(inplist)
gpa = average * 0.04

print(f'Average: {average}')
print(f'GPA: {gpa}')
