console.log("JavaScript Ready");

$page = document.querySelector("#page-indicator");

document.querySelector("#home-link").classList.remove("active");
document.querySelector("#about-link").classList.remove("active");
document.querySelector("#contact-link").classList.remove("active");
if (document.querySelector("#login-link")) {
    document.querySelector("#login-link").classList.remove("active");
}
document.querySelector("#posts-link").classList.remove("active");

switch ($page.innerHTML) {
    case "Home":
        document.querySelector("#home-link").classList.add("active");
        break;

    case "About":
        document.querySelector("#about-link").classList.add("active");
        break;

    case "Contact":
        document.querySelector("#contact-link").classList.add("active");
        break;

    case "Login":
        document.querySelector("#login-link").classList.add("active");
        break;

    case "Posts":
        document.querySelector("#posts-link").classList.add("active");
        break;

    default:
        break;
}

const sendEmailMessage = () => {
    let isValidEmail = document.querySelector('#id_from_email').checkValidity();
    let isValidSubject = document.querySelector('#id_subject').checkValidity();
    let isValidMessage = document.querySelector('#id_message').checkValidity();

    if (isValidEmail && isValidSubject && isValidMessage) {
        document.querySelector("#email-button").disabled = false;
        document.querySelector("#email-button").click();
        document.querySelector("#email-button").disabled = true;
    } else {
        document.querySelector("#email-button").disabled = false;
        document.querySelector("#close-it").click();
        document.querySelector("#contact-form").submit();
        document.querySelector("#email-button").disabled = true;

    }


}

