$(function() {
    $("#registration-new-team").hide();
    $("#registration-join-team").hide();
    pageTransitionSpeed = 200;
    offset = 0;
    $("#button-new-team").click(function() {
        return $("#registration-join-team").hide("slow", function() {
            return $("#registration-new-team").slideDown(250, "linear")
        });
    });
    $("#button-join-team").click(function() {
        return $("#registration-new-team").hide("slow", function() {
            return $("#registration-join-team").slideDown(250, "linear")
        });
    });
});
