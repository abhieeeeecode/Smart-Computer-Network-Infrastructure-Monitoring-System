from flask import Flask, render_template, jsonify
import re

app = Flask(__name__)

def get_latest_data():
    try:
        with open("network_log.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                return None

            last_line = lines[-1]

            loss_match = re.search(r"Loss: (\d+)", last_line)
            latency_match = re.search(r"Latency: (-?\d+)", last_line)

            if loss_match and latency_match:
                loss = int(loss_match.group(1))
                latency = int(latency_match.group(1))

                if loss > 1 or latency > 100:
                    status = "🚨 RISK"
                    ai_msg = "Failure Likely"
                else:
                    status = "✅ STABLE"
                    ai_msg = "All Good"

                return {
                    "loss": loss,
                    "latency": latency,
                    "status": status,
                    "ai_msg": ai_msg
                }
    except:
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    data = get_latest_data()
    return jsonify(data if data else {})

if __name__ == "__main__":
    app.run(debug=True)