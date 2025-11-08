// Back button functionality
const backButton = document.querySelector(".back-arrow");
backButton.addEventListener("click", () => {
    window.location.href = "/";
});

// Dyanmically set title as hash in url
const hash = window.location.hash.substring(1); // Substring removes the #
const titleElement = document.querySelector(".title");
titleElement.textContent = hash.charAt(0).toUpperCase() + hash.slice(1);

window.onload = () => {
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
    const texture = new THREE.TextureLoader().load(`../textures/${hash}.jpg`);
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