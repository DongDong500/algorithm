def solution(phone_book):
    answer = True

    for idx, pivot in enumerate(phone_book):
        src_len = len(pivot)
        for tidx in range(idx + 1, len(phone_book)):
            tar = phone_book[tidx]
            tar_len = len(tar)
            if src_len <= tar_len:
                substring = tar[0:src_len]
                if pivot == substring:
                    return False

    return answer


if __name__ == "__main__":

    PB = [
        ["119", "97674223", "1195524421"],
        ["123","456","789"],
        ["12","123","1235","567","88"]
    ]
    for i, pb in enumerate(PB):
        print(solution(pb))