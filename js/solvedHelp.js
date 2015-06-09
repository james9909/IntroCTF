//In progress - Joel
function validateSolve() {
    var cookies = document.cookie;
    var start = cookies.search("uid=");
    var end = cookies.slice(start).search(";");
    var uid = cookies.slice(start+4,end);
    var solved = []//Some way of getting users.txt, should be array of strings
    for (i = 0; i < solved.length; i++) {
        document.getElementbyId(solved[i]).class="collapsible-header green lighten-3";
    }
}