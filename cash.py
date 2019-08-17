a = {"year":2019, "month":8, "balance":600000}
current = []
current.append({'year':2019, 'month':8, 'expence':40000, 'item':'cost'})
current.append({'year':2019, 'month':8, 'expence':77600, 'item':'land'})
current.append({'year':2019, 'month':8, 'expence':70000, 'item':'life'})
current.append({'year':2019, 'month':8, 'income':200000, 'item':'publisher'})

result8 = a["balance"] - sum([i['expence'] for i in current if 'expence' in i])+ sum([i['income'] for i in current if 'income' in i])
print(r"result 8 : ", result8)

planA = []
planA.append({'year':2019, 'month':9, 'income':100000, 'item':'personal'})
planA.append({'year':2019, 'month':9, 'income':200000, 'item':'publisher'})
planA.append({'year':2019, 'month':12, 'income':200000, 'item':'publisher'})
planA.append({'year':2019, 'month':12, 'income':100000, 'item':'personal'})
planA.append({'year':2019, 'month':10, 'income':150000, 'item':'personal'})
planA.append({'year':2019, 'month':12, 'income':80000, 'item':'dojin'})
planA.append({'year':2019, 'month':10, 'expence':60000, 'item':'print'})
planA.append({'year':2019, 'month':12, 'expence':160000, 'item':'cost'})
planA.append({'year':2019, 'month':12, 'expence':77600*4, 'item':'land'})
planA.append({'year':2019, 'month':12, 'expence':70000*4, 'item':'life'})

resultA = a["balance"] - sum([i['expence'] for i in current if 'expence' in i])+ sum([i['income'] for i in current if 'income' in i])- sum([i['expence'] for i in planA if 'expence' in i])+ sum([i['income'] for i in planA if 'income' in i])
print("result A : ", resultA)

planB = []
planB.append({'year':2019, 'month':9, 'income':100000, 'item':'personal'})
planB.append({'year':2019, 'month':9, 'income':200000, 'item':'publisher'})
planB.append({'year':2019, 'month':12, 'income':300000, 'item':'personal'})
planB.append({'year':2019, 'month':10, 'income':150000, 'item':'personal'})
planB.append({'year':2019, 'month':12, 'income':80000, 'item':'dojin'})
planB.append({'year':2019, 'month':10, 'expence':60000, 'item':'print'})
planB.append({'year':2019, 'month':12, 'expence':160000, 'item':'cost'})
planB.append({'year':2019, 'month':12, 'expence':77600*4, 'item':'land'})
planB.append({'year':2019, 'month':12, 'expence':70000*4, 'item':'life'})

resultB = a["balance"] - sum([i['expence'] for i in current if 'expence' in i])+ sum([i['income'] for i in current if 'income' in i])- sum([i['expence'] for i in planB if 'expence' in i])+ sum([i['income'] for i in planB if 'income' in i])
print("result B : ", resultB)