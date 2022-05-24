$('.slider').slick({
    slidesToShow: 5
});

$(function(){
	$('#elem').on('click', function(){
  	$('#front_').toggleClass('transform');
    $('#back_').toggleClass('transform');
  });
});

$(function(){
	$('#elem-1').on('click', function(){
  	$('#front_').toggleClass('transform');
    $('#back_').toggleClass('transform');
  });
});

const screenHeight = window.screen.height
const height = document.documentElement.scrollTop

// $(window).scroll(function(){
//         if (height >= screenHeight) {
//             $('.background').style.overflow = 'hidden';
//         }
//         else {
//             $('.background').removeClass('fixed');
//         }
//     });


	$(document).ready(function() {

		var element = $(".background");
		var height_el = element.height();
        console.log(height_el);
		$(".fixed_block_position").css({
			"width": element.outerWidth(),
			"height": element.outerHeight()
		});

		$(window).scroll(function() {

			if($(window).scrollTop() > height_el) {

				element.addClass("fixed");

			} else {

				element.removeClass("fixed");

			}

		});

	});

