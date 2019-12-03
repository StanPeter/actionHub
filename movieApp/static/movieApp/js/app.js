//change movie-item brightness on hover
function main() {
    $('.movie-item').hover(function() {
        $(this).find('.movie-image').css({"filter": "brightness(20%)"});
        $(this).find('.movie-star').toggleClass('hide');
        $(this).find('.movie-rating').toggleClass('hide');
        $(this).find('.movie-expander').toggleClass('hide');
        $(this).find('.movie-delete-button').toggleClass('hide');
    }, function() {
        $(this).find('.movie-image').css({"filter": "brightness(100%)"});
        $(this).find('.movie-star').toggleClass('hide');
        $(this).find('.movie-rating').toggleClass('hide');
        $(this).find('.movie-expander').toggleClass('hide');
        $(this).find('.movie-delete-button').toggleClass('hide');
    });
}

$(document).ready(main());

