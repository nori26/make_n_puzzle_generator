import random
import operator
from fractions import Fraction

def create_expr(args, oper_set):
    expr = []
    terms = list(args)
    opers = [random.choice(oper_set) for _ in range(1, len(args))]
    term_counter = []
    while terms:
        if len(term_counter) < 2 or random.randint(0, 1):
            expr.append(terms.pop())
            term_counter.append(None)
        else:
            expr.append(opers.pop())
            term_counter.pop()
    expr.extend(opers)
    return expr

def calc_expr(expr, oper_set):
    terms = []
    for elem in expr:
        if elem not in oper_set:
            terms.append(Fraction(int(elem), 1))
        elif elem == "/" and terms[-1] == 0:
            return None
        else:
            x, y = terms.pop(), terms.pop()
            terms.append(oper_set[elem](y, x))
    return terms.pop()

def gen(args):
    oper_set = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    while True:
        expr = create_expr(args, list(oper_set.keys()))
        ans = calc_expr(expr, oper_set)
        if ans is not None and 10 < ans < 30 and float(ans) == int(ans):
            break
    return ans, expr

def main():
    n_args = random.randint(4, 6)
    args = [str(random.randint(1, 9)) for i in range(n_args)]
    ans, expr = gen(args)
    print(*sorted(args), f"-> {ans}")
    print(*expr)

if __name__ == "__main__":
    main()
