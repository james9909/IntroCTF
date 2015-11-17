$('#add').click(function (e) {
    var problem_name = $("#problem_name").val();
    var problem_desc = $("#problem_desc").val();
    var problem_hint = $("#problem_hint").val();
    var problem_category = $("#problem_category").val();
    var problem_value = $("#problem_value").val();

    add(problem_name, problem_desc, problem_hint, problem_category, problem_value);
})

function add(problem_name, problem_desc, problem_hint, problem_category, problem_value) {
    $.post("/api/add_problem", {
        problem_name: problem_name,
        problem_desc: problem_desc,
        problem_hint: problem_hint,
        problem_category: problem_category,
        problem_value: problem_value
    }, function (data) {
        if (data == -1) {
            Materialize.toast("Database error. You should not be seeing this message :(", 2000);
        } else if (data == 0) {
            Materialize.toast("Problem with that name already exists!", 2000);
        } else if (data == 1) {
            Materialize.toast("Successfully added problem", 2000);
        }
    });
}
