import math

def Glicko(obj1, obj2, sj):
    u = (obj1.ratings[-1] - 1500)/173.7178
    phi = obj1.deviations[-1]/173.7178
    gphi =  1/math.sqrt(1 + (3*phi**2)/math.pi**2)
    vol1 = obj1.volatilities[-1]

    uj = (obj2.ratings[-1] - 1500)/173.7178
    phij = obj2.deviations[-1]/173.7178
    gphij = 1/math.sqrt(1 + (3*phij**2)/math.pi**2)
    vol2 = obj2.volatilities[-1]

    E = 1/ (1 + (math.exp(-gphij*(u - uj))))
    v = ((gphij**2)*E*(1 - E))**(-1)
    delta = v*(gphij)*(sj - E)

    t = 0.6
    a = math.log(vol1 ** 2)
    def f(x):
        first_term = (math.exp(x)*(delta**2 - phi**2 - v - math.exp(x)))/(2*(phi**2 + v + math.exp(x))**2)
        second_term = (x-a)/(t**2)
        return first_term - second_term
    A = a
    if delta**2 > phi**2 + v:
        B = math.log(delta**2 - phi**2 - v)
    elif delta**2 <= phi**2 + v:
        k = 1
        while f(a - k*t) < 0:
            k = k+1
        B = a - k*t
    fa = f(A)
    fb = f(B)
    e = 0.000001
    while abs(B - A) > e:
        C = A + (A-B)*fa/(fb-fa)
        fc = f(C)
        if fc*fb <= 0:
            A = B
            fa = fb
        else:
            fa = fa/2
        B = C
        fb = fc
    new_volatility = math.exp(A/2)
    phi_star = math.sqrt(phi**2 + new_volatility**2)
    new_phi = 1/math.sqrt(1/phi_star**2 + 1/v)
    new_u = u + (new_phi**2)*(gphij)*(sj - E)

    r_ = 173.7178*new_u + 1500
    RD_ = 173.7178*new_phi

    return r_,RD_, new_volatility

