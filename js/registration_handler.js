$(function() {
    $("#registration-new-team").hide();
    $("#registration-join-team").hide();
    pageTransitionSpeed = 200;
    offset = 0;
    $("#button-new-team").click(function() {
        event.preventDefault();
        return $("#registration-join-team").hide("fast", function() {
            return $("#registration-new-team").slideDown(250, "linear")
        });
    });
    $("#button-join-team").click(function() {
        event.preventDefault();
        return $("#registration-new-team").hide("fast", function() {
            return $("#registration-join-team").slideDown(250, "linear")
        });
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
        data: $("#"+form, "#register-form").serialize(),
        success: function(response) {
            Materialize.toast(response, 4000);
            if (response.includes("+")) {
                setTimeout(function(){
                    location.reload();
                }, 3000);
            }

        }
    });
}
