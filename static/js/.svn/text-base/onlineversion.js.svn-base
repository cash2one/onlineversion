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


function delete_productset(odj){

    //alert(odj.name);
    var productSetId = odj.name;
    var pathname = window.location.pathname;
    //alert(pathname);

    jQuery.ajax({
                type:"post",
                datatype:"json",
                url:"/delete_productSet/",
                data:{'productSetId':productSetId},
                error:function(ex){alert(ex.status);},
                success:function(data){                

                    window.location.href=pathname;     
                }

            });
}


function dismiss_save(){
    var pathname = window.location.pathname;
    href = pathname.split("/")[1];
    window.location.href="/"+href;
}

function delete_product(odj){
    //alert("123");
    var form_name = odj.id
    //document.form_name.submit();
    //alert(form_name);
    document.getElementById(form_name).submit();

    
    
}

function save_product(){
    var productName=""
    productName = $("#id_name").val();
    if (productName=="")
        alert("请输入产品名称！");
    else
        //alert(document.product_add_save);
        document.product_add_save.submit();


    
}


