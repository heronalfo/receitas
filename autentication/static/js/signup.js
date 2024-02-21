function togglePasswordVisibility() {

  const passwordInput = document.getElementById("passwordInput");
  
  const passwordToggle = document.querySelector(".password-toggle");
  
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    
    passwordToggle.classList.remove("fa-eye");
    passwordToggle.classList.add("fa-eye-slash");
    
  } else {
    passwordInput.type = "password";
    passwordToggle.classList.remove("fa-eye-slash");
    passwordToggle.classList.add("fa-eye");
  }
  
}

function togglePasswordRepeatVisibility() {

  const passwordInput = document.getElementById("passwordRepeatInput");
  
  const passwordRepeatToggle = document.querySelector(".password-repeat-toggle");
  
  if (passwordRepeatInput.type === "password") {
    passwordRepeatInput.type = "text";
    
    passwordRepeatToggle.classList.remove("fa-eye");
    passwordRepeatToggle.classList.add("fa-eye-slash");
    
  } else {
    passwordInput.type = "password";
    passwordRepeatToggle.classList.remove("fa-eye-slash");
    passwordRepeatToggle.classList.add("fa-eye");
  }
  
}