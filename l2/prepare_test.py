import json
from word_utils import split_to_bigint3

with open("../circuit/proof.json", "r") as f:
    data = json.loads(f.read())


pi_a = data['pi_a']
pi_b = data['pi_b']
pi_c = data['pi_c']

a0_words = split_to_bigint3(pi_a[0])
a1_words = split_to_bigint3(pi_a[1])

b10_words = split_to_bigint3(pi_b[0][0])
b11_words = split_to_bigint3(pi_b[0][1])

b20_words = split_to_bigint3(pi_b[1][0])
b21_words = split_to_bigint3(pi_b[1][1])

c0_words = split_to_bigint3(pi_c[0])
c1_words = split_to_bigint3(pi_c[1])

out = f"""

    let a_len = 6;
    let a: felt* = alloc();
    assert a[0] = {a0_words[0]};
    assert a[1] = {a0_words[1]};
    assert a[2] = {a0_words[2]};
    assert a[3] = {a1_words[0]};
    assert a[4] = {a1_words[1]};
    assert a[5] = {a1_words[2]};

    let b1_len = 6;
    let b1: felt* = alloc();
    assert b1[0] = {b10_words[0]};
    assert b1[1] = {b10_words[1]};
    assert b1[2] = {b10_words[2]};
    assert b1[3] = {b11_words[0]};
    assert b1[4] = {b11_words[1]};
    assert b1[5] = {b11_words[2]};

    let b2_len = 6;
    let b2: felt* = alloc();
    assert b2[0] = {b20_words[0]};
    assert b2[1] = {b20_words[1]};
    assert b2[2] = {b20_words[2]};
    assert b2[3] = {b21_words[0]};
    assert b2[4] = {b21_words[1]};
    assert b2[5] = {b21_words[2]};

    let c_len = 6;
    let c: felt* = alloc();
    assert c[0] = {c0_words[0]};
    assert c[1] = {c0_words[1]};
    assert c[2] = {c0_words[2]};
    assert c[3] = {c1_words[0]};
    assert c[4] = {c1_words[1]};
    assert c[5] = {c1_words[2]};

"""

input_words = split_to_bigint3("6")     # needs to be changed as circuit updates

out += f"""

    let input_len = 3;
    let input: felt* = alloc();
    assert input[0] = {input_words[0]};
    assert input[1] = {input_words[1]};
    assert input[2] = {input_words[2]};
"""

print(out)