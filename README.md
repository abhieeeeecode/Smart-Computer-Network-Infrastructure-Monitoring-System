Smart Computer Network Infrastructure Monitoring System.


📌 Overview :- 

This project presents a self-healing network system that can monitor, predict, and automatically resolve network issues using networking concepts, Python automation, and machine learning.
The system is designed to simulate a real-world enterprise network environment with intelligent fault detection and recovery.

 Key Features :- 

 Real-time network monitoring (latency & packet loss)
 AI-based failure prediction using machine learning
 Automated self-healing via SSH (interface restart, recovery actions)
 Live dashboard for visualization (graphs & alerts)
 Scalable network design with VLAN, routing, and wireless components


Project Architecture :-

Network (Packet Tracer)
        ↓
monitor.py → Collects data (ping, latency, packet loss)
        ↓
network_log.txt → Stores monitoring data
        ↓
ai_model.py → Predicts failures
        ↓
auto_heal.py → Fixes issues via SSH
        ↓
app.py (Flask) → Displays dashboard




🛠️Tech Stack
🔹 Networking
VLAN, Inter-VLAN Routing
OSPF (Dynamic Routing)
DHCP, DNS
Wireless (WLC, LAP)
🔹 Programming
Python




Libraries:

paramiko (SSH automation)
subprocess (network monitoring)
time (task scheduling)
🔹 AI / ML
scikit-learn
Logistic Regression
🔹 Web Dashboard
Flask
HTML, CSS, JavaScript
⚙️ Setup Instructions


1️⃣ Clone the Repository :-
git clone https://github.com/your-username/Smart-Computer-Netwrok-Infrastructure-Monitoring-System.git
cd Smart-Computer-Netwrok-Infrastructure-Monitoring-System




Install Dependencies :- 

pip install paramiko scikit-learn flask

3️⃣ Run Monitoring Script
python monitor.py

4️⃣ Train AI Model
python ai_model.py

5️⃣ Run Dashboard
python app.py


Open browser:-

http://127.0.0.1:5000/

📊 Output :-

Real-time latency & packet loss graphs
Failure prediction alerts
Automated recovery actions

🔐 Self-Healing Logic

If latency ↑ OR packet loss ↑
        ↓
AI predicts failure
        ↓
Automation triggers:
    - Interface restart
    - Network recovery

    
💡 Use Cases :-

Enterprise network monitoring
NOC (Network Operations Center) environments
AI-based observability systems
Network automation learning projects


🚧 Future Enhancements :-
Integration with real network devices (GNS3 / live routers)
Advanced ML models for prediction
Email/SMS alert system
Cloud-based deployment




Author :-
Abhishek kasture 
Aspiring  Network & Automation Engineer.


THANK YOU<img width="1850" height="915" alt="Screenshot 2026-04-13 021508" src="https://github.com/user-attachments/assets/85ce5996-7e23-460c-aef8-d4751eea9a08" />
<img width="1061" height="897" alt="Screenshot 2026-04-13 021323" src="https://github.com/user-attachments/assets/c134fa00-b0c0-4337-92c7-a0d61b270971" />
<img width="1915" height="1078" alt="Screenshot 2026-04-13 014559" src="https://github.com/user-attachments/assets/b389373d-04af-4388-96c0-1f48de8cfd32" />
<img width="1158" height="959" alt="Screenshot 2026-04-13 004335" src="https://github.com/user-attachments/assets/9038f8be-eb94-4e20-9f83-cedf9e8370e2" />


