from __future__ import annotations

import argparse

def matmul(a, b, mod):
    return (
        (a[0]*b[0] + a[1]*b[2]) % mod,
        (a[0]*b[1] + a[1]*b[3]) % mod,
        (a[2]*b[0] + a[3]*b[2]) % mod,
        (a[2]*b[1] + a[3]*b[3]) % mod,
    )

def pell_mod(n: int, mod: int) -> int:
    result = (1, 0, 0, 1)
    base = (2 % mod, 1 % mod, 1 % mod, 0)
    e = n
    while e:
        if e & 1:
            result = matmul(result, base, mod)
        base = matmul(base, base, mod)
        e >>= 1
    return result[1] % mod

def prime_divisors(n: int) -> list[int]:
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out

def verify_rank(modulus: int, predicted_rank: int) -> bool:
    if pell_mod(predicted_rank, modulus) != 0:
        return False
    for q in prime_divisors(predicted_rank):
        if pell_mod(predicted_rank // q, modulus) == 0:
            return False
    return True

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-k', type=int, default=8)
    args = parser.parse_args()

    assert verify_rank(3, 4)
    assert verify_rank(7, 6)
    print('boundary k=1:', verify_rank(21, 12), 'z_P(21)=12')

    for k in range(2, args.max_k + 1):
        modulus = 21 ** k
        predicted = 4 * 21 ** (k - 1)
        ok = verify_rank(modulus, predicted)
        square = None
        if k % 2 == 1:
            r = (k - 1) // 2
            square = (2 * 21 ** r) ** 2
            assert square == predicted
        print({
            'k': k,
            'modulus': modulus,
            'predicted_rank': predicted,
            'square_rank': square,
            'verified': ok,
        })
        if not ok:
            raise SystemExit(2)

if __name__ == '__main__':
    main()
