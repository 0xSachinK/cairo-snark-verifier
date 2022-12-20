pragma circom 2.0.0;

template Factors() {
    // I know two numbers x and y the product of which is a public value z.
    // In other words, I know factors of z.
    signal input x;
    signal input y;

    signal output z;

    z <== x * y;
}

component main = Factors();