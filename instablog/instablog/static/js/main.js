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
                console.log(response)
                console.log(JSON.stringify(response))
                if(response.status == 201){
                    $("#fullName").val("")
                    $("#email").val("")
                    $("#password").val("")
                    $("#username").val("")
                    alert(response.message)
                }else{
                    // alert(response.message)
                    alert(response.error)
                    // $("#register-alert").html(response.error)
                }
            },
            error:function(response){
                // $("#register-alert").html(JSON.stringify(response).error)
                alert(response.error)
            }
        })
    })
    //UPLOAD IMAGE
    $("#upload-img-btn").click(function(e){
        var data = new FormData()
        data.append("image",$("#imageFile")[0].files[0])
        data.append("image_name",$("#imageName").val())
        data.append("image_caption",$("#imageCaption").val())
        data.append("profile",$("#user").val())
        data.append("csrfmiddlewaretoken","{{ csrf_token }}")
        $.ajax({
            method:'POST',
            url:'blog-images',
            data:data,
            processData:false,
            contentType:false,
            mimeType:"multipart/form-data",
            success: function(response){
                location.reload()
            },
            error: function(response){
                alert(response.error)
            }
        })
    })
    //LIKES

    $(".likes-btn").click(function(e){
        let id = $(this).data("id");
        let data = {
            id:id
        }
        $.ajax({
            method:'POST',
            url:'likes',
            data:data,
            success:function(response){
                location.reload()
            },
            error:function(response){
                alert(response.error)
            }
        })
    })
    //COMMENT
    $(".comments-btn").click(function(e){
        e.preventDefault();
        let id = $(this).data("id");
        data = {
            image:id,
            comment:$("#comments-input-"+id).val(),
            profile:$("#profile-id").val()
        }
        $.ajax({
            method:'POST',
            url:'comments',
            data:data,
            success:function(response){
                location.reload()
            },
            error:function(response){
                location.reload()
            }
        })
    })
    $(".view-comments").click(function(e){
        e.preventDefault()
        $(".image-comments-section").css({"display":"none"})
        let id = $(this).data("id")
        $("#comment-section-"+id).css({"display":"flex"})
    })
    //FOLLOW USER
    $(".follow-btn").click(function(e){
        e.preventDefault()
        let follower = $(this).data("id")
        let profile = $("#profile-id").val()
        $.ajax({
            method:'POST',
            url:'follow',
            data :{
                profile:profile,
                follower:follower
            },
            success:function(response){
                location.reload()
            },
            error:function(response){
                location.reload()
            }
        })
    })
    //EDIT PROFILE
    $("#edit-profile").click(function(e){
        e.preventDefault()
        $.ajax({
            method:'POST',
            url:'edit-profile',
            data:{
                full_name:$("#editFullName").val(),
                email:$("#editEmail").val(),
                username:$("#editUsername").val(),
                bio:$("#editBio").val(),
                id:$("#userId").val()
            },
            success:function(response){
                alert("User updated successfully")
            }
        })
    })
})