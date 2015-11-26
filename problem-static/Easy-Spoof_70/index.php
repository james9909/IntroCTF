<?php

$browser = $_SERVER["HTTP_USER_AGENT"];
if($browser == "Mozilla/5.0 (PLAYSTATION 3; 3.55)") {
    $user = $_POST["user"];
    if ($user == "admin") {
        if ($_COOKIE["auth"] == 1) {
            if ($_SERVER['HTTP_REFERER'] == "http://www.stuycs.org/" or $_SERVER['HTTP_REFERER'] == "http://www.stuycs.org" or $_SERVER['HTTP_REFERER'] == "www.stuycs.org") {
                echo "The flag is wasnt_that_easy";
            } else {
                echo "Wrong referer!";
            }
        } else {
            echo "Not authorized!";
        }
    } else {
        echo "Your user is not admin!";
    }
} else {
    echo "Wrong browser!";
}
