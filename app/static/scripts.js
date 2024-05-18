document.addEventListener("DOMContentLoaded", function() {
    var usernameField = document.getElementById("id_username");
    var firstNameField = document.getElementById("id_first_name");
    var lastNameField = document.getElementById("id_last_name");
    var emailField = document.getElementById("id_email");
    var passOneField = document.getElementById("id_password1");
    var passTwoField = document.getElementById("id_password2");
    var addVehicleYearField = document.getElementById("id_year")
    var addVehicleMakeField = document.getElementById("id_make")
    var addVehicleModelField = document.getElementById("id_model")
    var createListingPriceField = document.getElementById("id_price")

    if (usernameField) {
        usernameField.placeholder = "Username..";
        }

    if (firstNameField) {
            firstNameField.placeholder = "First Name..";
            }

    if (lastNameField) {
            lastNameField.placeholder = "Last Name..";
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
        
    if (addVehicleYearField) {
        addVehicleYearField.placeholder = "Year..";
        }
    
    if (addVehicleMakeField) {
        addVehicleMakeField.placeholder = "Make..";
        }
    
    if (addVehicleModelField) {
        addVehicleModelField.placeholder = "Model..";
        }

    if (createListingPriceField) {
        createListingPriceField.placeholder = "Price per week"
    }

    });