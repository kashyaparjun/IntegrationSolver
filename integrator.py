from sympy import (Symbol, sympify, denom, cos, sin, tan, sec,
                   cot, csc, log, trigsimp, diff, numer, ln)


def go_through_knowledge_base(g):
    y = str(g)
    print(g)
    gc = g
    p = 0
    for i in range(len(y)):
        if y[i] == "-":
            p = 1
    if p == 1:
        g = -g
    t = 0
    if denom(gc).find(cos(x)) != set([]):
        gc = gc * cos(x) * sec(x)
        g = gc
    if denom(gc).find(sin(x)) != set([]):
        gc = gc * sin(x) * csc(x)
        g = gc
    if denom(gc).find(tan(x)) != set([]):
        gc = gc * tan(x) * cot(x)
        g = gc
    if gc.find(sin(x)) != set([]) and (gc / sin(x)).find(x) == set([]):
        g = g.replace(sin(x), -cos(x))
        t = g
    elif gc.find(cos(x)) != set([]) and (gc / cos(x)).find(x) == set([]):
        g = g.replace(cos(x), sin(x))
        t = g
    elif gc.find(sec(x) ** 2) != set([]) and (gc / sec(x) ** 2).find(x) == set([]):
        g = g.replace(sec(x) ** 2, tan(x))
        t = g
    elif gc.find(csc(x) ** 2) != set([]) and (gc / csc(x) ** 2).find(x) == set([]):
        g = g.replace(csc(x) ** 2, -cot(x))
        t = g
    elif gc.find(sec(x)) != set([]) and gc.find(tan(x)) != set([]) and (gc / (sec(x) * tan(x))).find(x) == set([]):
        g = g.replace(sec(x), 1)
        g = g.replace(tan(x), sec(x))
        t = g
    elif gc.find(csc(x)) != set([]) and gc.find(cot(x)) != set([]) and (gc / (csc(x) * cot(x))).find(x) == set([]):
        g = g.replace(csc(x), 1)
        g = g.replace(cot(x), -csc(x))
        t = g
    elif gc.find(sec(x)) != set([]) and (gc / sec(x)).find(x) == set([]):
        g = g.replace(sec(x), ln(sec(x) + tan(x)))
        t = g
    elif gc.find(sec(x) ** 3) != set([]) and (gc / sec(x) ** 3).find(x) == set([]):
        g = g.replace(sec(x) ** 3, (sec(x) * tan(x) / 2) + (ln(sec(x) + tan(x)) / 2))
        t = g
    elif gc.find(tan(x)) != set([]) and (gc / tan(x)).find(x) == set([]):
        g = g.replace(tan(x), log(sec(x)))
        t = g
    elif gc.find(cot(x)) != set([]) and (gc / cot(x)).find(x) == set([]):
        g = g.replace(cot(x), log(sin(x)))
        t = g
    elif gc.find(csc(x)) != set([]) and (gc / csc(x)).find(x) == set([]):
        g = g.replace(csc(x), log(csc(x) - cot(x)))
        t = g
    elif gc.find(tan(x) ** 2) != set([]) and (gc / tan(x) ** 2).find(x) == set([]):
        g = g.replace(tan(x) ** 2, tan(x) - x)
        t = g
    elif gc.find(cot(x) ** 2) != set([]) and (gc / cot(x) ** 2).find(x) == set([]):
        g = g.replace(cot(x) ** 2, -x - cot(x))
        t = g
    elif gc.find(sin(x) ** 2) != set([]) and (gc / sin(x) ** 2).find(x) == set([]):
        g = g.replace(sin(x), (x - sin(x) * cos(x)) / 2)
        t = g
    elif gc.find(cos(x) ** 2) != set([]) and (gc / cos(x) ** 2).find(x) == set([]):
        g = g.replace(cos(x) ** 2, (x + sin(x) * cos(x)) / 2)
        t = g
    elif gc.find(cos(x) ** 3) != set([]) and (gc / cos(x) ** 3).find(x) == set([]):
        g = g.replace(cos(x) ** 3, (9 * sin(x) + sin(3 * x)) / 12)
        t = g
    elif gc.find(sin(x) ** 3) != set([]) and (gc / sin(x) ** 3).find(x) == set([]):
        g = g.replace(sin(x) ** 3, (cos(3 * x) - 9 * cos(x)) / 12)
        t = g
    elif gc.find(tan(x) ** 3) != set([]) and (gc / tan(x) ** 3).find(x) == set([]):
        g = g.replace(tan(x), (sec(x) ** 2) / 2 + log(cos(x)))
        t = g
    elif gc.find(cot(x) ** 3) != set([]) and (gc / cot(x) ** 3).find(x) == set([]):
        g = g.replace(cot(x), (-csc(x) ** 2) / 2 - log(sin(x)))
        t = g
    elif gc.find(sec(x) ** 3) != set([]) and (gc / sec(x) ** 3).find(x) == set([]):
        g = g.replace(sec(x) ** 3, (tan(x) * sec(x) - log(cos(x / 2) - sin(x / 2)) + log(sin(x / 2) + cos(x / 2))) / 2)
        t = g
    elif gc.find(tan(x) ** 4) != set([]) and (gc / tan(x) ** 4).find(x) == set([]):
        g = g.replace(tan(x) ** 4, (x - (4 * tan(x) / 3) + ((tan(x) * sec(x) ** 2) / 3)))
        t = g
    else:
        t = 0
    if p == 1:
        t = -t
    return t


def simplifier(qr):
    qr = trigsimp(qr)
    print(qr)
    ty = str(qr)
    q = 0
    er = 0
    we = 0
    p = ""
    for i in range(0, len(ty)):
        if ty[i] == "(":
            q = 1
            er += 1
        elif ty[i] == ")":
            q = 0
            we = 1
        if ty[i] == "(":
            p += ""
        elif q == 1 and we != 1:
            p += ty[i]
    for i in range(er):
        ty = ty.replace(p, "x")
    we = sympify(ty)
    wq = go_through_knowledge_base(we)
    wqw = str(wq)
    pq = "(" + p + ")"
    wqw = wqw.replace("x", pq)
    wq = sympify(wqw)
    p = sympify(p)
    p = diff(p)
    wq = wq / p
    return wq


def power_calc(g):
    g = sympify(g)
    h = str(g)
    r = -1
    yr = ""
    yu = h.find("x**") + 3
    ty = h.find("x**")
    if ty != -1:
        for i in range(yu, len(h)):
            bg = h[i]
            if bg.isdigit() or bg == "/" or bg == "-":
                yr += h[i]
                r = 1
            elif bg == "(":
                r = 1
            else:
                r = 0
            if r == 0:
                break
    if yr != "":
        p = sympify(yr) + 1
        g = g * x
        g = g / p
    elif denom(g).find(x) != set([]) or (numer(g).find(x) == set([]) and denom(g).find(x) == set([])):
        if str(denom(g)).find("+") != -1:
            g = g * denom(g) * log(denom(g)) / diff(denom(g))
        else:
            g = g * x * log(x)
    elif g.find(x) != set([]):
        g = g * x / 2
    return g


def decision_maker(t):
    py = 0
    ty = 0
    t = sympify(t)
    if str(t).find("x") == -1:
        return t * x
    if str(denom(t)).find("x**") == -1 or (str(denom(t)).find("x**") != -1 and str(numer(t)).find("x") == -1):
        py = 1
    if py == 1:
        if (str(t).find("sin")) != -1 or (str(t).find("cos")) != -1 or (str(t).find("tan")) != -1 or (
                str(t).find("cot")) != -1 or (str(t).find("sec")) != -1 or (str(t).find("csc") != -1):
            ty = simplifier(t)
        else:
            ty = power_calc(t)
    if denom(t).find((1 - x ** 2) ** (1 / 2)) != set([]) and numer(t).find(x) == set([0]):
        ty = t * ((1 - x ** 2) ** (1 / 2)) * sin(x) ** (-1)
    return ty


x = Symbol('x')
y = Symbol('y')


def get_integral(expression):
    print(expression)
    n = expression
    a = sympify(n)
    den = denom(a)
    num = numer(a)
    hr = 0
    pwn = str(num)
    for i in range(len(pwn)):
        if pwn[i] == "+":
            hr = hr + 1
        elif pwn[i] == "-":
            hr = hr + 1
    lister = []
    a = 0
    b = 0
    t = -1
    print(pwn)
    for i in range(len(pwn)):
        if pwn[i] == "(":
            t = 0
        elif pwn[i] == ")":
            t = -1
        if pwn[i] == "+" and t != 0:
            b = i
            lister.append(pwn[a:b])
            a = b
        elif pwn[i] == "-" and i != 0 and t != 0:
            b = i
            lister.append(pwn[a:b])
            a = b
    lister.append(pwn[b:len(pwn)])
    list2 = []
    c = Symbol('c')
    finale = c
    for i in range(len(lister)):
        list2.append(str(sympify(lister[i]) / den))
    for i in range(len(list2)):
        res = list2[i]
        res = sympify(res)
        if str(denom(res)) == "(-x**2 + 1)**(5/2)":
            res = numer(res)
            res = res.replace(x, sin(x))
            res = res / cos(x) ** 4
            finale = finale + decision_maker(res)
        elif str(denom(res)) == "-x**2 + 1":
            res = numer(res).replace(x, sin(x))
            res = res / cos(x) ** 2
            res = res * cos(x)
            finale = finale + decision_maker(res)
        else:
            finale = finale + decision_maker(res)
    return finale
