import subprocess
import re
import time
from datetime import datetime
from sklearn.linear_model import LogisticRegression

target_ip = "8.8.8.8"

print("🚀 Starting Self-Healing Intelligent Network...\n")

data = []
labels = []

# Load previous logs for training
def load_data():
    try:
        with open("network_log.txt", "r") as f:
            for line in f:
                loss_match = re.search(r"Loss: (\d+)", line)
                latency_match = re.search(r"Latency: (-?\d+)", line)

                if loss_match and latency_match:
                    loss = int(loss_match.group(1))
                    latency = int(latency_match.group(1))

                    data.append([loss, latency])

                    if loss > 1 or latency > 100:
                        labels.append(1)
                    else:
                        labels.append(0)
    except:
        print("No previous log file found. Starting fresh.")

# Train AI model
def train_model():
    if len(set(labels)) < 2:
        print("⚠️ Not enough data for AI training. Add more logs.")
        return None

    model = LogisticRegression()
    model.fit(data, labels)
    print("✅ AI Model Trained!\n")
    return model

# Monitor network
def check_network(model):
    result = subprocess.run(
        ["ping", target_ip, "-n", "4"],
        capture_output=True,
        text=True
    )

    output = result.stdout
    print(output)

    loss_match = re.search(r"Lost = (\d+)", output)
    latency_match = re.search(r"Average = (\d+)", output)

    if loss_match:
        loss = int(loss_match.group(1))

        if latency_match:
            latency = int(latency_match.group(1))
        else:
            latency = -1

        print(f"\n📊 Loss: {loss}, Latency: {latency} ms")

        # Log data
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("network_log.txt", "a") as f:
            f.write(f"{current_time} | Loss: {loss}, Latency: {latency}\n")

        # AI Prediction
        if model:
            prediction = model.predict([[loss, latency]])[0]

            if prediction == 1:
                print("\n🤖 AI ALERT: Failure Likely!")
                print("🔄 Initiating Self-Healing...\n")

                time.sleep(2)
                print("Restarting network interface...")
                time.sleep(2)
                print("✅ Issue Resolved (Simulated)\n")

            else:
                print("\n🤖 AI: Network Stable\n")

        else:
            print("\n⚠️ AI not active yet\n")

# MAIN FLOW
load_data()
model = train_model()

while True:
    check_network(model)
    print("⏳ Next check in 10 seconds...\n")
    time.sleep(10)