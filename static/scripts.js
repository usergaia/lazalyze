document.addEventListener("DOMContentLoaded", function() {
    var input = document.getElementById("userInput");
    var showBtn = document.getElementById("enterBtn");

    // Create or get the error message element
    var errorMsg = document.getElementById("inputError");
    if (!errorMsg) {
        errorMsg = document.createElement("div");
        errorMsg.id = "inputError";
        errorMsg.style.color = "#d7263d";
        errorMsg.style.fontSize = "0.98rem";
        errorMsg.style.marginTop = "0.5rem";
        errorMsg.style.display = "none";
        input.parentNode.appendChild(errorMsg);
    }

    if (showBtn && input) {
        showBtn.addEventListener("click", function(e) {
            var value = input.value;
            if (!value.includes(".com")) {
                errorMsg.textContent = "Invalid link, input a valid link.";
                errorMsg.style.display = "block";
                e.preventDefault(); // prevent form submission
            } else {
                errorMsg.style.display = "none";
            }
        });
    }

    // Make all result images clickable to open in a new tab
    var imgs = document.querySelectorAll('.result-img-combo');
    imgs.forEach(function(img) {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function() {
            window.open(img.src, '_blank');
        });
    });
});