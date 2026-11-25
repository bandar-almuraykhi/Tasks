
// Test external JavaScript
console.log("Hello from the script tag!");

// Display the DOM
console.log(document);

// Find the heading by ID
let title = document.getElementById("title");

console.log(title);

// Find all paragraphs by tag name
let paragraphs = document.getElementsByTagName("p");

console.log(paragraphs);

// Find all cards by class name
let cards = document.getElementsByClassName("card");

console.log(cards);

// Find the first card using querySelector
let firstCard = document.querySelector(".card");

console.log(firstCard);

// Find all cards using querySelectorAll
let allCards = document.querySelectorAll(".card");

console.log(allCards);

// Change the heading text
title.textContent = "Hello JavaScript DOM";

// Add HTML content to the empty box
let box = document.getElementById("box");

box.innerHTML = "<h2>Added by JavaScript</h2><p>This was not in the HTML file.</p>";

// Display HTML tags as plain text
// box.textContent = "<strong>Hello</strong>";

// Display HTML tags as actual HTML
// box.innerHTML = "<strong>Hello</strong>";

// Change the heading color
title.style.color = "red";

// Change the text color of all cards
for (let i = 0; i < allCards.length; i++) {
    allCards[i].style.color = "blue";
}
