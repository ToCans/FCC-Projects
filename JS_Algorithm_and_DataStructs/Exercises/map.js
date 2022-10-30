function orbitalPeriod(arr) {
    const GM = 398600.4418;
    const earthRadius = 6367.4447;
    function formula(alt) {
        let period = 2 * Math.PI * (alt ** 3 / GM) ** (1 / 2);
        return Math.round(period);
    }

    for (let index = 0; index < arr.length; index++) {
        //console.log(arr[index]);
        arr[index].orbitalPeriod = formula(arr[index].avgAlt + earthRadius);
        delete arr[index].avgAlt;
        //console.log(arr[index]);
    }
    console.log(arr);
    return arr;
}

orbitalPeriod([
    { name: 'iss', avgAlt: 413.6 },
    { name: 'hubble', avgAlt: 556.7 },
    { name: 'moon', avgAlt: 378632.553 },
]);
