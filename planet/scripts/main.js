import { loadPlanet, setUpBackButton, setTitle } from "./ui.js";

document.addEventListener("DOMContentLoaded", () => {
    // Get the planet we are on
    const hash = window.location.hash.substring(1); // Substring removes the #
    // Back button functionality
    setUpBackButton();
    setTitle(hash);
    loadPlanet(hash);
});