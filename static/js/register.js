$('#register').click(function(e) {
    var team_name = $("#team_name").val();
    var password = $("#password").val();
    var password2 = $("#password2").val();
    if (password != password2) {
        Materialize.toast("Passwords do not match.");
        return;
    }
    if (password.length < 4) {
        Materialize.toast("Passwords should be at least 4 characters long", 2000);
        return;
    }
    register(team_name, password);
});

function register(team, password) {
    $.post("/api/register", {
        team: team,
        password: password
    }, function(data) {
        if (data == -1) {
            Materialize.toast("Database error... Please contact an admin as soon as possible", 2000);
        } else if (data == 0) {
            Materialize.toast("Team name already in use", 2000);
        } else if (data == 1) {
            Materialize.toast("Success!", 2000);
        }
    });
}
