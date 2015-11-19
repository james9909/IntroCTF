$("[name='submit']").click(function (e) {
    e.preventDefault();
    var form = $(this).parents('form:first');
    var flag = $("input[name='flag']", form).val();
    var pid = $("input[name='pid']", form).val();
    if (flag == "") {
        Materialize.toast("Flag cannot be empty!", 2000);
        return;
    }
    submit_flag(pid, flag);
})

function submit_flag(pid, flag) {
    $.post("/api/submit_flag", {
        pid: pid,
        flag: flag
    }, function (data) {
        if (data == 1) {
            Materialize.toast("Correct!", 2000);
        } else if (data == 0) {
            Materialize.toast("Incorrect", 2000);
        } else if (data == -1) {
            Materialize.toast("You already solved this problem!", 2000)
        }
    });
}
