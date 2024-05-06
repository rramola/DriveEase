document.addEventListener("DOMContentLoaded", function() {
    var usernameField = document.getElementById("id_username");
    var emailField = document.getElementById("id_email");
    var passOneField = document.getElementById("id_password1");
    var passTwoField = document.getElementById("id_password2");
    
    usernameField.placeholder = "Username..";
    emailField.placeholder = "Email..";
    passOneField.placeholder = "Password..";
    passTwoField.placeholder = "Password..";
}
    );