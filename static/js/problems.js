$("[name='submit']").click(function(e) {
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
    }, function(data) {
        Materialize.toast(data.message, 2000);
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

$(document).ready(function() {
    render_descriptions();
});
