$(function () {
    function render_time() {
        return moment($(this).data('timestamp')).format('lll')
    }
    $('[data-toggle="tooltip"]').tooltip(
        {title: render_time}
    );
});

$.ajax({
                url:'/login',
                type:'post',
                data:{
                    user:$('#user').val(),
                    password:$('#password').val(),
                },
                beforeSend:function(){
                    $.messager.progress({
                        text:'正在登陆准备中......',
                    });
                },
                success:function(data,response,status){
                    $.messager.progress('close');
                    if (data>0){
                        location.href='/templates/index.html';
                    }else{
                        $.messager.alert('登陆失败！','用户名或密码错误！','warning',function(){
                            $('#password').select();
                        });
                    }
                }
            });
