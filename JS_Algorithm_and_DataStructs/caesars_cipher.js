function rot13(str) {
    let counter = 0;
    let cipher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let punctuation = '!?. ';
    let returnString = '';
    for (let index = 0; index < str.length; index++) {
        console.log(str[index]);
        if (punctuation.indexOf(str[index]) >= 0) {
            returnString += str[index];
        } else {
            counter = 0;
            for (let subindex = 0; subindex < cipher.length; subindex++) {
                counter++;
                if (cipher[subindex] == str[index]) {
                    counter += 12;
                    if (counter > 25) {
                        counter -= 26;
                    }
                    returnString += cipher[counter];
                }
            }
        }
    }
    console.log(returnString);
    return returnString;
}

rot13('SERR PBQR PNZC');
