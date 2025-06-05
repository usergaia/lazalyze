document.addEventListener("DOMContentLoaded", function() {
    var input = document.getElementById("userInput");
    var showBtn = document.getElementById("showBtn");
    var display = document.getElementById("displayText");

    if (showBtn && input && display) {
        showBtn.addEventListener("click", function() {
            display.textContent = input.value;
        });
    }
});