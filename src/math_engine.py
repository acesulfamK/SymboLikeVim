import sympy as sp


class MathEngine:
    def __init__(self):
        # sympyに関連する初期設定
        pass

    @classmethod
    def diff(cls, formula_str, val):
        expr = sp.simplify(formula_str)
        diff_expr = sp.diff(expr, sp.symbols(val))
        return str(diff_expr)

    @classmethod
    def integrate(cls, formula_str, val):
        expr = sp.simplify(formula_str)
        diff_expr = sp.integrate(expr, sp.symbols(val))
        return str(diff_expr)

    def process_expression(self, expression):
        # 数式の処理ロジック
        pass
