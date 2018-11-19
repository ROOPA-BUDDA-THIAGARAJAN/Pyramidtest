$(document).ready(function(){
	$("#delete_user").on('click', function(){
        // check with DB here
        alert("delete button clickedd");     
        name = $("#delete_user").attr('name');
        alert(name);
        if (name != "") {        	
		$.ajax({
    		data:{
    			'email' : name
    		},
    		type :"POST",
    		url:"/del_user"
    	}).done(function(data){
    		// check success 
    		// if - to refresh the page
    		location.reload();
    		//alert(data);
    		/*
    		if (data == 'success'){
    			// code to refreshes the page goes here
    			location.reload();
    		}*/
		});
	    }
	});
});
    
