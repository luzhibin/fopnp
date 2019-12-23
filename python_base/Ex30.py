import random
import operator


def getPokers():
    pokers = []
    poker = []
    for i in ['♥', '♠', '♦', '♣']:
        for j in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            poker.append(i)
            poker.append(j)
            pokers.append(poker)
            poker = []
    return pokers


pokers = getPokers()
random.shuffle(pokers)  # 将序列的所有元素随机排序
li = {}
for player in ['player1', 'player2', 'player3', 'player4']:
    b = random.sample(pokers, 13)
    for s in b:
        pokers.remove(s)
    li.setdefault(player, b)

print('player1：', sorted(li['player1'], key=operator.itemgetter(0, 1)))  # operator.itemgetter(0, 1)根据花色和数字来排序
print('player2：', sorted(li['player2'], key=operator.itemgetter(0, 1)))
print('player3：', sorted(li['player3'], key=operator.itemgetter(0, 1)))
print('player4：', sorted(li['player4'], key=operator.itemgetter(0, 1)))
