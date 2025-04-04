function predict() {
    // Get form values
    const age = parseInt(document.getElementById("age").value);
    const job = document.getElementById("job").value;
    const marital = document.getElementById("marital").value;
    const education = document.getElementById("education").value;
    const creditDefault = document.getElementById("default").value;
    const housing = document.getElementById("housing").value;
    const loan = document.getElementById("loan").value;

    // Input validation
    if (isNaN(age) || age < 18 || age > 120) {
        Swal.fire("Error", "Age must be between 18 and 120!", "warning");
        return;
    }
    if (!job || !marital || !education || !creditDefault || !housing || !loan) {
        Swal.fire("Error", "All fields are required!", "warning");
        return;
    }

    const formData = { age, job_code: parseInt(job), marital_code: parseInt(marital), education_code: parseInt(education), default_code: parseInt(creditDefault), housing_code: parseInt(housing), loan_code: parseInt(loan) };

    // Send data to Flask API
    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            Swal.fire("Prediction Result", `The predicted outcome is: ${data.prediction}`, "success");
        })
        .catch(error => {
            Swal.fire("Error", "Something went wrong!", "error");
            console.error("Error:", error);
        });
}
