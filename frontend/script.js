// frontend/script.js
async function predictDrug() {
    const min_conc = parseFloat(document.getElementById('min_conc').value);
    const max_conc = parseFloat(document.getElementById('max_conc').value);
    const ln_ic50 = parseFloat(document.getElementById('ln_ic50').value);
    const aa_position = document.getElementById('aa_position').value;

    const response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            MIN_CONC: min_conc,
            MAX_CONC: max_conc,
            LN_IC50: ln_ic50,
            AA_POSITION: aa_position
        })
    });

    const data = await response.json();
    document.getElementById('result').innerHTML = `
        <strong>Predicted Drug:</strong> ${data.predicted_drug}<br>
        <strong>Sensitivity:</strong> ${data.sensitivity}<br>
        <strong>Input:</strong> MIN_CONC: ${min_conc}, MAX_CONC: ${max_conc}, LN_IC50: ${ln_ic50}
    `;
}
