export function loadPlanet(hash) {
    const container = document.querySelector(".planet-container");
    // Make scene for object
    const scene = new THREE.Scene();
    
    // Create camera
    const camera = new THREE.PerspectiveCamera(
        75,
        container.clientWidth / container.clientHeight,
        0.1,
        1000
    );
    camera.position.z = 50;
    
    // Create renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);

    // Create geometry + material with texture
    const geometry = new THREE.SphereGeometry(23, 32, 32);
    const texture = new THREE.TextureLoader().load(`../../textures/${hash}.jpg`);
    const material = new THREE.MeshPhongMaterial({ map: texture, shininess: 10 });
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    const light = new THREE.DirectionalLight(0xffffff, 3);
    light.position.set(50, 50, 50);
    scene.add(light);
    scene.add(new THREE.AmbientLight(0xffffff, 0.2));

    // Animation loop (where the sphere is drawn)
    function animate() {
        requestAnimationFrame(animate);
        
        // Rotation of sphere by default
        sphere.rotation.y += 0.005;
        sphere.rotation.x += 0.001;
        
        renderer.render(scene, camera);
    }
    animate();
    
    // Handle window resize
    window.addEventListener("resize", () => {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });
};

export function setUpBackButton() {
    const backButton = document.querySelector(".back-arrow");
    backButton.addEventListener("click", () => {
        window.location.href = "/";
    });
};

export function setTitle(hash) {
    const titleElement = document.querySelector(".title");
    titleElement.textContent = hash.charAt(0).toUpperCase() + hash.slice(1);
}

export function showCalendar(data, hash) {
    const container = document.querySelector(".data-container");

    // Find the existing Calendar Info list in the page and replace its contents
    const calendarList = container.querySelector('ul.space-mono-regular');
    if (!calendarList) {
        // Fallback: append a new list if the expected element is missing
        const fallback = document.createElement('ul');
        fallback.classList.add('space-mono-regular');
        container.appendChild(fallback);
    }

    const ul = container.querySelector('ul.space-mono-regular');
    // Clear existing items
    ul.innerHTML = '';

    const liTitle = document.createElement('li');
    liTitle.textContent = `${data.planet_title} — Calendar Info`;
    liTitle.classList.add('space-mono-bold', 'font-medium');
    ul.appendChild(liTitle);

    const liDaysPerYear = document.createElement('li');
    liDaysPerYear.textContent = `Days per year: ${data.days_per_year}`;
    ul.appendChild(liDaysPerYear);

    const liDayLength = document.createElement('li');
    liDayLength.textContent = `Day length (hours): ${data.day_length_hours}`;
    ul.appendChild(liDayLength);

    const liPlanetDays = document.createElement('li');
    liPlanetDays.textContent = `Planet days since Earth Jan 1: ${data.planet_days_since_jan_1}`;
    ul.appendChild(liPlanetDays);

    if (data.earth_days_since_jan_1 !== null && data.earth_days_since_jan_1 !== undefined) {
        const liEarthDays = document.createElement('li');
        liEarthDays.textContent = `Earth days since Jan 1: ${data.earth_days_since_jan_1}`;
        ul.appendChild(liEarthDays);
    }
}

export function showLoading(message = 'Loading…') {
    const container = document.querySelector('.data-container');
    // remove previous error
    const prevErr = container.querySelector('.api-error');
    if (prevErr) prevErr.remove();

    let el = container.querySelector('.api-loading');
    if (!el) {
        el = document.createElement('p');
        el.classList.add('api-loading');
        el.style.fontFamily = '"Space Mono", monospace';
        el.style.color = '#aaa';
        container.appendChild(el);
    }
    el.textContent = message;
}

export function hideLoading() {
    const container = document.querySelector('.data-container');
    const el = container.querySelector('.api-loading');
    if (el) el.remove();
}

export function showError(message) {
    const container = document.querySelector('.data-container');
    // remove previous loading
    hideLoading();
    // remove previous error
    const prev = container.querySelector('.api-error');
    if (prev) prev.remove();

    const err = document.createElement('p');
    err.classList.add('api-error');
    err.style.color = 'crimson';
    err.style.fontFamily = '"Space Mono", monospace';
    err.textContent = message;
    container.appendChild(err);
}