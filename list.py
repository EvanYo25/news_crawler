data = [{'tags':[],'title':'none'} for x in range(10)]
data[5]['title'] = "hello"
data[5]['tags'].append("hello")
data[5]['tags'].append("hi")
del data[6:10]
print (data)