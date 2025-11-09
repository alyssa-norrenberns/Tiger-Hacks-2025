import { loadPlanet, setUpBackButton, setTitle, showCalendar, showLoading, hideLoading, showError } from "./ui.js";
import { calendarData } from "./api.js";

document.addEventListener("DOMContentLoaded", () => {
    // Get the planet we are on
    const hash = window.location.hash.substring(1); // Substring removes the #
    // Back button functionality
    setUpBackButton();
    setTitle(hash);
    loadPlanet(hash);
    // const calanderData = getCalendar(hash);
    // Fetch calendar data and show it in the UI (defaults to 'earth' when hash is empty)
    (async () => {
        const planetName = hash && hash.length ? hash : 'earth';
        try {
            showLoading('Loading calendar...');
            const calanderData = await calendarData(planetName);
            hideLoading();
            if (calanderData) {
                showCalendar(calanderData, planetName);
            } else {
                showError('Could not load calendar data. See console for details.');
            }
        } catch (err) {
            hideLoading();
            console.error(err);
            showError('Unexpected error while loading calendar data.');
        }
    })();
});