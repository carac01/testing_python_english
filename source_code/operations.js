function sum(number1, number2) {
    return number1 + number2;
}

function subtraction(number1, number2) {
    return number1 - number2;
}

// Export to call it from another modules/places
module.exports = {
    sum,
    subtraction
};