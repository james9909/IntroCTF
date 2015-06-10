$(function() {

    $('#register-form').on('submit', function(event){
        event.preventDefault();
        register("register-form");
    })
    $('#login-form').on('submit', function(event){
        event.preventDefault();
        login("login-form");
    })
    function register(formid) {
        $.ajax({
            url: "scripts/registration_handler.py",
            type: "POST",
            data: $("form[id=" + formid + "]").serialize(),
            success: function(response) {
                Materialize.toast(response, 4000);
                setTimeout(function(){
                    location.reload();
                }, 2000);
            }
        });
    }

    function login(formid) {
        $.ajax({
            url: "scripts/login_handler.py",
            type: "POST",
            data: $("form[id=" + formid + "]").serialize(),
            success: function(response) {
                Materialize.toast(response, 4000);
                if (response.includes("Success")) {
        	    $.ajax({
        	        url: "scripts/login.py",
        	        type: "POST",
        	        data: $("form[id=" + formid + "]").serialize(),
        	        success: function(response) {
                            response = response.split(",");
                            document.cookie = "token=" + response[0] + "; expires=Thur, 2 Aug 9001 20:47:11 UTC path=/";
                            document.cookie = "tid=" + response[1] + "; expires=Thur, 2 Aug 9001 20:47:11 UTC path=/";
                            setTimeout(function(){
                                location.reload();
                            }, 2000);
        	        }
        	    });
                }
            }
        });

    }

});
var deleteCookie = function(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
};
function logout() {
    deleteCookie("tid");
    deleteCookie("token");
    Materialize.toast("Logged out");
    setTimeout(function(){
        location.reload();
    }, 2000);

}
