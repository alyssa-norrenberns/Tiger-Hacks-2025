const API_BASE_URL = "http://127.0.0.1:5050/";


export async function getCalendar(hash) {
    try {
        const response = await fetch(`${API_BASE_URL}planet/calander?=${hash}`, {
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