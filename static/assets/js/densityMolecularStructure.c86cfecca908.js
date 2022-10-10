let compoundIndex = 1;
const allCompounds = [];
let isCompoundAdded = false;

function addCompound() {
    const addedCompound = document.querySelector(".add-compound");
    const estherType = addedCompound.querySelector("select").value;
    const carbonsNumber = addedCompound.querySelector("input[id=carbons-number]").value;
    const doubleBonds = addedCompound.querySelector("input[id=double-bounds-number]").value;

    if (checkInputs(carbonsNumber, doubleBonds) === false) {
        alert("Por favor preencha todos os campos para prosseguir.");
        return
    } else if (checkInputs(carbonsNumber, doubleBonds) === "wrong fields") {
        alert ("O número de ligações duplas deve ser menor que o número de carbonos menos 1.");
        return
    } else if (checkInputs(carbonsNumber, doubleBonds) === "negative input") {
        alert("Por favor, forneça números positivos");
        return
    }

    const estherName = getEstherName(parseInt(estherType));

    let compoundDetails = {
        esther: estherName,
        carbons: carbonsNumber,
        db: doubleBonds
    };

    isCompoundAdded = checkRepetitiveCompound(compoundDetails);

    if (isCompoundAdded) {
        alert("Composto já inserido.");
        isCompoundAdded = false;
        return
    }

    allCompounds.push(compoundDetails);

    const form = document.querySelector(".added-compounds");
    form.innerHTML += `
        <label for="${estherName}">
            ${"Parâmetro do " + estherName}
        </label>
        <input name="${"Esther parameter " + String(compoundIndex)}" type='number' value=${estherType} readonly>
        <label for="${"Carbons number " + String(compoundIndex)}">
            Número de carbonos
        </label>
        <input name="${"Carbons number " + String(compoundIndex)}" type='number' value=${carbonsNumber} min="1">
        <label for="${"Double bonds " + String(compoundIndex)}">
            Número de duplas ligações
        </label>
        <input name="${"Double bonds " + String(compoundIndex)}" type='number' value=${doubleBonds} min=0 max=${carbonsNumber - 1}>
        <label for="${"Molar fraction " + String(compoundIndex)}">
            Fração molar (%)
        </label>
        <input name="${"Molar fraction " + String(compoundIndex)}" type='number' placeholder='0' min=0 max=100 value=0>
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
        case 1:
            return "Metil"
        case 2:
            return "Etil"
        case 3:
            return "Propil"
        default:
            return "Butil"
    }
}