document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("file");
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("/upload", {
        method: "POST",
        body: formData,
    });

    const result = await response.json();
    if (response.ok) {
        document.getElementById("frameworkSelection").style.display = "block";
        document.getElementById("generateButton").dataset.filepath = result.filepath;
    } else {
        alert(result.error);
    }
});

document.getElementById("generateButton").addEventListener("click", async () => {
    const framework = document.getElementById("framework").value;
    const filepath = document.getElementById("generateButton").dataset.filepath;

    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ framework, filepath }),
    });

    const result = await response.json();
    if (response.ok) {
        document.getElementById("output").textContent = result.scripts;
        document.getElementById("outputContainer").style.display = "block";
    } else {
        alert(result.error);
    }
});