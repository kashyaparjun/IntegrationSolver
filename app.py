# Global imports
from flask import Flask, render_template, request, jsonify
from json import dumps

# Local imports
from integrator import get_integral

app = Flask("Integrator")


@app.route("/")
def integrate():
    return render_template("home.html")


@app.route("/get_integral", methods=["POST"])
def calc_value():
    try:
        expression = request.form["expression"]
        expression.replace("^", "**")
        print(expression)
        result = get_integral(expression)
        if str(result).strip() == "c":
            result = "Sorry, solving that isn't in my knowledge base yet!"
            return jsonify({"status": "error", "result": result})
        return jsonify({"status": "ok", "result": str(result).replace("**", "^")})
    except Exception as ex:
        return jsonify({"status": "error", "msg": str(ex)})


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
