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




