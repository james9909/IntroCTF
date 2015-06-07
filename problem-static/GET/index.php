<html>
<head>
<title>Login</title>
</head>
<body>
<!-- 
debug
username: admin
password: 123456
-->
We are currently under construction so a few features are missing. <br>
We will be up in a few years though, so don't worry <br>
<?php
$flag = "i_dont_get_it";
$user = $_GET["username"];
$pass = $_GET["password"];

if ($user == "admin" && $pass == "123456") {
    echo "Logged in! The flag is $flag";
}
?>

</body>
</html>
