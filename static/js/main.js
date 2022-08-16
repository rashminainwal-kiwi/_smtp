$(document).ready(function(){
             $("#pageloader").hide();
			$( "#contactForm" ).validate( {
			submitHandler: function(form) {
			  update_user_basic_profile()
			  $( "#block" ).val('please wait ..');
            },
            rules: {
             host: {
              required: true,
             },
             email_to: {
              required: true,
              email:true,
              minlength:5,
            },
            email_from: {
              required: true,
              email:true,
              minlength:5,
            },
             username: {
                  required: true,
                  minlength:2
             },
             password: {
                  required: true,
             },
             port:{
                   required:true,
             },
             subject:{
                   required:true,
             },
             message:{
                   required:true,
             },
         },
        messages: {
        host: {
          required: "Please enter your name.",
        },
        username: {
          required: "Please enter your name.",
        },
        email_to: {
          required: "Please enter your  to email.",
          email: "Please provide a valid email."
        },
        email_from: {
          required: "Please enter your from email.",
          email: "Please provide a valid email.",
        },
        password: {
          required: "Please enter your password.",
        },
        port: {
          required: "Please enter the port."
        },
        subject: {
          required: "Please provide a subject."
        },
        message: {
          required: "Please provide a message."
        },
       },
	});

	function update_user_basic_profile(){
        var basic_profile_update_url = "sender"
        $.ajax({
            url: basic_profile_update_url,
            type : 'POST',
            data: {
             csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
             host: $('#host').val(),
             username: $('#username').val(),
             port: $("#port").val(),
             email_to: $("#email_to").val(),
             email_from: $("#email_from").val(),
             message: $("#message").val(),
             subject: $("#subject").val(),
             password: $("#password").val()
            },
            beforeSend : function(){
                 $('#block').prop('disabled', true);
                 $("#pageloader").fadeIn();
            },
            success: function (msg) {
                location.reload();
                $('#block').prop('disabled', false);

            },
            error: function(error) {

            }
        });
    }
});

