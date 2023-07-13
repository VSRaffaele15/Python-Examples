def CountNumbers(start, end, pow, digits):
    num = start
    results = []
    while True:
        num += 1
        lengthset = set(str(num**pow))
        if len(lengthset) == digits:
            results.append(num)
        if num == end:
            if len(lengthset) == digits:
                results.append(num)
            break
    return results

Counted = CountNumbers(2, 50, 2, 10)