import ast
import operator

OPERATORS = {ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv}

MAX_LENGTH = 100
MAX_DEPTH = 20

def safe_eval(expression: str) -> float:
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("Invalid expression")

    if len(expression) > MAX_LENGTH:
        raise ValueError("Expression too long")

    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError:
        raise ValueError("Invalid expression")

    def calculate(node, depth=0):
        if depth > MAX_DEPTH:
            raise ValueError("Depth limit exceeded")

        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            left = calculate(node.left, depth + 1)
            right = calculate(node.right, depth + 1)

            if isinstance(node.op, ast.Div) and right == 0:
                raise ValueError("Division by zero")

            return OPERATORS[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in (ast.UAdd, ast.USub):
            value = calculate(node.operand, depth + 1)
            return value if isinstance(node.op, ast.UAdd) else -value

        raise ValueError("Unsupported expression")

    return calculate(tree.body)

if __name__ == "__main__":
    expressions = [
        "4 * 12",
        "48 + 75",
        "123 - 20",
        "__import__('os')",
        "open('x')",
        "10 / 0",
    ]

    for expression in expressions:
        try:
            print(expression, "=", safe_eval(expression))
        except ValueError as error:
            print(expression, "-> Rejected:", error)
