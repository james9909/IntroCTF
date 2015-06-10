function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

function validateCookie(name) {
    cookie = getCookie(name);
    return (cookie == "" || cookie == null);
}

function validateLogin() {
    isValid = validateCookie("tid") && validateCookie("token")
    if (isValid) {
        document.getElementById("navbar").innerHTML += "<li><a href='login'>Login</a></li>"
        document.getElementById("navbar").innerHTML += "<li><a href='register'>Register</a></li>"
    } else {
        document.getElementById("navbar").innerHTML += "<li><a onclick='logout()'>Log Out</a></li>"
    }
}

function validateMobileLogin() {
    isValid = validateCookie("tid") && validateCookie("token")
    if (isValid) {
        document.getElementById("nav-mobile").innerHTML += "<li><a class='waves-effect waves-indigo' href='login'>Login</a></li>"
        document.getElementById("nav-mobile").innerHTML += "<li><a class='waves-effect waves-indigo' href='register'>Register</a></li>"
    } else {
        document.getElementById("nav-mobile").innerHTML += "<li><a onclick='logout()' class='waves-effect waves-indigo'>Log Out</a></li>"
    }
}
