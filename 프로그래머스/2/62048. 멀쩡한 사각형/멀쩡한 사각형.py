def solution(w,h):
    GCD = gcd(w, h)
    ww = w // GCD
    hh = h // GCD
    cnt = (ww * hh) - ((ww - 1) * (hh - 1)) 
    cnt *= GCD
    return w * h - cnt

def gcd(a, b):
    while b != 0:
        if a > b:
            b, a = a, b
        b = b % a
    return a

print(gcd(12, 8))