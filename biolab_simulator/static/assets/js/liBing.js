function addCompound() {
    const compound = document.querySelector(".add-compound select").value;
    if (!checkCompound(compound)) {
        alert("Composto já inserido.");
        return
    }

    const form = document.querySelector(".added-compounds");
    form.innerHTML += `
        <label for="${compound}">
            ${compound}
        </label>
        <input type='number' min='0' max='100' placeholder='0'
        name="${compound}" step="0.000001"><br>
    `;
}

function checkCompound(compound) {
    const compounds = document.querySelectorAll(".added-compounds input");
    let areEqual = true
    if (compounds.length === 0) {
        return true;
    }

    compounds.forEach(obj => {
        if (obj.name === compound) areEqual = false;
    });

    return areEqual
}