// Completed! Did this without learning regex, etc

function palindrome(str) {
  let stripped_string = "";
  let check_string = "abcdefghijklmnopqrstuvwxyz0123456789";
  let left_side = "";
  let right_side = "";

  // Stripping string
  for (var i = 0; i < str.length; i++){
    if (check_string.includes(str[i].toLowerCase())){
      stripped_string += str[i].toLowerCase();
    }
  }
  
  // Checking how str is spelt from left to right
  for (var j = 0; j < stripped_string.length; j++){
    left_side += stripped_string[j];
  }
    console.log(left_side);
  // Checking how str is spelt from right to left
  for (var k = stripped_string.length-1; k >= 0 ; k--){
    right_side += stripped_string[k];
  }
  console.log(right_side);
  
  // Return Statements
  if (left_side === right_side){
    console.log("True");
    return true;
  }
  else{
    console.log("False");
    return false;
  }
}

palindrome("eye");