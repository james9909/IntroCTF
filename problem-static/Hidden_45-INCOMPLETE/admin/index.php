<html>
<head>
<title>Forms</title>
</head>
<body>

<?php
$flag = "hidden_input_too_easy";
$auth = $_POST["auth"];
$user = $_POST["user"];
$pass = $_POST["pass"];

if ($user == "admin" && $pass == "abc123") {
    if ($auth == 1) {
        echo "Congratulations! The flag is $flag";
    } else {
        echo "Logged in!"
    }
} else {
    echo "Bad login!"
}
?>

<form action="" method="post">
    PIN:<br>
    <input type="text" name="user" value="">
    <input type="password" name="PIN" value="">
    <input type="hidden" name="auth" value=0>
    <button type="submit">Enter</button>
</form>
</body>
</html>
