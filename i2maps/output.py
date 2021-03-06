import decimal
import json
def printDecimal(d):
    n = 3 # Number of decimal places
    s = str(d)
    s = s[:s.find('.') + 1 + n]
    return '|' + s + '|'

def to_json(results, callback=''):
    s = json.dumps(results, default=printDecimal)
    s = s.replace('"|', '').replace('|"', '')
    if callback != "":
        s = callback + '(' + s + ')'
    return s
    