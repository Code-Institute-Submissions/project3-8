    function sendmail(contactForm) {
        console.log("heh im in sendmail.")
        emailjs.send(
                "gmail", "template_5CenzoeC", {
                    "from_email": "ciaran.quinlan@gmail.com",
                    "reply_to": "ciaran.quinlan@gmail.com",
                    "from_name": "The Full Stack team",
                    "to_name": "to name",
                    "contact_name": contactForm.name.value,
                    "contact_phone": contactForm.phone.value,
                    "contact_email": contactForm.email.value,
                    "contact_message": contactForm.message.value
                }
            )
            .then(
                function (response) {
                    console.log("SUCCESS", response);
                },
                function (error) {
                    console.log("FAILED", error);
                }
            );
        return false; // To block from loading a new page
    }