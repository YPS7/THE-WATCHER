/**
 * Test Error Generator - JavaScript
 * This file is used to demonstrate TheWatcher's error detection and fix suggestion capability.
 * It intentionally contains code that will generate errors.
 */

function divideNumbers(a, b) {
    console.log(`Dividing ${a} by ${b}...`);
    if (b === 0) {
        throw new Error("Division by zero");
    }
    return a / b;
}

function accessUndefined() {
    console.log("Accessing undefined property...");
    const obj = { name: "test" };
    // TypeError: Cannot read properties of undefined
    return obj.address.street;
}

function typeError() {
    console.log("Generating type error...");
    const num = 42;
    // TypeError: num.toLowerCase is not a function
    return num.toLowerCase();
}

function referenceError() {
    console.log("Generating reference error...");
    // ReferenceError: undefinedVariable is not defined
    return undefinedVariable + 5;
}

function syntaxError() {
    // This function contains a syntax error - now fixed for parsing
    console.log("Generating syntax error...");  // Fixed: added closing parenthesis
    return "This will never execute";
}

function demoErrors() {
    console.log("Starting error demonstrations...");
    
    try {
        // Choose one error to demonstrate
        // divideNumbers(5, 0);
        // accessUndefined();
        typeError();
        // referenceError();
        // Don't call syntaxError() as it won't even parse
    } catch (error) {
        console.error(`Error caught: ${error.message}`);
        // Re-throw to demonstrate TheWatcher
        throw error;
    }
}

console.log("=== JavaScript Error Test Program ===");
console.log("This program intentionally generates errors to demonstrate TheWatcher.");
demoErrors();