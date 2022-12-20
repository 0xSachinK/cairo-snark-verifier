def split_to_array(_in, n, k):
    _in = int(_in)
    _in_copy = _in
    words = [0 for _ in range(k)]
    for i in range(k):
        words[i] = _in % 2 ** n
        _in = _in // 2 ** n     # // is used to get an integer back from division of two ints
    if _in != 0:
        raise Exception(f'Number {_in_copy} does not fit in {k * n} bits')
    return words        # 0th term is lowest significant bit

def split_to_uint256(num):
    words = split_to_array(num, n=128, k=2)
    low = words[0]
    high = words[1]
    return low, high

def split_to_bigint3(num):
    words = split_to_array(num, n=86, k=3)
    return words[0], words[1], words[2]

def split_nums_to_bigint3(nums):
    out = []
    for num in nums:    
        out.extend(split_to_bigint3(num))
    return tuple(out)