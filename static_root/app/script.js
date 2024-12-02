// Smooth Scrolling for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Handle Multi-Step Form Navigation
document.addEventListener('DOMContentLoaded', function () {
    const steps = document.querySelectorAll('.step');
    const nextButtons = document.querySelectorAll('.btn-next');
    const backButtons = document.querySelectorAll('.btn-back');
    const submitButton = document.querySelector('.btn-submit');
    const confirmationMessage = document.createElement('div');
    let currentStep = 0;

    // Add confirmation message container for Step 4
    confirmationMessage.id = 'confirmation-message';
    confirmationMessage.style.display = 'none';
    confirmationMessage.innerHTML = `
        <h2>Booking Confirmed</h2>
        <p>Your booking has been successfully completed.</p>
        <p>Thank you for scheduling with us!</p>
    `;
    document.body.appendChild(confirmationMessage);

    // Function to show the current step
    function showStep(stepIndex) {
        steps.forEach((step, index) => {
            if (index === stepIndex) {
                step.style.display = 'block';
                step.classList.add('active');
            } else {
                step.style.display = 'none';
                step.classList.remove('active');
            }
        });
        if (stepIndex === steps.length) {
            // Show confirmation message
            steps.forEach(step => (step.style.display = 'none'));
            confirmationMessage.style.display = 'block';
        }
    }

    // Validation logic for Step 1
    function validateStep1() {
        const service = document.querySelector('#service');
        const location = document.querySelector('#location');
        const instructor = document.querySelector('#instructor');
        let valid = true;

        // Clear previous error messages
        [service, location, instructor].forEach(field => {
            const errorMessage = field.nextElementSibling;
            if (errorMessage && errorMessage.classList.contains('error-message')) {
                errorMessage.remove();
            }
            field.classList.remove('error');
        });

        // Validate fields
        if (!service.value) {
            valid = false;
            addErrorMessage(service, "Please select a service.");
        }
        if (!location.value) {
            valid = false;
            addErrorMessage(location, "Please select a location.");
        }
        if (!instructor.value) {
            valid = false;
            addErrorMessage(instructor, "Please select an instructor.");
        }

        return valid;
    }

    // Validation logic for Step 2
    function validateStep2() {
        const date = document.querySelector('#date');
        const time = document.querySelector('#time');
        let valid = true;

        // Clear previous error messages
        [date, time].forEach(field => {
            const errorMessage = field.nextElementSibling;
            if (errorMessage && errorMessage.classList.contains('error-message')) {
                errorMessage.remove();
            }
            field.classList.remove('error');
        });

        // Validate fields
        if (!date.value) {
            valid = false;
            addErrorMessage(date, "Please select a date.");
        }
        if (!time.value) {
            valid = false;
            addErrorMessage(time, "Please select a time.");
        }

        return valid;
    }

    // Function to add error messages below fields
    function addErrorMessage(field, message) {
        const error = document.createElement('span');
        error.className = 'error-message';
        error.style.color = 'red';
        error.style.fontSize = '12px';
        error.textContent = message;
        field.classList.add('error');
        field.insertAdjacentElement('afterend', error);
    }

    // Handle "Next" button clicks
    nextButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault(); // Prevent default behavior

            if (currentStep === 0 && !validateStep1()) return; // Stop if validation fails for Step 1
            if (currentStep === 1 && !validateStep2()) return; // Stop if validation fails for Step 2

            currentStep++;
            if (currentStep > steps.length) {
                currentStep = steps.length;
            }
            showStep(currentStep);
        });
    });

    // Handle "Back" button clicks
    backButtons.forEach(button => {
        button.addEventListener('click', function () {
            currentStep--;
            if (currentStep < 0) {
                currentStep = 0; // Prevent going below first step
            }
            showStep(currentStep);
        });
    });

    // Handle form submission at Step 3
    submitButton?.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent form submission

        // Example of sending data to a backend or logging it
        const name = document.querySelector('#name').value;
        const email = document.querySelector('#email').value;
        const phone = document.querySelector('#phone').value;

        if (name && email && phone) {
            currentStep++;
            showStep(currentStep); // Move to Step 4 (confirmation)
        } else {
            alert("Please fill out all required fields.");
        }

        // Optional: Send email using a backend API (e.g., with Fetch or Axios)
        // fetch('/api/send-email', {
        //     method: 'POST',
        //     body: JSON.stringify({ name, email, phone }),
        //     headers: { 'Content-Type': 'application/json' }
        // });
    });

    // Dynamically initialize Flatpickr for Step 2
    flatpickr("#date", {
        dateFormat: "d-m-Y",
        minDate: "today",
    });

    // Show the initial step
    showStep(currentStep);
});
