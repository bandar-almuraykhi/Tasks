// Print Hello World
console.log("Hello, World!");

// Variables and Data Types
const name = "Bandar";
let age = 22;
let isStudent = true;
let city;
let phone = null;

// Print Variables and Their Types
console.log(name, typeof name);
console.log(age, typeof age);
console.log(isStudent, typeof isStudent);
console.log(city, typeof city);
console.log(phone, typeof phone);

// Change a Variable
age = 23;
console.log(age);

// Try to Change a Constant
// name = "Ahmed";

console.log();

// Arithmetic Operators
let a = 10;
let b = 5;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);

console.log();

// Increment and Decrement
let x = 10;

x++;
console.log(x);

x--;
console.log(x);

console.log();

// Comparison Operators
console.log(a === b);
console.log(a !== b);
console.log(a > b);
console.log(a < b);
console.log(a >= b);
console.log(a <= b);

console.log();

// Compare Different Data Types
console.log(5 === "5");

console.log();

// Logical Operators
let first = true;
let second = false;

console.log(first && second);
console.log(first || second);
console.log(!first);
console.log(!second);


console.log();

// Grade Result
let grade = 85;

if (grade >= 90) {
    console.log("Excellent");
} else if (grade >= 75) {
    console.log("Very Good");
} else if (grade >= 60) {
    console.log("Pass");
} else {
    console.log("Fail");
}

console.log();

// Day of the Week
let day = 3;

switch (day) {
    case 1:
        console.log("Sunday");
        break;

    case 2:
        console.log("Monday");
        break;

    case 3:
        console.log("Tuesday");
        break;

    case 4:
        console.log("Wednesday");
        break;

    case 5:
        console.log("Thursday");
        break;

    case 6:
        console.log("Friday");
        break;

    case 7:
        console.log("Saturday");
        break;

    default:
        console.log("Invalid day");
}

console.log();

// For Loop
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

console.log();

// While Loop
let count = 5;

while (count >= 1) {
    console.log(count);
    count--;
}

console.log();

// Do-While Loop
let num = 10;

do {
    console.log(num);
} while (num < 5);

console.log();

// Break and Continue
for (let i = 1; i <= 10; i++) {
    if (i === 5) {
        continue;
    }

    if (i === 7) {
        break;
    }

    console.log(i);
}

console.log();

// Addition Function
function add(a, b) {
    return a + b;
}

console.log(add(10, 5));
console.log(add(20, 30));
console.log(add(7, 3));

console.log();

// Check if a Number is Even
function isEven(number) {
    return number % 2 === 0;
}

console.log(isEven(10));
console.log(isEven(7));

console.log();

// Greeting Function
function greet(name) {
    return "Hello, " + name + "!";
}

console.log(greet("Bandar"));

// A parameter is a variable in the function definition.
// An argument is the actual value passed when calling the function.
