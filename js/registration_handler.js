$(function() {
    pageTransitionSpeed = 200;
    offset = 0;
    $("#submit-registration").click(function() {
        event.preventDefault();
        submitRegistration();
    });
});

function submitRegistration() {
    var newTeam = $("#registration-new-team").is(":visible");
    if (newTeam) {
        var form_handler = "create_team.py";
        var form = "new-team";
    } else {
        var form_handler = "join_team.py";
        var form = "existing-team";
    }
    $.ajax({
        url: "scripts/"+form_handler,
        type: "POST",
        data: $("#"+form + ", #register-form").serialize(),
        success: function(response) {
            Materialize.toast(response, 4000);
            if (response.includes("Success")) {
                setTimeout(function(){
                    location.reload();
                }, 3000);
            }

        }
    });
}
