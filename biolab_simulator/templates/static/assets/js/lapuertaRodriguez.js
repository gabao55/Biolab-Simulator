let compoundIndex = 1;
const allCompounds = [];
let isCompoundAdded = false;

function addCompound() {
    const compounds = document.querySelector(".added-compounds");
    const addedCompound = document.querySelector(".add-compound");
    const estherType = addedCompound.querySelector("select").value;
    const carbonsNumber = addedCompound.querySelector("input[name=carbons-number]").value;
    const doubleBonds = addedCompound.querySelector("input[name=double-bounds-number]").value;

    if (checkInputs(carbonsNumber, doubleBonds) === false) {
        alert("Please fill all fields to proceed.");
        return
    } else if (checkInputs(carbonsNumber, doubleBonds) === "wrong fields") {
        alert ("Number of double bonds should be smaller then the number of carbons minus 1.");
        return
    } else if (checkInputs(carbonsNumber, doubleBonds) === "negative input") {
        alert("Please provide positive numbers");
        return
    }

    const estherName = getEstherName(estherType);

    let compoundDetails = {
        esther: estherName,
        carbons: carbonsNumber,
        db: doubleBonds
    };

    isCompoundAdded = checkRepetitiveCompound(compoundDetails);

    // for (let i = 0; i < allCompounds.length; i++) {
    //     if (allCompounds[i] === compoundDetails) {
    //         return isCompoundAdded = true;
    //     }
    // }

    if (isCompoundAdded) {
        alert("Compound already added.");
        isCompoundAdded = false;
        return
    }

    allCompounds.push(compoundDetails);

    const form = document.querySelector(".added-compounds");
    form.innerHTML += `
        <label for="${estherName}">
            ${estherName + " parameter"}
        </label>
        <input type='number' value=${estherType} readonly>
        <label for="${"Carbons number" + String(compoundIndex)}">
            Carbons number
        </label>
        <input type='number' value=${carbonsNumber} min="1">
        <label for="${"Double bonds" + String(compoundIndex)}">
            Double bond
        </label>
        <input type='number' value=${doubleBonds} min=0 max=${carbonsNumber - 1}>
        <br>
    `;

    compoundIndex ++;

}

function checkInputs(carbonsNumber, doubleBonds) {
    if (!carbonsNumber || !doubleBonds) {
        return false
    } else if (doubleBonds > carbonsNumber - 1) {
        return "wrong fields"
    } else if (doubleBonds < 0) {
        return "negative input"
    }

    return true
}

function checkRepetitiveCompound(compound) {
    for (let i = 0; i < allCompounds.length; i++) {
        if (checkElements(compound, allCompounds[i])) {
            return true;
        }
    }
    return false
}

function checkElements(compoundX, compoundY) {
    if (compoundX.esther === compoundY.esther 
        && compoundX.carbons === compoundY.carbons
        && compoundX.db === compoundY.db) {
            return true
        }
    return false
}

function getEstherName(input) {
    switch (input) {
        case 2:
            return "Ethyl"
        case 3:
            return "Propyl"
        default:
            return "Butyl"
    }
}

console.log("Hello");