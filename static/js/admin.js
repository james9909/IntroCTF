$('#add').click(function (e) {
    var problem_name = $("#problem_name").val();
    var problem_desc = $("#problem_desc").val();
    var problem_hint = $("#problem_hint").val();
    var problem_category = $("#problem_category").val();
    var problem_value = $("#problem_value").val();
    var problem_flag = $("#problem_flag").val();

    add(problem_name, problem_desc, problem_hint, problem_category, problem_value, problem_flag);
})

function add(problem_name, problem_desc, problem_hint, problem_category, problem_value, problem_flag) {
    $.post("/api/add_problem", {
        problem_name: problem_name,
        problem_desc: problem_desc,
        problem_hint: problem_hint,
        problem_category: problem_category,
        problem_value: problem_value,
        problem_flag: problem_flag
    }, function (data) {
        if (data == -1) {
            Materialize.toast("Database error. You should not be seeing this message :(", 2000);
        } else if (data == 1) {
            Materialize.toast("Successfully added problem", 2000);
        }
    });
}

function render_descriptions() {
    var desc = $('p[name=problem-desc]').map(function(){
                   return $.trim($(this).text());
                }).get();
    $("p[name=problem-desc]").each(function() {
        $(this).html(marked(desc[0]));
        desc = desc.splice(1, desc.length);
    });
}
