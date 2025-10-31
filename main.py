from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Cost Estimator API is running!"})

@app.route('/estimate', methods=['POST'])
def estimate():
    try:
        data = request.get_json()
        area = float(data.get('area', 0))
        type_ = data.get('type', 'basic').lower()

        rate = 1500 if type_ == "basic" else 2000 if type_ == "standard" else 2500
        total = area * rate

        return jsonify({
            "estimated_cost": total,
            "currency": "INR",
            "breakdown": {
                "materials": total * 0.5,
                "labor": total * 0.3,
                "finishing": total * 0.15,
                "misc": total * 0.05
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
