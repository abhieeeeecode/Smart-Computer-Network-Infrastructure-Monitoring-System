import re
from sklearn.linear_model import LogisticRegression

# Read log file
data = []
labels = []

with open("network_log.txt", "r") as f:
    for line in f:
        loss_match = re.search(r"Loss: (\d+)", line)
        latency_match = re.search(r"Latency: (-?\d+)", line)

        if loss_match and latency_match:
            loss = int(loss_match.group(1))
            latency = int(latency_match.group(1))

            # Features
            data.append([loss, latency])

            # Label logic (simple)
            if loss > 1 or latency > 100:
                labels.append(1)  # Risk
            else:
                labels.append(0)  # Normal

# Train model
model = LogisticRegression()
model.fit(data, labels)

print("✅ AI Model Trained Successfully!")

# Test prediction
test_input = [[2, 150]]  # Example (loss=2, latency=150)

prediction = model.predict(test_input)

if prediction[0] == 1:
    print("⚠️ AI Prediction: Network Failure Likely!")
else:
    print("✅ AI Prediction: Network Stable")