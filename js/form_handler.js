$(function() {

    $('#intro-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("intro-form");
    })
    $('#caesar-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("caesar-form");
    })
    $('#base-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("base-form");
    })
    $('#absent-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("absent-form");
    })
    $('#brutus-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("brutus-form");
    })
    $('#bb-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("bb-form");
    })
    $('#stego-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("stego-form");
    })
    $('#dot-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("dot-form");
    })
    $('#corrupt-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("corrupt-form");
    })
    $('#inverted-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("inverted-form");
    })
    $('#rawr-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("rawr-form");
    })
    $('#messy-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("messy-form");
    })
    $('#inspect-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("inspect-form");
    })
    $('#cookie-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("cookie-form");
    })
    $('#hidden-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("hidden-form");
    })
    $('#get-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("get-form");
    })
    $('#spoof-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("spoof-form");
    })
    $('#donttrip-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("donttrip-form");
    })
    $('#indif-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("indif-form");
    })
    $('#fast-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("fast-form");
    })
    $('#triangle-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("triangle-form");
    })
    $('#overflow-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("overflow-form");
    })
    $('#eval-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("eval-form");
    })
    $('#easy-rev-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("easy-rev-form");
    })
    $('#rand-eval-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("rand-eval-form");
    })
    $('#election-form').on('submit', function(event){
        event.preventDefault();
        submit_problem("election-form");
    })
    function submit_problem(formid) {
        $.ajax({
            url: "scripts/problem_handler.py",
            type: "POST",
            data: $("form[id=" + formid + "]").serialize(),
            success: function(response) {
                Materialize.toast(response, 4000);
            }
        });

    }
});
