
class Solution(object):
    def maxCoins(self,piles):
        piles.sort()
        x=int(len(piles)/3)
        coin=0
        for i in range(x):
            data=piles[-2:]
            data=[piles[i]]+data
            coin+=data[1]
            piles.pop()
            piles.pop()
            # print(data)
        return(coin)
