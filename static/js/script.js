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
		let height_el = element.height();
        let dx = 0-Math.floor(height_el*0.9)
         console.log(dx);
		$('#mn').css('margin-top',dx+'px')
	});


