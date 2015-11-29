$('#register-form').on("submit", function(e) {
    e.preventDefault();
    $("#register").addClass("disabled").attr("disabled", true);
    var team_name = $("#team_name").val();
    var password = $("#password").val();
    var password2 = $("#password2").val();
    register(team_name, password, password2);
});

function register(team, password, password2) {
    $.post("/api/register", {
        team: team,
        password: password,
        password2: password2
    }, function(data) {
        Materialize.toast(data.message, 2000);
        setTimeout(function() {
            $("#register").removeClass("disabled").removeAttr("disabled");
        }, 2000)
    });
}
