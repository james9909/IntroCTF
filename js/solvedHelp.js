//In progress - Joel
function readFile(path) {
    var request = new XMLHttpRequest();
    request.open("GET", path, false);
    request.send(null);
    return request.responseText;
}
function validateSolve() {
    var cookies = document.cookie;
    var start = cookies.search("uid=");
    var uid = cookies.slice(start+4);
    var text = readFile("accounts/users.txt");
    pos = text.search(uid); // Find our username
    text = text.slice(pos).trim(); // Trim off trailing whitespace
    var solved = text.split(",").slice(2); // Get only solved problems, ignore username and pass
    // Loop through all solved problems
    for (i = 0; i < solved.length; i++) {
        document.getElementById(solved[i]).className="collapsible-header green lighten-5";
    }
}
