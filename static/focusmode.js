
const toggle = document.getElementById("focusToggle");

toggle.addEventListener("click", () => {
    document.body.classList.toggle("focus-mode");

    const enabled = document.body.classList.contains("focus-mode");
    toggle.textContent = enabled ? "Disable Focus Mode" : "Enable Focus Mode";
    toggle.setAttribute("aria-pressed", enabled);
});

