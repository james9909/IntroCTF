// Creds to the helpful guys over at stackoverflow
function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
    results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

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

function getTeamData(team) {
    data = [];
    scores = readFile("../accounts/scores.txt");
    scores = getTeamInfo(scores, team);
    scores = scores.slice(1);
    for (i = 0; i < scores.length; i+=2) {
        data.push([parseInt(scores[i+1], 10), parseInt(scores[i], 10)]);
    }
    return data;
}

var team = getParameterByName("team");
console.log(getTeamData(team));
$(document).ready(function () {
    $('#container').highcharts({
        chart: {
            renderTo: "graph"
        },
        title: {
            text: 'Team score progression',
            x: -20
        },
        xAxis: {
            type: "datetime",
            dateTimeLabelFormats: { 
                month: '%e. %b',
                year: '%b'
            }
        },
        yAxis: {
            title: {
                text: 'Points'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }],
            floor: 0
        },
        tooltip: {
            valueSuffix: 'points'
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            spline: {
                marker: {
                    enabled: true
                }
            }
        },
        series: [{
            pointStart: 1434312000000,
            pointInterval: 86400000,
            pointEnd: 1435017862000,
            name: team,
            data: getTeamData(team)
        }]
    });
})
