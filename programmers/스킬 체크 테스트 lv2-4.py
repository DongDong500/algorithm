def solution(fees, records):
    answer = []

    import math
    cars = {}
    LIM_TIME = "23:59"

    for r in records:
        time, car, state = r.split(' ')
        if car not in cars.keys():
            h, m = time.split(':')
            cars[car] = [[state, int(h), int(m)]]
        else:
            h, m = time.split(':')
            cars[car].append([state, int(h), int(m)])
    cars = dict(sorted(cars.items()))
    
    for key, val in cars.items():
        if len(val) % 2 == 1:
            val.append(['OUT', 23, 59])
        accum = 0

        total = 0
        for v in val:
            state = v[0]
            if state == 'IN':
                h, m = v[1], v[2]
                total = h * 60 + m
            if state == 'OUT':
                h, m = v[1], v[2]
                total = h * 60 + m - total
                accum += total
                total = 0

        accum -= fees[0]
        pay = fees[1]
        if accum > 0:
            block = math.ceil(accum / fees[2])
            pay += fees[3] * block

        answer.append(pay)

    return answer



if __name__ == "__main__":

    # 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
    fees = [
        [180, 5000, 10, 600],
        [120, 0, 60, 591],
        [1, 461, 1, 10]
    ]
    # 시각(시:분), 차량번호, 내역
    records = [
        ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
        ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"],
        ["00:00 1234 IN"]
    ]
    result = [
        [14600, 34400, 5000],
        [0, 591],
        [14841]
    ]
    for f, r, ans in zip(fees, records, result):
        print(solution(f, r) == ans)