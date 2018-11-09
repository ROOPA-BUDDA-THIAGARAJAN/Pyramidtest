$(document).ready(function(){

   // jQuery methods go here...
   $("#email").on('blur', function(){
        // check with DB here
        //alert("Test alert here");   

        $.ajax({
                data :{
                    email : $('#email').val()
                },
                type: "POST",
                url: "/checkregistration"
                
            }).done(function(data){
            	//alert("inside function here");  
            	//alert(data.error);
            	//alert("data.state is ");
            	//alert(data.state);
                if(data.error){
                	//alert("inside data error here");  
                    $('#failure_alert').text(data.error).show();
                    $('#success_alert').hide();
                }
                else if(data.state){
                	//alert("inside data state here");  
                    $('#success_alert').text(data.state).show();
                    $('#failure_alert').hide();
                }
        });
    });
   $("#rpword").on('blur', function(){
    pwd = $("#rpword").val()
    rpwd = $("#pword").val()
   	if(pwd != rpwd){      
   		alert("password mismatch")
   	}

   });

}); 


