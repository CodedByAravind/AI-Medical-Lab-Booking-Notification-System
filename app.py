from flask import Flask, request, jsonify, send_file
import threading
import time
import csv

app = Flask(__name__)

def send_reminder(name, test, date):
    time.sleep(5)  # simulate delay (5 sec instead of 1 day)
    print(f"Reminder: {name}, your {test} is scheduled on {date}")
# Save booking data
def save_booking(name, test, date):
    with open("leads.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, test, date])
    threading.Thread(target=send_reminder, args=(name, test, date)).start()   
    threading.Thread(target=send_report_update, args=(name,)).start() 
    
@app.route("/")
def home():
    return send_file("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    text = user_input.lower()

    if "book" in text:
        return jsonify({"reply": "Sure! Please provide your name, test type, and date."})

    elif "," in user_input:
        try:
            parts = [x.strip() for x in user_input.split(",")]

            name = None
            test = None
            date = None

            for p in parts:
                p_lower = p.lower()

                if "/" in p or "-" in p or "today" in p_lower or "tomorrow" in p_lower:
                    date = p

                elif "test" in p_lower or "blood" in p_lower or "sugar" in p_lower or "urin" in p_lower:
                    test = p

                else:
                    name = p

            if not name or not test or not date:
                return jsonify({
                    "reply": "Please provide details in this format:\nName, Test, Date\nExample: Aravind, Blood Test, 23-12-2026\nAvailable tests: Blood, Sugar, Urine\nDate format: DD-MM-YYYY"
                })

            save_booking(name, test, date)

            return jsonify({
                "reply": f"Booking confirmed for {name}. Reminder: Your test is on {date}."
            })

        except:
            return jsonify({
                "reply": "Please provide details in this format:\nName, Test, Date\nExample: Aravind, Blood Test, 23-12-2026\nAvailable tests: Blood, Sugar, Urine\nDate format: DD-MM-YYYY"
            })

    elif "fasting" in text:
        return jsonify({"reply": "Most blood tests require 8–12 hours fasting."})

    elif "report" in text:
        return jsonify({"reply": "Reports are usually ready within 24 hours."})

    elif "test" in text:
        return jsonify({"reply": "We offer blood tests, sugar tests, and full body checkups."})

    else:
        return jsonify({"reply": "I can help with lab bookings, tests, and reports."})

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    save_booking(data["name"], data["test"], data["date"])
    return jsonify({"status": "saved"})

def send_report_update(name):
    time.sleep(8)
    print(f"Report Update: {name}, your lab report is ready.")

if __name__ == "__main__":
    app.run(debug=True)