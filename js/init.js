$( document ).ready(function() {
    $('.button-collapse').sideNav();
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
    $('.scrollspy').scrollSpy();

    if ($('nav').length) {
        $('.toc-wrapper').pushpin({ top: $('nav').height() });
    }
});
