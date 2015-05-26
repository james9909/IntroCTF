$(function() {

    $('#intro-form').on('submit', function(event){
        event.preventDefault();
        submit_handle("intro-form");
    })
    $('#caesar-form').on('submit', function(event){
        event.preventDefault();
        submit_handle("crypto1-form");
    })
    $('#crypto2-form').on('submit', function(event){
        event.preventDefault();
        submit_handle("crypto2-form");
    })

    function submit_handle(formid) {
        $.ajax({
            url: "scripts/problem_handler.py",
            type: "POST",
            data: $("form[id=" + formid + "]").serialize(),
            success: function(response) {
                Materialize.toast(response, 4000);
            }
        });

    }
});

function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}
