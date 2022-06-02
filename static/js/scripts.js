$('.slider').slick({
    slidesToShow: 5
});

$(function () {
    $('#elem').on('click', function () {
        $('#front_').toggleClass('transform');
        $('#back_').toggleClass('transform');
        clearInput();
    });
});

$(function () {
    $('#elem-1').on('click', function () {
        $('#front_').toggleClass('transform');
        $('#back_').toggleClass('transform');
        clearInput();
    });
});

const screenHeight = window.screen.height
const height = document.documentElement.scrollTop

$(document).ready(function () {
    var element = $(".background");
    let height_el = element.height();
    let dx = 0 - Math.floor(height_el * 0.9)
    $('#mn').css('margin-top', dx + 'px')
});

$(document).ready(function () {
    let element = $("#mn");
    let height_el = element.height();
    let back = $(".background").height();
    let dx;
    if ((height_el < back) && (height_el < 1920)) {
        dx = 0.9 * (back - height_el);
    }
    $('#foot').css('margin-top', dx + 'px')
});

function clearInput() {
    $('input[name = username]').val('').change();
    $('input[name = password]').val('').change();
    $('.message').text('');

    $('input[name = reg_username]').val('').change();
    $('input[name = reg_pass1]').val('').change();
    $('input[name = reg_pass2]').val('').change();
}

$(function ($) {
    $('#login_form').submit(function (e) {
        e.preventDefault()
        let url = this.action
        $.ajax({
            type: this.method,
            url: url,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                document.location.href = url + response.url
            },
            error: function (response) {
                $('.message').text(response.responseJSON.error)
            }
        })
    })
})

$(function ($) {
    $('#registration_form').submit(function (e) {
        e.preventDefault()
        let isValid;
        let Password = false;
        let url = this.action
        let Name = validName(this.reg_username.value)
        console.log(this.reg_username.value)
        if (Name) {
            Password = validPassword(this.reg_pass1.value, this.reg_pass2.value)
        }
        isValid = Password && Name;
        if (isValid) {
            $.ajax({
                type: this.method,
                url: this.action,
                data: $(this).serialize(),
                dataType: 'json',
                success: function (response) {
                    document.location.href = url + response.url
                },
                error: function (response) {
                    $('.message').text(response.responseJSON.error)
                }
            })
        }
    })
})


function validName(name) {
    if (name.length < 4) {
        $('.message').text("Имя пользователя должно быть больше 4-х символов")
        return false
    }

    if (name.match(/[;№$:'"#.,/\&^()!\\+=_|&?]+/)) {
        $('.message').text("Имя пользователя не может состоять из специальных символов")
        return false
    }
    return true
}

function validPassword(password1, password2) {
    if (password1 !== password2) {
        $('.message').text("Пароли не совпадают")
    }
    if (password1.length < 4) {
        $('.message').text("Пароль должен быть больше 4-х символов")
        return false
    }
    return true
}

