var $password = $("#password");
var $confirmPassword = $("#confirm_password");


//hide hints
$("form span").hide();

function passwordEvent(){
    if ($password.val().length > 8){
    $password.next().hide();
  }
  else
    $password.next().show();

}

function confirmPasswordEvent(){
  if($password.val()=== $confirmPassword.val()){
    $confirmPassword.next().hide();
  }
  else
    $confirmPassword.next().show();
}
//find out if password is valid
$password.focus(passwordEvent).keyup(passwordEvent)
         .focus(confirmPasswordEvent).keyup(confirmPasswordEvent);
  // hide hint if valid
  //else show hint

// when event happens on confirmation input
$confirmPassword.focus(confirmPasswordEvent).keyup(confirmPasswordEvent);