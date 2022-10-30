function checkCashRegister(price, cash, cid) {
    let change = cash - price;
    let coinsInDrawer = [];
    let coinsToReturn = [];
    let changeToGive = cash - price;
    let retChange = [];
    let retObj = {};
    let currency = [
        ['PENNY', 0.01],
        ['NICKEL', 0.05],
        ['DIME', 0.1],
        ['QUARTER', 0.25],
        ['DOLLAR', 1.0],
        ['FIVE', 5.0],
        ['TEN', 10.0],
        ['TWENTY', 20.0],
        ['ONE HUNDRED', 100],
    ];

    // Number of Coins/Bills currently in Cash Register
    for (let index = 0; index < cid.length; index++) {
        let num = parseInt((cid[index][1] / currency[index][1]).toFixed(0));
        coinsInDrawer.unshift([cid[index][0], currency[index][1], num]);
    }

    // Number of Coins/Bills to take from Cash Register
    for (let index = 0; index < currency.length; index++) {
        if (change >= coinsInDrawer[index][1]) {
            let remainder = parseFloat((change % coinsInDrawer[index][1]).toFixed(2));
            let coinsGiven = Math.floor(change / coinsInDrawer[index][1]);
            if (coinsGiven > coinsInDrawer[index][2]) {
                coinsGiven = coinsInDrawer[index][2];
            }
            if (remainder >= 0.0) {
                coinsToReturn.push([coinsInDrawer[index][0], coinsGiven]);
                change -= coinsGiven * coinsInDrawer[index][1];
                change = parseFloat(change.toFixed(2));
            }
        }
    }

    // Return Change
    for (let index = 0; index < coinsToReturn.length; index++) {
        for (let subindex = 0; subindex < coinsInDrawer.length; subindex++) {
            if (coinsToReturn[index][0] == coinsInDrawer[subindex][0]) {
                retChange.push([
                    coinsToReturn[index][0],
                    coinsInDrawer[subindex][1] * coinsToReturn[index][1],
                ]);
            }
        }
    }

    // Checking for sufficient funds
    let totalInDrawer = 0;
    for (let index = 0; index < cid.length; index++) {
        let float = parseFloat(cid[index][1].toFixed(2));
        totalInDrawer += float;
    }
    totalInDrawer = parseFloat(totalInDrawer.toFixed(2));
    let returnChange = 0;
    for (let index = 0; index < retChange.length; index++) {
        returnChange += retChange[index][1];
    }

    // Status of Drawer
    // Insufficient Funds
    if (changeToGive > returnChange) {
        retObj.status = 'INSUFFICIENT_FUNDS';
        retObj.change = [];
    } else if (totalInDrawer == returnChange) {
        retObj.status = 'CLOSED';
        for (let index = retChange.length; index >= 0; index--) {
            retChange.unshift([coinsInDrawer[index][0], coinsInDrawer[index][2]]);
        }
        retObj.change = retChange.reverse();
    } else {
        retObj.status = 'OPEN';
        retObj.change = retChange;
    }

    // Console Logs
    return retObj;
}
