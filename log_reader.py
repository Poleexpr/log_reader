import json

result_dict = {}

with open('visit_log.csv') as visit_log:
    with open('funnel.csv', 'w', encoding='utf-8') as funnel:
        purchase = open('purchase_log.txt', encoding='utf-8').readlines()
        for element in purchase:
            json_dict = json.loads(element)
            result_dict.update({json_dict.values()})
        for line in visit_log:
            line = line.strip().split(',')
            if line[0] in result_dict.keys():
                funnel.write(line[0] + ',' + line[1] + ',' + str(result_dict.get(line[0])) + '\n')


