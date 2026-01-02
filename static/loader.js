const form = document.getElementById("brainform");
const loader = document.getElementById("loader");
const outputText = document.getElementById("output-text");

if (form && loader && outputText) {
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

    
        form.style.display = "none";
        loader.style.display = "block";
        outputText.textContent = "";

        try {
            const response = await fetch(form.action, {
                method: "POST",
                headers: { "X-Requested-With": "fetch" },
                body: new FormData(form)
            });

            const result = await response.text();
            outputText.textContent = result;
        } catch (err) {
            outputText.textContent = "Something went wrong. Please try again.";
        } finally {
            loader.style.display = "none";
            form.style.display = "block";
        }
    });
}
