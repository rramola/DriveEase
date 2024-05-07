document.addEventListener("DOMContentLoaded", function() {
    var usernameField = document.getElementById("id_username");
    var emailField = document.getElementById("id_email");
    var passOneField = document.getElementById("id_password1");
    var passTwoField = document.getElementById("id_password2");
    
    if (usernameField) {
        usernameField.placeholder = "Username..";
        }
    if (emailField) {
        emailField.placeholder = "Email..";
        }
    if (passOneField){
        passOneField.placeholder = "Password..";
        }
    if (passTwoField) {
        passTwoField.placeholder = "Password..";
        }
    }
    );