def solution1(coin, cards):
    answer = 0

    from collections import deque
    class State():
        def __init__(self, coin, cards, mycards, round) -> None:
            self.coin = coin
            self.cards = cards
            self.mycards = mycards
            self.round = round

        def get_round(self):
            return self.round

    def findmatch(lst, cons):
        """ Returns true if the sum of the two cards equals to N + 1 in the given card list
        and remove elements from the list
        lst (list): given list of my cards
        cons (int): matching condition, N + 1
        """
        for i in range(len(lst) - 1):
            for j in range(i + 1, len(lst)):
                if lst[i] + lst[j] == cons:
                    a, b = lst[i], lst[j]
                    lst.remove(a)
                    lst.remove(b)
                    return True
        return False

    N = len(cards)
    slot = deque(cards)
    me = []

    # initialize
    for i in range(int(N/3)):
        item = slot.popleft()
        me.append(item)

    Ans = deque([
        State(
            coin=coin,
            cards=slot.copy(),
            mycards=me.copy(),
            round=1
        )
    ])

    while Ans:
        nstate = Ans.popleft()

        if answer < nstate.get_round():
            answer = nstate.get_round()
        
        if nstate.cards:
            pop1 = nstate.cards.popleft()
            pop2 = nstate.cards.popleft()
            # case1: dump all cards
            tmp = nstate.mycards.copy()
            if findmatch(tmp, cons=N+1):
                Ans.append(
                    State(
                        coin=nstate.coin,
                        cards=nstate.cards.copy(),
                        mycards=tmp,
                        round=nstate.round + 1
                    )
                )
            if nstate.coin > 0:
                # case2-1: pick one card
                tmp = nstate.mycards.copy()
                tmp.append(pop1)
                if findmatch(tmp, cons=N+1):
                    Ans.append(
                        State(
                            coin=nstate.coin - 1,
                            cards=nstate.cards.copy(),
                            mycards=tmp,
                            round=nstate.round + 1
                        )
                    )        
                # case2-2: pick one card
                tmp = nstate.mycards.copy()
                tmp.append(pop2)
                if findmatch(tmp, cons=N+1):
                    Ans.append(
                        State(
                            coin=nstate.coin - 1,
                            cards=nstate.cards.copy(),
                            mycards=tmp,
                            round=nstate.round + 1
                        )
                    ) 
            if nstate.coin > 1:
                # case3: pick two cards
                tmp = nstate.mycards.copy()
                tmp.extend([pop1, pop2])
                if findmatch(tmp, cons=N+1):
                    Ans.append(
                        State(
                            coin=nstate.coin - 2,
                            cards=nstate.cards.copy(),
                            mycards=tmp,
                            round=nstate.round + 1
                        )
                    ) 

    return answer

def solution2(coin, cards):
    answer = 0

    # initialize
    from collections import deque
    N = len(cards)
    Q = deque(cards)
    my = []
    for i in range(int(N/3)):
        my.append(Q.popleft())

    def nextRound(myCards):
        """ Return elements if sum of any given two cards equal to N+1
        """
        for i in range(len(myCards) - 1):
            for j in range(i + 1, len(myCards)):
                if myCards[i] + myCards[j] == N + 1:
                    return [myCards[i], myCards[j]]
        return 0
    
    def removeElement(myCards, elements):
        """ Remove given elements from myCards
        """
        for item in elements:
            myCards.remove(item)
    
    def countPair(myCards):
        """ Return pairs where sum is equal to N + 1 in the given list 
        """
        cnt = 0
        for i in range(len(myCards) - 1):
            for j in range(i + 1, len(myCards)):
                if myCards[i] + myCards[j] == N + 1:
                    cnt += 1
        return cnt
    
    def keepCard(q, myCards, coin, items):
        """ Return ... if given item will be used in upcoming round
        """
        jumpRound = countPair(myCards)
        tq = q.copy()
        for i in range(jumpRound):
            if tq:
                pop = [tq.popleft(), tq.popleft()]
                for p in items:
                    for fp in pop:
                        if p + fp == N + 1 and coin > 0:
                            myCards.append(p)
                            coin -= 1
                            items.remove(p)
        return coin
    
    answer += 1
    while Q: # 카드 뭉치에 남은 카드가 없다면 게임을 종료합니다
        pop = [Q.popleft(), Q.popleft()]
        for item in my:
            for p in pop:
                if item + p == N + 1 and coin > 0:
                    my.append(p)
                    coin -= 1
                    pop.remove(p)
        if pop:
            coin = keepCard(Q, my, coin, pop)

        nr = nextRound(my)
        if nr != 0:
            removeElement(my, nr)
            answer += 1
        else:
            break
    
    return answer

def solution(coin, cards):
    answer = 0

    # initialize
    from collections import deque
    N = len(cards)
    Q = deque(cards)
    my = []
    for i in range(int(N/3)):
        my.append(Q.popleft())

    class State:
        def __init__(self, cards, my, coin, round) -> None:
            self.cards = cards
            self.my = my
            self.coin = coin
            self.round = round
    T = deque(
        [
            State(
                cards=Q.copy(),
                my=my.copy(),
                coin=coin,
                round=1
            )
        ]
    )   

    while T:
        cstate = T.popleft()
        if answer < cstate.round:
            answer = cstate.round
        
        a, b = cstate.cards.popleft(), cstate.cards.popleft()
        # case 1
        
        # case 2

        # case 3

        # case 4


    return answer

if __name__ == "__main__":

    coins = [
        4, 3, 2, 10
    ]
    cards = [
        [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4],
        [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12],
        [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    ]
    results = [
        5, 2, 4, 1
    ]

    for coin, card, rst in zip(coins, cards, results):
        print(solution(coin, card))