let clues = [];
let currentIndex = 0;

fetch("https://cryptickles-backend.onrender.com/clues")
    .then(res => res.json())
    .then(data => {
        clues = data;
        loadClue();
    })
    
function loadClue() {    
    document.getElementById("clue").textContent = clues[currentIndex].clue;
    document.getElementById("answer").value = "";
    document.getElementById("hint").textContent = "";
    document.getElementById("result").textContent = "";
}

document.getElementById("submit").addEventListener("click", function() {
    const userAnswer = document.getElementById("answer").value.trim().toLowerCase();
    const correctAnswer = clues[currentIndex].answer.toLowerCase();
    const result = document.getElementById("result");

    if (userAnswer === correctAnswer) {
        result.textContent = "Correct Answer!";
        result.style.color = "green";
    } else {
        result.textContent = "Wrong Answer. Try Again!";
        result.style.color = "red";
    }
});

// Hint button functionality
document.getElementById("hintBtn").addEventListener("click", function() {    
    const hintElement = document.getElementById("hint");
    if (clues[currentIndex].hint) {
        hintElement.textContent = "Hint: " + clues[currentIndex].hint;
        hintElement.style.color = "blue";
    } else {
        hintElement.textContent = "No hint available for this clue.";
        hintElement.style.color = "gray";
    }
});

// Allow pressing Enter to submit
document.getElementById("answer").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        document.getElementById("submit").click();
    }
});