<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Seat Selection</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<div class="container">
    <h1>Seat Selection</h1>

    <div class="screen">SCREEN THIS WAY 🔊</div>

    <!-- Legend -->
    <div class="legend">
        <span><div class="dot available"></div>Available</span>
        <span><div class="dot selected"></div>Selected</span>
        <span><div class="dot booked"></div>Booked</span>
    </div>

    <!-- Seats -->
    <div class="seats" id="seats"></div>

    <!-- Price Summary -->
    <div class="card">
        <div class="row">
            <span>Seats Selected</span>
            <span id="count">0</span>
        </div>
        <div class="row">
            <span>Total Price</span>
            <span>Rs.<span id="price">0</span></span>
        </div>

        <button onclick="confirmBooking()">Confirm Booking</button>
    </div>

    <div class="success" id="success">
        ✔ Booking Confirmed Successfully
    </div>
</div>

<script>
const rows = ["A","B","C","D","E","F","G"];
const cols = 10;
const seatPrice = 200;
const bookedSeats = ["A3","B6","C2","D8","E5"];

let selected = [];

const seatBox = document.getElementById("seats");

rows.forEach(r => {
    for (let c = 1; c <= cols; c++) {
        const seatNo = r + c;
        const seat = document.createElement("div");
        seat.className = "seat";

        if (bookedSeats.includes(seatNo)) {
            seat.classList.add("booked");
        } else {
            seat.classList.add("available");
            seat.onclick = () => toggleSeat(seat, seatNo);
        }

        seat.innerText = seatNo;
        seatBox.appendChild(seat);
    }
});

function toggleSeat(seat, no) {
    if (seat.classList.contains("selected")) {
        seat.classList.remove("selected");
        seat.classList.add("available");
        selected = selected.filter(s => s !== no);
    } else {
        seat.classList.remove("available");
        seat.classList.add("selected");
        selected.push(no);
    }
    update();
}

function update() {
    document.getElementById("count").innerText = selected.length;
    document.getElementById("price").innerText = selected.length * seatPrice;
}

function confirmBooking() {
    if (selected.length === 0) {
        alert("Please select at least one seat");
        return;
    }
    document.getElementById("success").style.display = "block";
}
</script>

</body>
</html>













/* ---------- BACKGROUND ---------- */
body {
    margin: 0;
    font-family: "Segoe UI", Arial, sans-serif;
    background: radial-gradient(circle at top, #5a0000, #000000 70%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

/* ---------- MAIN CARD ---------- */
.container {
    width: 420px;
    background: rgba(0,0,0,0.65);
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 0 40px rgba(255,0,0,0.25);
}

/* ---------- TITLE ---------- */
h1 {
    text-align: center;
    margin-bottom: 12px;
}

/* ---------- SCREEN ---------- */
.screen {
    text-align: center;
    background: linear-gradient(#333, #111);
    padding: 8px;
    border-radius: 10px;
    margin-bottom: 14px;
    font-size: 14px;
}

/* ---------- LEGEND ---------- */
.legend {
    display: flex;
    justify-content: space-around;
    font-size: 13px;
    margin-bottom: 14px;
}

.legend span {
    display: flex;
    align-items: center;
    gap: 6px;
}

.dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;   
}

/* LEGEND COLORS */
.dot.available {
    background: #43A047;
}

.dot.selected {
    background: #1E88E5;
}

.dot.booked {
    background: #E53935;
}

/* ---------- SEATS ---------- */
.seats {
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    gap: 8px;
    justify-items: center;
    margin-bottom: 18px;
}

.seat {
    width: 34px;
    height: 34px;
    border-radius: 6px;
    font-size: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

.seat.available {
    background: linear-gradient(#66bb6a, #2e7d32);
}

.seat.selected {
    background: linear-gradient(#42a5f5, #1e88e5);
    box-shadow: 0 0 10px rgba(30,136,229,0.9);
}

.seat.booked {
    background: linear-gradient(#ef5350, #c62828);
    cursor: not-allowed;
    opacity: 0.85;
}

.seat:hover:not(.booked) {
    transform: scale(1.15);
}

/* ---------- PRICE ---------- */
.card {
    background: rgba(255,255,255,0.05);
    padding: 14px;
    border-radius: 14px;
}

.row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 6px;
    font-size: 14px;
}

/* ---------- BUTTON ---------- */
button {
    width: 100%;
    height: 44px;
    background: linear-gradient(#e53935, #b71c1c);
    border: none;
    border-radius: 10px;
    color: #fff;
    font-size: 15px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    opacity: 0.9;
}

/* ---------- SUCCESS ---------- */
.success {
    display: none;
    margin-top: 14px;
    text-align: center;
    color: #66bb6a;
    font-size: 16px;
}



