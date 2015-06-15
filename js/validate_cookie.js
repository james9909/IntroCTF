function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

function validateCookie(name) {
    cookie = getCookie(name);
    return !(cookie == "" || cookie == null);
}

function validateCookies() {
    return validateCookie("tid") && validateCookie("token");
}
function validateLogin() {
    isValid = validateCookies();
    if (isValid) {
        document.getElementById("navbar").innerHTML += "<li><a id='logout'>Log Out</a></li>"
    } else {
        document.getElementById("navbar").innerHTML += "<li><a href='login'>Login</a></li>"
        document.getElementById("navbar").innerHTML += "<li><a href='register'>Register</a></li>"
    }
}

function validateMobileLogin() {
    isValid = validateCookie("tid") && validateCookie("token")
    if (isValid) {
        document.getElementById("nav-mobile").innerHTML += "<li><a id='logout' class='waves-effect waves-indigo'>Log Out</a></li>"
    } else {
        document.getElementById("nav-mobile").innerHTML += "<li><a class='waves-effect waves-indigo' href='login'>Login</a></li>"
        document.getElementById("nav-mobile").innerHTML += "<li><a class='waves-effect waves-indigo' href='register'>Register</a></li>"
    }
}
