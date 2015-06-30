$(document).ready(function(){


//右上角收起按钮


    $( ".box" )
        .find( ".box-title" )
            .prepend( "<i class='icon icon-chevron-up chevron'></i>")
            .end()
        .find( ".box-content" );

    $( ".box-title .icon.chevron" ).click(function() {
        $( this ).toggleClass( "icon-chevron-up" ).toggleClass( "icon-chevron-down" );
        $( this ).parents( ".box:first" ).find( ".box-content" ).toggle('fast');
    });
    
    $( ".column" ).disableSelection();




});


