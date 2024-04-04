// script that fetches and prints how to say “Hello” depending on the lang.

$(document).ready(function(){
    function translate() {
        const lang = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/', { lang: lang }, function(data){
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translate);
    $('#language_code').keypress(function(e){
        if(e.which == 13) { // 13 is the ENTER key code
            translate();
        }
    });
});
