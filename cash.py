# -*- coding: utf-8 -*-
from pprint import pprint as pp
import yaml

level = 2
input_file = 'test.yaml'

with open(input_file) as f: obj = yaml.load(f, Loader=yaml.SafeLoader)

div = obj['div']
start = obj['start']
current = obj['current']
planA = obj['planA']
planB = obj['planB']
group = obj['group']

''''数値の文字列表現を演算・タプルの文字列表現をタプルに変換'''
for a in current: a['amount'] = eval(a['amount']) if isinstance(a['amount'], str) else a['amount']
for a in planA: a['amount'] = eval(a['amount']) if isinstance(a['amount'], str) else a['amount']
for a in planB: a['amount'] = eval(a['amount']) if isinstance(a['amount'], str) else a['amount']

for a in current: a['month'] = eval(a['month']) if isinstance(a['month'], str) else a['month']
for a in planA: a['month'] = eval(a['month']) if isinstance(a['month'], str) else a['month']
for a in planB: a['month'] = eval(a['month']) if isinstance(a['month'], str) else a['month']


def result_balance(balance, plan):
    '''planを適用し、将来の結果を取得'''
    result = balance - sum([i['amount'] for i in plan if i['class'] == 'expence'])+ sum([i['amount'] for i in plan if i['class'] == 'income'])
    return result 

def output_result(plan, level=1):
    '''CSV形式でプランを出力'''
    def get_culumn_names(plan):
        ''''ヘッダ・項目名の作成'''
        date_keys = list(set([i['month'] for i in plan]))
        date_keys.sort()
        item_keys = list(set([ i['item'] for i in plan]))
        return (date_keys, item_keys)

    def val(plan, item, month):
        '''同年同月同項目の額をまとめる'''
        matched_plan = [ p for p in plan if p['item'] == item and p['month'] == month]
        value = sum([ p['amount'] if p['class'] == 'income' else p['amount'] * (-1) if p['class'] == 'expence' else 0  in p for p in matched_plan])
        return value
    
    # 月の表現を tuple で統一化
    for p in plan: p["month"] = (p["month"],) if isinstance(p["month"], int) else p["month"] 

    mlist = list(set([(p['year'],  p['month']) for p in plan]))
    mlist.sort()
    dic = {}
    newplan = []
    for m in mlist:
        dic[m] = [p for p in plan if m[0] == p['year'] and m[1] == p['month']]

    if level==1:
        for m in mlist:
            p_cost = [p['amount'] for p in dic[m] if div[p['item']]['parent'] == 'cost']
            newplan.append({'year':m[0], 'month':m[1], 'item':'cost', 'class': 'expence', 'amount':sum(p_cost)})
            p_sales = [p['amount'] for p in dic[m] if div[p['item']]['parent'] == 'sales']
            newplan.append({'year':m[0],'month':m[1], 'item':'sales', 'class':'income','amount':sum(p_sales)})
        plan = newplan

    header, row = get_culumn_names(plan) 
    result = [['row'] + header] + [[r] + [val(plan, r, m)  for m in header] for r in row]
    return result

current_balance = result_balance(start['balance'], current)
print(r"result current: ", current_balance)
print(r"result A: ", result_balance(current_balance, planA))
print(r"result B: ", result_balance(current_balance, planB))

pp(output_result(planA,level))
pp(output_result(planB,level))