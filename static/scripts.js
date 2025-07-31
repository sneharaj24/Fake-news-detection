const fileInput = document.getElementById("input");
const uploadForm = document.getElementById("uploadForm");
const outputContainer = document.querySelector(".output-container");
const waitingAnimation = document.getElementById("waitingAnimation");

// Function to trigger file input click
function triggerFileInput() {
  fileInput.click();
}

// Automatically submit the form when a file is selected
fileInput.addEventListener("change", () => {
  if (fileInput.files.length > 0) {
    waitingAnimation.style.display = "flex";
    uploadForm.submit();
  }
});

// Show loading animation when form is submitted
form.addEventListener("submit", () => {
  // Show loading spinner and hide form content
  document.getElementById("loadingContainer").style.display = "flex";
  document.getElementById("form").style.display = "none";
});

// Hide loading animation and display content after the process is completed
function hideLoading() {
  document.getElementById("loadingContainer").style.display = "none";
  document.getElementById("form").style.display = "block";
}
