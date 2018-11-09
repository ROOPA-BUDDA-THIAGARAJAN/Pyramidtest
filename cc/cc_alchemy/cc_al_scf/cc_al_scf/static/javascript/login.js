$(document).ready(function(){
	$("#submit").on('click', function(){
        // check with DB here
        alert("check email pwd if empty");  
        //email = $("#emailid").val(); 
        //alert(email);
        if ($("#emailid").val() != "") {
        	if ($("#password").val() != ""){
        		$.ajax({
	        		data:{
	        			email : $('#emailid').val(),
	        			pwd : $('#password').val()
	        		},
	        		type :"POST",
	        		url:"/login_auth"
	        	}).done(function(data){
	        		alert(data.state);
        		});
	     	}
	    }
	    alert("the fields cannot be empty")
	});
});
    
