$('.slider').slick({
    slidesToShow: 5
});

$(function () {
    $('#elem').on('click', function () {
        $('#front_').toggleClass('transform');
        $('#back_').toggleClass('transform');
    });
});

$(function () {
    $('#elem-1').on('click', function () {
        $('#front_').toggleClass('transform');
        $('#back_').toggleClass('transform');
    });
});

const screenHeight = window.screen.height
const height = document.documentElement.scrollTop

$(document).ready(function () {
    var element = $(".background");
    let height_el = element.height();
    let dx = 0 - Math.floor(height_el * 0.9)
    console.log(dx);
    $('#mn').css('margin-top', dx + 'px')
});

$(document).ready(function () {
    let element = $("#mn");
    let height_el = element.height();
    let back = $(".background").height();
    console.log(height_el);
    let dx;
    if ((height_el < back) && (height_el < 1920)) {
        dx = 0.9*(back - height_el);
    }
    $('#foot').css('margin-top', dx + 'px')
});

