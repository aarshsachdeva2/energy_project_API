const API_URL = "http://127.0.0.1:8000/predict";


async function getPrediction() {

    const date = document.getElementById("date").value;
    const result = document.getElementById("result");

    if (!date) {
        result.textContent = "Please select a date.";
        return;
    }

    result.textContent = "Loading...";

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                date: date
            })

        });

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();

        result.textContent =
            "Predicted Load: " +
            Number(data.prediction).toLocaleString() +
            " MW";

    } catch (error) {

        console.error(error);

        result.textContent =
            "Could not connect to the API.";

    }
}