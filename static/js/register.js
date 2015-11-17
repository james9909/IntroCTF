$('#register').click(function (e) {
    register($("#team_name").val(), $("#password").val(), $("#password2").val());
});

function register(team, password, password2) {
    if (password != password2) {
        Materialize.toast("Passwords do not match.");
        return;
    }
    $.post("/api/register", {
        team: team,
        password: password
    }, function (data) {
        if (data == -1) {
            Materialize.toast("Database error... Please contact an admin as soon as possible", 2000);
        } else if (data == 0) {
            Materialize.toast("Team name already in use", 2000);
        } else if (data == 1) {
            Materialize.toast("Success!", 2000);
        } else if (data == 2) {
            Materialize.toast("Invalid password", 2000);
        }
    });
}
