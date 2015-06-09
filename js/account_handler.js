$(function() {

    $('#register-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("register-form");
    })
    function submit_problem(formid) {
        $.ajax({
            url: "scripts/account_handler.py",
            type: "POST",
            data: $("form[id=" + formid + "]").serialize(),
            success: function(response) {
                Materialize.toast(response, 4000);
            }
        });

    }
});
