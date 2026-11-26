// Get the Button and Heading
let button = document.getElementById("colorBtn");
let title = document.getElementById("title");

// Change Heading Color on Click
button.addEventListener("click", function (e) {
    title.style.color = "red";
    console.log(e.target);
});

// Get the Name Input and Preview
let nameInput = document.getElementById("nameInput");
let preview = document.getElementById("preview");

// Display the Name While Typing
nameInput.addEventListener("input", function () {
    preview.textContent = nameInput.value;
});

// Detect Keyboard Events
document.addEventListener("keydown", function (e) {
    console.log("Key pressed!");
    console.log(e);
    console.log(e.key);
});


// Get the Form, Email Input and Message
let form = document.getElementById("myForm");
let emailInput = document.getElementById("emailInput");
let message = document.getElementById("message");


// Handle Form Submission
form.addEventListener("submit", function (e) {
    e.preventDefault();

    if (emailInput.value === "") {
        message.textContent = "Please enter your email";
    } else {
        message.textContent = "Thank you! We will contact you at " + emailInput.value;
    }
});
