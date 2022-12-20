%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin, BitwiseBuiltin
from starkware.cairo.common.alloc import alloc


@contract_interface
namespace IVerifer {
    
    func verifyProof(
        a_len: felt,
        a: felt*,
        b1_len: felt,
        b1: felt*,
        b2_len: felt,
        b2: felt*,
        c_len: felt,
        c: felt*,
        input_len: felt,
        input: felt*,
    ) -> (r: felt) {
    }
}

@external
func __setup__{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
) {
    alloc_locals;

    local verifier_address;

    %{
        context.verifier_address = deploy_contract("./contracts/lambda_verifier_groth16.cairo", []).contract_address
        ids.verifier_address = context.verifier_address
    %}

    return ();
}

@external
func test_verify{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
) {
    alloc_locals;

    local verifier_address;

    %{
        ids.verifier_address = context.verifier_address
    %}

  
    let a_len = 6;
    let a: felt* = alloc();
    assert a[0] = 689293671112655705472757;
    assert a[1] = 65623032915505738926605751;
    assert a[2] = 836523791865493859676436;
    assert a[3] = 38208473162921824911272323;
    assert a[4] = 5827801934574708084984624;
    assert a[5] = 670803203718411206455647;

    let b1_len = 6;
    let b1: felt* = alloc();
    assert b1[0] = 13260860746841134783288155;
    assert b1[1] = 57836616422093088324042265;
    assert b1[2] = 1914619460080353659917058;
    assert b1[3] = 48143031306146711316906917;
    assert b1[4] = 8268433416695206128799948;
    assert b1[5] = 2536194287693909350763118;

    let b2_len = 6;
    let b2: felt* = alloc();
    assert b2[0] = 32847018497835588843928877;
    assert b2[1] = 7315599241793184252709899;
    assert b2[2] = 1301499178568839749801033;
    assert b2[3] = 42515360982858890870568931;
    assert b2[4] = 70534102323719929868880226;
    assert b2[5] = 2488729409275722737655454;

    let c_len = 6;
    let c: felt* = alloc();
    assert c[0] = 56680408251155592152844419;
    assert c[1] = 31498299884223987694110363;
    assert c[2] = 1748443217055790807391452;
    assert c[3] = 64207608929783286402506683;
    assert c[4] = 45578112301577117643490798;
    assert c[5] = 1436362865969996456101977;

    let input_len = 3;
    let input: felt* = alloc();
    assert input[0] = 6;
    assert input[1] = 0;
    assert input[2] = 0;



    let (result) = IVerifer.verifyProof(contract_address=verifier_address, a_len=a_len, a=a, b1_len=b1_len, b1=b1, b2_len=b2_len, b2=b2, c_len=c_len, c=c, input_len=input_len, input=input);

    %{
        print(ids.result)
    %}

    return ();
}