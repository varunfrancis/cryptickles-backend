let clues = [];
let currentIndex = 0;

fetch("http://127.0.0.1:5000/clues")
    .then(res => res.json())
    .then(data => {
        clues = data;
        if (clues.length > 0) {
            loadClue();
        } else {
            document.getElementById("clue").textContent = "No clues available";
        }
    })
    .catch(error => {
        console.error("Error loading clues:", error);
        document.getElementById("clue").textContent = "Error loading clues. Make sure the server is running.";
    });

function loadClue() {
    if (clues.length === 0) return;
    
    document.getElementById("clue").textContent = clues[currentIndex].clue;
    document.getElementById("answer").value = "";
    document.getElementById("hint").textContent = "";
    document.getElementById("result").textContent = "";
}

document.getElementById("submit").addEventListener("click", function() {
    if (clues.length === 0) return;
    
    const userAnswer = document.getElementById("answer").value.trim().toLowerCase();
    const correctAnswer = clues[currentIndex].answer.toLowerCase();
    const result = document.getElementById("result");

    if (userAnswer === correctAnswer) {
        result.textContent = "Correct Answer!";
        result.style.color = "green";
        // Move to next clue after a short delay
        setTimeout(() => {
            currentIndex = (currentIndex + 1) % clues.length;
            loadClue();
        }, 1500);
    } else {
        result.textContent = "Wrong Answer. Try Again!";
        result.style.color = "red";
    }
});

// Hint button functionality
document.getElementById("hintBtn").addEventListener("click", function() {
    if (clues.length === 0) return;
    
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