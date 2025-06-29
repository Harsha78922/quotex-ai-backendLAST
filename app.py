from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("quotex_signal_model.h5")

app = Flask(__name__)

@app.route("/")
def home():
    return "Quotex AI Backend is running."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json.get("ohlcv")
        if not data or len(data) < 50:
            return jsonify({"error": "Invalid input. Send 50 rows of OHLCV data."}), 400

        X = np.array(data).reshape(1, 50, 5)
        prediction = model.predict(X)[0]
        signal = "buy" if prediction[0] > prediction[1] else "sell"
        confidence = float(max(prediction))
        return jsonify({"signal": signal, "confidence": confidence})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)