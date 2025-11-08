from flask import Blueprint, jsonify, request
from models.test import Test

t = Test()
test_bp = Blueprint("test", __name__)

@test_bp.route("/", methods=["GET"])
def test():
    return jsonify({"message": t.id})