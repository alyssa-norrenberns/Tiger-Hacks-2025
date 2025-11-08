// Clicking on planets take you to /planet/planetName
export function setupPlanetClicks() {
    const planets = document.querySelectorAll(".planet");

    planets.forEach((planet) => {
        planet.addEventListener("click", () => {
            const planetName = planet.id;
            window.location.href = `planet/#${planetName}`;
        });
    });
}