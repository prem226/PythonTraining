from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

income = [
    {"Desc": "salary", "amount":5000}
]

@app.route("/incomes")
def get_incomes():
    return jsonify(income)

@app.route("/incomes",methods=['POST'])
def add_income():
    income.append(request.get_json())
    return 'Created', 201

stock = {
    "fruit":{
        "apple":100,
        "banana":45,
        "cherry":100
    },
    "veg":{
        "orange":50
    }

}

@app.route("/stock")
def get_stock():
    res=make_response(jsonify(stock),200)
    return res

@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res = make_response(jsonify(stock[collection]),200)
        return res
    res = make_response(jsonify({"error:not found"}),404)
    return res

@app.route("/stock/<collection>/<member>")
def get_member(collection, member):
    if collection in stock:
        member = stock[collection].get(member)
        if member:
            res = make_response(jsonify(member),200)
            return res
        res = make_response(jsonify({"error:not found"}),404)
        return res
    res = make_response(jsonify({"error:not found"}),404)
    return res


@app.route("/stock/<collection>", methods = ["PUT"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock :
        original = stock[collection]
        for key,value in req.items():
            if key in original:
                original[key]=value
            else:
                original[key]=value
        # stock[collection] = req
        res = make_response(jsonify({"msg":"Collection Updated.."}), 200)
        return res
    # stock[collection] = req
    # res = make_response(jsonify({"msg":"Collection created.."}),201)
    res = make_response(jsonify({"msg":"Not found"}), 404)
    return res

@app.route("/stock/<collection>", methods=["DELETE"])
def delete_collection(collection):
    if collection in stock:
        del stock[collection]
        res = make_response(jsonify({"msg": "Collection deleted"}), 204)
        return res
    else:
        res = make_response(jsonify({"msg":"Error collection not found"}), 404)
        return res

@app.route("/stock/<collection>/<member>", methods=["DELETE"])
def delete_collectionMember(collection,member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res = make_response(jsonify({"msg": "member deleted"}), 204)
            return res
        else:
            res = make_response(jsonify({"msg": "Error member not found"}), 404)
            return res
    else:
        res = make_response(jsonify({"msg":"Error collection not found"}), 404)
        return res







if __name__ == '__main__':
    app.run(debug = True, port = 5001)