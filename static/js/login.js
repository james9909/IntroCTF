$('#login-form').on("submit", function(e) {
    e.preventDefault();
    $("#login").addClass("disabled").attr("disabled", true);
    login($("#team_name").val(), $("#password").val());
});

function login(team, password) {
    $.post("/api/login", {
        team: team,
        password: password
    }, function(data) {
        Materialize.toast(data.message, 2000);
        if (data.success == 1) {
            setTimeout(function() {
                $("#login").removeClass("disabled").removeAttr("disabled");
            }, 2000)
        }
    });
}
