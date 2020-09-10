from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Хранилище коэффициентов
coeffs = {}


def solver(a: int, b: int, c: int) -> int:
    # Решатель квадратного уравнения.
    #Ax^2 + Bx + C = 0
    if a == 0:
        # Решаем линейное уравнение: Bx + C = 0
        # x = -C/B
        if b == 0:
            return 0
        else:
            return 1
    else:
        d = b**2 - 4*a*c 
        if d > 0:
            return 2
        elif d == 0:
            return 1
        else:
            return 0


class GrabResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("A", type=int, required=True, help="A coeff required!")
    parser.add_argument("B", type=int, required=True, help="B coeff required!")
    parser.add_argument("C", type=int, required=True, help="C coeff required!")

    def post(self):
        req_body = GrabResource.parser.parse_args()
        global coeffs
        coeffs = dict(req_body)
        return {}, 201


class SolveResource(Resource):
    def get(self):
        return {
            "A": coeffs["A"],
            "B": coeffs["B"],
            "C": coeffs["C"],
            "Nroots": solver(coeffs["A"], coeffs["B"], coeffs["C"]),
        }, 200


api.add_resource(GrabResource, '/grab')
api.add_resource(SolveResource, '/solve')

if __name__ == "__main__":
    app.run(port=8080, debug=True)
