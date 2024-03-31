
function valid(){
    var email=document.myform.email.value;
    var pwd =document.myform.password.value;
    console.log('email value : ',email);
    console.log('pwd value : ',pwd);
    if(email==""||email==null){
        console.log('email empty');
        var emailErrorField = document.getElementById("e");
        emailErrorField.innerHTML="Email can't be empty";
        emailErrorField.style.display="block";
    }
    else if (email!=""||email!=null){
        console.log(`Email present`);
        document.getElementById("e").style.display="none";
    }
    if(pwd.length<6||pwd==""){
        var pwdErrorField = document.getElementById("pwd");
        console.log('Pwd empty');
        pwdErrorField.innerHTML="Enter password greater than 6 elements";
        pwdErrorField.style.display="block"; 
    }
    else if (pwd.length>=6){
        console.log('pwd present');
        document.getElementById("pwd").style.display="none";
    }
 

}
