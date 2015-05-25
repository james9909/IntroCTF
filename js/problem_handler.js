$(function() {

    $('#post-form').on('submit', function(event){
        event.preventDefault();
        submit_handle();
    })

    function submit_handle() {
        $.ajax({
            url: "scripts/problem_handler.py",
            type: "POST",
            data: $("form[id=post-form]").serialize(),
            success: function(response) {
                alert(response);
            }
        });

    }
});

function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}
