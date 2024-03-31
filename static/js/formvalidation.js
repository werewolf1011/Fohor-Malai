document.addEventListener("DOMContentLoaded", function () {

  const password = document.getElementById("password");
  const confirmPassword = document.getElementById("confirmPassword");
  const passwordMatchError = document.getElementById("passwordMatchError");

  function validatePassword() {
    if (password.value !== confirmPassword.value) {
      passwordMatchError.style.display = "block";
      confirmPassword.setCustomValidity("Passwords do not match");
    } else {
      passwordMatchError.style.display = "none";
      confirmPassword.setCustomValidity("");
    }
  }

  password.addEventListener("input", validatePassword);
  confirmPassword.addEventListener("input", validatePassword);
});
