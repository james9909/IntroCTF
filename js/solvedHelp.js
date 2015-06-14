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
    var allproblems = ["intro", "caesar", "base", "absent", "brutus", "bb", "stego", "dot", "corrupt", "inverted", "rawr", "messy", "inspect", "cookie", "hidden", "get", "spoof", "donttrip", "indif", "fast", "triangle", "overflow", "eval", "copy", "easy-rev", "rand-eval", "election", "sets"];
    var solved = [];
    var cookies = document.cookie;
    var tid = cookies.split("; ");
    tid = tid[1].slice(4);
    console.log(tid);
    var text = readFile("accounts/solved.txt");
    var info = getTeamInfo(text, tid);
    info = info.slice(1);
    for (i = 0; i < info.length; i += 2) {
        solved.push(info[i]);

    }
    for (i = 0; i < solved.length; i++) {
        document.getElementById(solved[i]).className = "collapsible-header green lighten-5";
        document.getElementById(solved[i]).innerHTML += "<span style='float: right'>Solved</span>";
    }
    var unsolved = allproblems.diff(solved);
    for (i = 0; i < unsolved.length; i++) {
        document.getElementById(unsolved[i]).innerHTML += "<span style='float: right'>Unsolved</span>";
    }
}
