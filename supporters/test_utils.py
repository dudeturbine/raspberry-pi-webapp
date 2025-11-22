from flask import request, Blueprint

test_bp = Blueprint('test_bp', __name__)

@test_bp.route('/test', methods=['GET', 'POST'])
def test_multiply():
    result = ""
    if request.method == 'POST':
        input_x = to_float(request.form.get('x'))
        input_y = to_float(request.form.get('y'))
        result = multiply(input_x, input_y)
    return f'''
        <h2>Test multiply</h2>
        <form method="post">
            <input type="number" name="x" step="0.001" placeholder="x">
            <input type="number" name="y" step="0.001" placeholder="y">
            <input type="submit" value="Multiply">
        </form>

        <p>{result}</p>
    '''

def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def multiply(x: float, y: float) -> float: #some lovely type-hinting
    return x*y