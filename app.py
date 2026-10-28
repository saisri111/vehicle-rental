
from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)

VEHICLES = ["Car", "SUV", "Bike", "Van"]
bookings = []


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    error = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        vehicle = request.form.get("vehicle", "")
        pickup = request.form.get("pickup", "")
        dropoff = request.form.get("dropoff", "")

        if not all([name, email, phone, vehicle, pickup, dropoff]):
            error = "Please fill in every field."
        elif vehicle not in VEHICLES:
            error = "Please select a valid vehicle."
        else:
            try:
                start = date.fromisoformat(pickup)
                end = date.fromisoformat(dropoff)

                if start < date.today():
                    error = "Pickup date cannot be in the past."
                elif end < start:
                    error = "Return date must be on or after pickup."
                else:
                    booking = {
                        "id": len(bookings) + 1,
                        "name": name,
                        "email": email,
                        "vehicle": vehicle,
                        "pickup": pickup,
                        "dropoff": dropoff,
                    }
                    bookings.append(booking)
                    message = (
                        f"Booking confirmed! Booking ID: {booking['id']}"
                    )
            except ValueError:
                error = "Please enter valid dates."

    return render_template(
        "index.html",
        vehicles=VEHICLES,
        message=message,
        error=error,
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
