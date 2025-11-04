from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ allow requests from localhost


@app.route('/')
def home():
    return jsonify({"status": "Cost Estimator API is running!"})

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.get_json()
    area = float(data.get('area', 0))
    building_type = data.get('type', 'basic')

    rate = 1500 if building_type == "basic" else 2000 if building_type == "standard" else 2500
    estimated_cost = area * rate

    # Add chart data
    chart_data = {
        "labels": ["Material", "Labor", "Finishing", "Misc"],
        "values": [
            estimated_cost * 0.5,
            estimated_cost * 0.3,
            estimated_cost * 0.15,
            estimated_cost * 0.05
        ]
    }

    return jsonify({
        "estimated_cost": estimated_cost,
        "currency": "INR",
        "chart_data": chart_data   # ✅ Added this line
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
