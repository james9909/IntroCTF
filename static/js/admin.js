$('#add').click(function (e) {
    var problem_name = $("#problem_name").val();
    var problem_desc = $("#problem_desc").val();
    var problem_hint = $("#problem_hint").val();
    var problem_category = $("#problem_category").val();
    var problem_value = $("#problem_value").val();
    var problem_flag = $("#problem_flag").val();

    add(problem_name, problem_desc, problem_hint, problem_category, problem_value, problem_flag);
});

$("[name='preview']").click(function (e) {
    var problem = $(this).parents("form:first");
    var name = $("input[name=problem_name]", problem).val();
    var desc = $("textarea[name=problem_desc]", problem).val();
    var hint = $("input[name=problem_hint]", problem).val();
    var flag = $("input[name=problem_flag]", problem).val();
    $("#preview-name").text(name);
    $("#preview-desc").html(marked(desc));
    document.getElementById("preview-hint").onclick = function() {
        Materialize.toast(hint, 4000);
    }
    document.getElementById("preview-submit").onclick = function() {
        var candidate = $("input[name=flag]").val();
        if (candidate == flag) {
            Materialize.toast("Correct!", 2000);
        } else {
            Materialize.toast("Incorrect", 2000);
        }
    }
});

$("[name='delete-modal']").click(function (e) {
    var form = $(this).parents("form:first");
    var pid = $("input[name=pid]", form).val();
    $("[name='delete']").click(function (e) {
        remove_problem(pid);
    });
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

function remove_problem(pid) {
    $.post("/api/remove_problem", {
        pid: pid
    }, function (data) {
        if (data == -1) {
            Materialize.toast("Database error. You should not be seeing this message :(", 2000);
        } else if (data == 0) {
            Materialize.toast("Problem does not exist", 2000);
        } else if (data == 1) {
            Materialize.toast("Successfully removed problem", 2000);
        }
    });
}
