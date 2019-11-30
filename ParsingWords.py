import re
f= open("../data_exapmle.txt","r")
string_a = "yo what up, you are my dude!" # example string
res = re.findall(r'\w+',f) # parsing words
print(str(res)) # print