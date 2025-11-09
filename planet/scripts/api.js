const API_BASE_URL = "http://127.0.0.1:5050/";


async function _fetchCalendar(planet) {
    // default to earth when no planet provided
    const p = (planet && planet.trim()) ? planet.trim() : 'earth';
    try {
        // Use the correctly spelled endpoint; backend also accepts the misspelled route,
        // but prefer the canonical `/planet/calendar` path.
        const response = await fetch(`${API_BASE_URL}planet/calendar?planet=${encodeURIComponent(p)}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            // try to read json error body, but fall back to text
            let errorBody = null;
            try { errorBody = await response.json(); } catch (e) { errorBody = await response.text(); }
            console.error("Backend error:", response.status, errorBody);
            return null;
        }

        const result = await response.json();
        console.log("calendar result:", result);
        return result;
    }
    catch (err) {
        console.error("Network or parsing error while fetching calendar:", err);
        return null;
    }
}

// Exported helpers. Keep getCalendar for backwards compatibility and add calendarData alias
export async function getCalendar(hash) {
    return await _fetchCalendar(hash);
}

export async function calendarData(hash) {
    return await _fetchCalendar(hash);
}

export default { getCalendar, calendarData };