name = 'Maria'
print(name)

#리스트
lottery = [3, 42, 12, 19, 30, 59]
len(lottery)

lottery.sort()
print(lottery)


lottery.reverse()
print(lottery)

lottery.append(199)
print(lottery)

print(lottery[0])
print(lottery[1])

print(lottery)
print(lottery[0])
lottery.pop(0)

print(lottery)

#딕셔너리
participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
print(participant['name'])

participant['favorite_language'] = 'Python'
len(participant)

participant.pop('favorite_numbers')
participant

participant['country'] = 'Germany'
participant

print(6 > 2 and 2 < 3)
print(3 > 2 and 2 < 1)