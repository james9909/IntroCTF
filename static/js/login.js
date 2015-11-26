$('#login').click(function(e) {
    login($("#team_name").val(), $("#password").val());
});

function login(team, password) {
    $.post("/api/login", {
        team: team,
        password: password
    }, function(data) {
        if (data == -1) {
            Materialize.toast("Database error... Please contact an admin as soon as possible.", 2000);
        } else if (data == 0) {
            Materialize.toast("Invalid credentials", 2000);
        } else if (data == 1) {
            Materialize.toast("Successfully logged in", 2000);
            setTimeout(function() {
                window.location.href = "/";
            }, 2000);
        }
    });
}
