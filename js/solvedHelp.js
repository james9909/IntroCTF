function readFile(path) {
    var request = new XMLHttpRequest();
    request.open("GET", path, false);
    request.send(null);
    return request.responseText;
}

function getTeamInfo(data, team) {

    data = data.split("\n");
    for (i = 0; i < data.length; i++) {
        temp = data[i].split("||&&||");
        if (temp[0] === team) {
            return temp;
        }
    }
}

// Creds to stack overflow
Array.prototype.diff = function(a) {
    return this.filter(function(i) {return a.indexOf(i) < 0;});
};

function validateSolve() {
    var allproblems = ["intro", "caesar", "base", "absent", "brutus", "bb", "stego", "dot", "corrupt", "inverted", "rawr", "messy", "inspect", "cookie", "hidden", "get", "spoof", "donttrip", "indif", "fast", "triangle", "overflow", "eval", "copy", "easy-rev", "rand-eval", "election", "sets"]
    var cookies = document.cookie;
    var start = cookies.search("tid=");
    var uid = cookies.slice(start+4);
    var text = readFile("accounts/teams.txt");
    var info = getTeamInfo(text, uid);
    var solved = info.slice(2); // Get only solved problems, ignore username and pass
    // Loop through all solved problems
    for (i = 0; i < solved.length; i++) {
        document.getElementById(solved[i]).className = "collapsible-header green lighten-5";
        document.getElementById(solved[i]).innerHTML += "<span style='float: right'>Solved</span>"
    }
    var unsolved = allproblems.diff(solved);
    // Loop through all unsolved problems
    for (i = 0; i < unsolved.length; i++) {
        document.getElementById(unsolved[i]).innerHTML += "<span style='float: right'>Unsolved</span>"
    }
}
