$(function(){
    //REGISTER USER
    $("#registerBtn").click(function(e){
        e.preventDefault()
        let body = {
            full_name:$("#fullName").val(),
            email:$("#email").val(),
            password:$("#password").val(),
            username:$("#username").val(),
        }
        console.log(body)
        $.ajax({
            method:'POST',
            url:'register',
            data:body,
            success:function(response){
                console.log(response)
                console.log(body)
            }
        })
        alert("Hello")
    })
})