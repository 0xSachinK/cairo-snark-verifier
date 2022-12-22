import json
from word_utils import split_nums_to_bigint3, split_to_bigint3

with open("../circuit/verification_key.json", "r") as f:
    data = json.loads(f.read())


alpha1 = data['vk_alpha_1']
beta2 = data['vk_beta_2']
gamma2 = data['vk_gamma_2']
delta2 = data['vk_delta_2']
IC = data['IC']

# out_string = f"""
# let alfa1 = G1Point(Uint256{split_to_uint256(alpha1[0])}, Uint256{split_to_uint256(alpha1[1])});
# let beta2 = G2Point(Uint256{split_to_uint256(beta2[0][0])}, Uint256{split_to_uint256(beta2[0][1])}, Uint256{split_to_uint256(beta2[1][1])}, Uint256{split_to_uint256(beta2[1][0])});
# let gamma2 = G2Point(Uint256{split_to_uint256(gamma2[0][0])}, Uint256{split_to_uint256(gamma2[0][1])}, Uint256{split_to_uint256(gamma2[1][1])}, Uint256{split_to_uint256(gamma2[1][0])});
# let delta2 = G2Point(Uint256{split_to_uint256(delta2[0][0])}, Uint256{split_to_uint256(delta2[0][1])}, Uint256{split_to_uint256(delta2[1][1])}, Uint256{split_to_uint256(delta2[1][0])});

# let IC_len = {len(IC)};
# let IC: G1Point* = alloc();
# """

# for i, ic in enumerate(IC):
#     out_string += f"\nassert IC[{i}] = G1Point(Uint256{split_to_uint256(ic[0])}, Uint256{split_to_uint256(ic[1])});"

# print(out_string)

# Check negate prime
negate_prime = "21888242871839275222246405745257275088696311157297823662689037894645226208583"
print(split_to_bigint3(negate_prime))


g2_points = [
    11559732032986387107991004021392285783925812861821192530917403151452391805634,
    10857046999023057135944570762232829481370756359578518086990519993285655852781,
    4082367875863433681332203403145435568316851327593401208105741076214120093531,
    8495653923123431417604973247489272438418190587263600148770280649306958101930
]
ns = split_nums_to_bigint3(g2_points)
hs = [hex(n) for n in ns]
print(hs)

        

out_string = f"""
let (alfa1) = BuildG1Point{split_nums_to_bigint3(alpha1[:-1])};
let (beta2) = BuildG2Point{split_nums_to_bigint3([*beta2[0], *beta2[1]])};
let (gamma2) = BuildG2Point{split_nums_to_bigint3([*gamma2[0], *gamma2[1]])};
let (delta2) = BuildG2Point{split_nums_to_bigint3([*delta2[0], *delta2[1]])};

let IC_length = {len(IC)};
let IC: G1Point* = alloc();
"""

for i, ic in enumerate(IC):
    out_string += f"""
    \nlet (ic{i}) = BuildG1Point{split_nums_to_bigint3(ic[:-1])};
assert IC[{i}] = ic{i};
    """

print('\n'*3)
print(out_string)