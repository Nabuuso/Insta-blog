$(document).ready(function(){
    //REGISTER USER
    $("#registerBtn").click(function(e){
        e.preventDefault();
        let body = {
            full_name: $("#fullName").val(),
            email: $("#email").val(),
            password: $("#password").val(),
            username: $("#username").val(),
        }
        $.ajax({
            method:'POST',
            url:'register',
            data:body,
            success:function(response){
                if(response.status == 201){
                    alert(response.message)
                    $("#fullName").val("")
                    $("#email").val("")
                    $("#password").val("")
                    $("#username").val("")
                }else{
                    alert(response.message)
                }
            },
            error:function(response){
                alert(response.error)
            }
        })
    })
})