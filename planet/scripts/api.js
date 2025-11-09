async function getCalander() {
    try {
        const response = await fetch(`${API_BASE_URL}planet/calander?=planet${hash}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error("Backend error:", errorData);
            return null;
        }

        // Get response from API
        const result = await response.json();
        console.log(result);
        return result;
    }
    catch (err) {
        console.error("Error", err);
    }
}