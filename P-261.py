import requests

equation = input('Give Your Equation : ')
result = 'https://newton.now.sh/api/v2//simplify/' + equation
data = requests.get(result).json()
print('Operation For The Given Equation : ', data['operation'])
print('Expression Of The Given Equation : ', data['expression'])
print('Result Of The Given Equation : ', data['result'])