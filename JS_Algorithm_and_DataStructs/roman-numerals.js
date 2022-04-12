// 2nd Project for Decimal to Roman Numeral Conversions

function convertToRoman(num) {
    let input = num.toString();
    let input_length = input.length;
    let bot = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
    let dec = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    let cent = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    let thou = ["", "M", "MM", "MMM"];
    let output = "";

    for (let counter = 0; counter < input.length; counter++) {
        let place = input_length - counter;

        if (place == 4) {
            output += thou[input[counter]];
        } else if (place == 3) {
            output += cent[input[counter]];
        } else if (place == 2) {
            output += dec[input[counter]];
        } else if (place == 1) {
            output += bot[input[counter]];
        } else {
            return "The Number is too long for Roman Numerals.";
        }
    }
    return output;
}

convertToRoman(36);
