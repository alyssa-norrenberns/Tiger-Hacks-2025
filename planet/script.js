// Back button functionality
const backButton = document.querySelector(".back-arrow");
backButton.addEventListener("click", () => {
    window.location.href = "/";
});

// Dyanmically set title as hash in url
const hash = window.location.hash.substring(1); // Substring removes the #
const titleElement = document.querySelector(".title");
titleElement.textContent = hash.charAt(0).toUpperCase() + hash.slice(1);