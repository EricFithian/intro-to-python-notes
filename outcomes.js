// ## 1. **Create Phone Number**

// Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

// Example:

// createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"


// ## 2. **RGB To Hex Conversion**

// The RGB function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

// **Note**: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

// The following are examples of expected output values:

function rgb(r, g, b) {
    const arr = [r, g, b];
    // I want to create a variable that will be output for this function
    let output = "";

    // rgb to hex is found by dividing each of the r, g and b by 16. The whole number and the remainder are 0 - 9 or A - F if it's 10 or more. 
    const rgbConverter = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    // I want to loop through the array I created and add the whole number and then the remainder from each number according to the above conditions.
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] >= 255) {
            output += "FF";
            continue;
        } else if(arr[i] <= 0) {
            output += "00";
            continue;
        }
        const wholeNumber = Math.floor(arr[i] / 16);
        const remainder = arr[i] % 16;
        // console.log(wholeNumber, remainder)
        // Check if the whole number is 10 or more. Meaning it's part of my lookup table
        if(rgbConverter[wholeNumber]) {
            output += rgbConverter[wholeNumber]
        } else {
            output += wholeNumber
        }
        rgbConverter[remainder] ? output += rgbConverter[remainder] : output += remainder
    }
    return output;
}

console.log(rgb(255, 255, 255)) // returns FFFFFF
console.log(rgb(255, 255, 300)) // returns FFFFFF
console.log(rgb(0,-1,-300)) // returns 000000
console.log(rgb(148, 0, 211)) // returns 9400D3