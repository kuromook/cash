a = {"year":2019, "month":8, "balance":600000}

current = []
current.append({'year':2019, 'month':8, 'expence':40000, 'item':'cost'})
current.append({'year':2019, 'month':8, 'expence':77600, 'item':'land'})
current.append({'year':2019, 'month':8, 'expence':70000, 'item':'life'})
current.append({'year':2019, 'month':8, 'income':200000, 'item':'publisher'})

def result_balance(balance, plan):
    '''planを適用し、将来の結果を取得'''
    result = balance - sum([i['expence'] for i in plan if 'expence' in i])+ sum([i['income'] for i in plan if 'income' in i])
    return result 

current_balance = result_balance(a['balance'], current)
print(r"result current: ", current_balance)

planA = []
planA.append({'year':2019, 'month':9, 'income':100000, 'item':'personal'})
planA.append({'year':2019, 'month':9, 'income':200000, 'item':'publisher'})
planA.append({'year':2019, 'month':(11,12), 'income':200000, 'item':'publisher'})
planA.append({'year':2019, 'month':(11,12), 'income':100000, 'item':'personal'})
planA.append({'year':2019, 'month':10, 'income':150000, 'item':'personal'})
planA.append({'year':2019, 'month':(11,12), 'income':80000, 'item':'dojin'})
planA.append({'year':2019, 'month':10, 'expence':60000, 'item':'print'})
planA.append({'year':2019, 'month':(11,12), 'expence':160000, 'item':'cost'})
planA.append({'year':2019, 'month':(11,12), 'expence':77600*4, 'item':'land'})
planA.append({'year':2019, 'month':(11,12), 'expence':70000*4, 'item':'life'})

print(r"result A: ", result_balance(current_balance, planA))

planB = []
planB.append({'year':2019, 'month':9, 'income':100000, 'item':'personal'})
planB.append({'year':2019, 'month':9, 'income':200000, 'item':'publisher'})
planB.append({'year':2019, 'month':(11,12), 'income':300000, 'item':'personal'})
planB.append({'year':2019, 'month':10, 'income':150000, 'item':'personal'})
planB.append({'year':2019, 'month':(11,12), 'income':80000, 'item':'dojin'})
planB.append({'year':2019, 'month':10, 'expence':60000, 'item':'print'})
planB.append({'year':2019, 'month':(11,12), 'expence':160000, 'item':'cost'})
planB.append({'year':2019, 'month':(11,12), 'expence':77600*4, 'item':'land'})
planB.append({'year':2019, 'month':(11,12), 'expence':70000*4, 'item':'life'})

print(r"result B: ", result_balance(current_balance, planB))
