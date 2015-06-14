function readFile(path) {
    var request = new XMLHttpRequest();
    request.open("GET", path, false);
    request.send(null);
    return request.responseText;
}

d = new Date();
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
            dateTimeLabelFormats: { // don't display the dummy year
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
        //minTickInterval: 86400000,
        //min: 1434312000000,
        series: [{
            pointStart: 1434312000000,
            pointInterval: 86400000,
            name: 'foo',
            data: [
                [1434312000000, 0 ],
                [1434322800000, 10], 
                [1434320320603, 25],
                [1434320329545, 55],
                [1434320329545, 95],
                [d.getTime(), 200]
            
            ]
        }]
    });
})

