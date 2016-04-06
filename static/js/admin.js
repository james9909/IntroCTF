$('#add-form').on("submit", function(e) {
    e.preventDefault();
    var problem_name = $("input[name=problem_name]").val();
    var problem_desc = $("textarea[name=problem_desc]").val();
    var problem_hint = $("input[name=problem_hint]").val();
    var problem_category = $("input[name=problem_category]").val();
    var problem_value = $("input[name=problem_value]").val();
    var problem_flag = $("input[name=problem_flag]").val();

    $("#add").addClass("disabled").attr("disabled", true);
    add(problem_name, problem_desc, problem_hint, problem_category, problem_value, problem_flag);
});

$("[name='preview']").click(function(e) {
    var problem = $(this).parents("form:first");
    var name = $("input[name=problem_name]", problem).val();
    var desc = $("textarea[name=problem_desc]", problem).val();
    var hint = $("input[name=problem_hint]", problem).val();
    $("#preview-name").text(name);
    $("#preview-desc").html(marked(desc));
    document.getElementById("preview-hint").onclick = function() {
        Materialize.toast(hint, 4000);
    }
});

$("[name=update]").click(function(e) {
    var problem = $(this).parents("form:first");
    var pid = $("input[name=pid]", problem).val();
    var name = $("input[name=problem_name]", problem).val();
    var desc = $("textarea[name=problem_desc]", problem).val();
    var hint = $("input[name=problem_hint]", problem).val();
    var category = $("input[name=problem_category]", problem).val();
    var points = $("input[name=problem_value]", problem).val();
    var flag = $("input[name=problem_flag]", problem).val();
    update_problem(pid, name, desc, hint, category, points, flag);
});

$("[name='delete-modal']").click(function(e) {
    var form = $(this).parents("form:first");
    var div =$(this).closest("li");
    var pid = $("input[name=pid]", form).val();
    $("#delete").off().click(function(e) {
        remove_problem(pid);
        $("#delete-modal").closeModal();
        div.slideUp("normal", function() { $(this).remove(); } );
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
    }, function(data) {
        Materialize.toast(data.message, 2000);
        setTimeout(function() {
            $("#add").removeClass("disabled").removeAttr("disabled");
        }, 2000)
    });
}

function remove_problem(pid) {
    $.post("/api/remove_problem", {
        pid: pid
    }, function(data) {
        Materialize.toast(data.message, 2000);
    });
}

function update_problem(pid, name, description, hint, category, points, flag) {
    $.post("/api/update_problem", {
        pid: pid,
        name: name,
        description: description,
        hint: hint,
        category: category,
        points: points,
        flag: flag
    }, function(data) {
        Materialize.toast(data.message, 2000);
    });
}
