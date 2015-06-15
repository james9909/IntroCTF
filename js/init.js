$( document ).ready(function() {
    $('.button-collapse').sideNav();
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
    $('.scrollspy').scrollSpy();

    if ($('nav').length) {
        $('.toc-wrapper').pushpin({ top: $('nav').height() });
    }
    $('.modal-trigger').leanModal({
        dismissible: true, // Modal can be dismissed by clicking outside of the modal
        opacity: .5, // Opacity of modal background
        in_duration: 300, // Transition in duration
        out_duration: 200, // Transition out duration

    }
    );

    $('ul.tabs').tabs();
});
