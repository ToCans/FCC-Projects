function addTogether() {
    let [first, second] = arguments;
    //console.log(second);
    if (typeof first !== 'number') {
        return undefined;
    }
    if (arguments.length === 1) {
        // Returns a function that requres a second parameter for the "addTogether" function. Think of it as feeding in a second parameter for the final return of first + second
        return (second) => addTogether(first, second);
    }
    if (typeof second !== 'number') {
        return undefined;
    }
    return first + second;
}

console.log(addTogether(5)(7));
