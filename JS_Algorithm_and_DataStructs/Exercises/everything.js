function truthCheck(collection, pre) {
    let flag = true;
    for (let index = 0; index < collection.length; index++) {
        console.log(Boolean(collection[index][pre]));
        if (Boolean(collection[index][pre]) == false) {
            flag = false;
        }
    }
    console.log('Returned Val ' + flag);
    return flag;
}

truthCheck(
    [
        { name: 'Pikachu', number: 25, caught: 3 },
        { name: 'Togepi', number: 175, caught: 1 },
        { name: 'MissingNo', number: NaN, caught: 0 },
    ],
    'number'
);
