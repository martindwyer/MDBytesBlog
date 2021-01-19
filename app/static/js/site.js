console.log("JavaScript Ready");

$page = document.querySelector("#page-indicator");

switch ($page.innerHTML) {
  case "Home":
    document.querySelector("#home-link").classList.add("active");
    document.querySelector("#about-link").classList.remove("active");
    document.querySelector("#contact-link").classList.remove("active");
    document.querySelector("#login-link").classList.remove("active");
    break;

  case "About":
    document.querySelector("#home-link").classList.remove("active");
    document.querySelector("#about-link").classList.add("active");
    document.querySelector("#contact-link").classList.remove("active");
    document.querySelector("#login-link").classList.remove("active");
    break;

  case "Contact":
    document.querySelector("#home-link").classList.remove("active");
    document.querySelector("#about-link").classList.remove("active");
    document.querySelector("#contact-link").classList.add("active");
    document.querySelector("#login-link").classList.remove("active");
    break;

  case "Login":
    document.querySelector("#home-link").classList.remove("active");
    document.querySelector("#about-link").classList.remove("active");
    document.querySelector("#contact-link").classList.remove("active");
    document.querySelector("#login-link").classList.add("active");
    break;

  default:
    break;
}
