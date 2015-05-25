$(function() {

    $('#post-form').on('submit', function(event){
        event.preventDefault();
        alert("d");
        submit_handle();
    })

    function submit_handle() {
        $.ajax({
            url: "scripts/problem_handler.py",
            type: "POST",
            d%ata: $("form[id=post-form]").serialize(),
            success: function(response) {
                alert(response);
            }
        });

    }
});
