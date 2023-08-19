import re


def parse_equation(input_string):
    input_string = input_string.replace('^', '**')

    # add '*' between coefficient and variable (ex// 3x -> 3*x)
    input_string = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', input_string)

    # Split the input at the '=' sign
    left, right = input_string.split('=')
    left = left.strip()
    right = right.strip()
    return left, right


def eval_expression(expression, x):
    try:
        y = eval(expression, {'x': x})
        return y
    except Exception as e:
        print(f'Error: {e}')


def generate_graph(expression, x_range=(-10, 10), width=40, height=20):
    graph = ''
    x_min, x_max = x_range
    x_step = (x_max - x_min) / width

    for y in range(height, -1, -1):
        row = ''
        for x in range(width):
            x_val = x_min + x * x_step
            y_val = eval_expression(expression, x_val)
            if y_val is not None and abs(y_val - y) <= 0.75:  # higher means more points
                row += '*'
            else:
                row += ' '
        graph += row + '\n'

    return graph
