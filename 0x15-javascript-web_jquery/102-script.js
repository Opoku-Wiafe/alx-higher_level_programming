// script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function(){
    $('#btn_translate').click(function(){
        const lang = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/', { lang: lang }, function(data){
            $('#hello').text(data.hello);
        });
    });
});// script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function(){
    $('#btn_translate').click(function(){
        const lang = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/', { lang: lang }, function(data){
            $('#hello').text(data.hello);
        });
    });
});
