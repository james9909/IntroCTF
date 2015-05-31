$(function() {

    $('#intro-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("intro-form");
    })
    $('#caesar-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("caesar-form");
    })
    $('#base-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("base-form");
    })
    $('#brutus-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("brutus-form");
    })

    function submit_problem(formid) {
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
