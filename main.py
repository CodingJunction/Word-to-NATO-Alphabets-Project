import pandas
d={}
f=pandas.read_csv("nato_letters.csv")
for (index,row) in f.iterrows():
    d[row.letter]=row.code

ip=input("Enter the word:\n").upper()
n=[]
for i in ip:
    n.append(d[i])
    

print(n)
