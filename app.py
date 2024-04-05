from flask import Flask, request, jsonify, send_from_directory
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)

limiter = Limiter(
    app=app,
    key_func=get_remote_address,  # Use the remote address as the rate limit key
    default_limits=["200 per minute"]  # Default rate limit for all routes
)

STATIC_FOLDER = 'static'

# Mock data for demonstration purposes
pets = [
    {"id": 1, "name": "Rex", "tag": "dog"},
    {"id": 2, "name": "Mittens", "tag": "cat"},
    {"id": 3, "name": "Goldie", "tag": "fish"},
    {"id": 4, "name": "Buddy", "tag": "dog"},
    {"id": 5, "name": "Fluffy", "tag": "rabbit"},
    {"id": 6, "name": "Squawks", "tag": "parrot"},
    {"id": 7, "name": "Spike", "tag": "dog"},
    {"id": 8, "name": "Whiskers", "tag": "cat"},
    {"id": 9, "name": "Bubbles", "tag": "fish"},
    {"id": 10, "name": "Nibbles", "tag": "rabbit"},
    {"id": 11, "name": "Polly", "tag": "parrot"},
    {"id": 12, "name": "Rusty", "tag": "dog"}
]


@app.route('/pets', methods=['GET'])
def list_pets():
    limit = request.args.get('limit', default=100, type=int)
    return jsonify(pets[:limit])


@app.route('/pets/<int:petId>', methods=['GET'])
def show_pet_by_id(petId):
    pet = next((pet for pet in pets if pet['id'] == petId), None)
    if pet:
        return jsonify(pet)
    else:
        return jsonify({"code": 404, "message": "Pet not found"}), 404


@app.route('/openapi', methods=['GET'])
def openapi_spec():
    return send_from_directory(STATIC_FOLDER, 'openapi.yaml')


# Error handling for the API
@app.errorhandler(404)
def not_found(error):
    return jsonify({"code": 404, "message": "Not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"code": 500, "message": "Internal server error"}), 500


@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"code": 429, "message": "Rate limit exceeded (200 requests per minute)"}), 429


if __name__ == '__main__':
    app.run(debug=True)

