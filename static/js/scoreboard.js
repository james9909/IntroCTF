function graph() {
    $.post("/api/top/5", {
        scoreboard: true
    }, function(data) {
        var series = [];
        teams = $.parseJSON(JSON.stringify(data));
        teams = teams["data"]["scoreboard"];
        for (var i = 0; i < teams.length; i++) {
            var team = {};
            var data = [];
            team["name"] = teams[i]["name"];
            var progression = teams[i]["progression"].split(",");
            for (var j = 0; j < progression.length; j+=2) {
                data.push([parseFloat(progression[j+1]), parseInt(progression[j])]);
            }
            team["data"] = data.sort();
            series.push(team);
        }
        // Graph
        $("#graph").highcharts({
            chart: {
                renderTo: "graph",
                zoomType: 'x'
            },
            title: {
                text: "Team progression",
                x: -20
            },
            xAxis: {
                type: "datetime",
                dateTimeLabelFormats: {
                    month: "%e. %b",
                    year: "%b"
                }
            },
            yAxis: {
                title: {
                    text: "Points"
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: "#808080"
                }],

                min: 0
            },
            tooltip: {
                valueSuffix: " points"
            },
            series: series
        }, function (chart) {
		if (chart.series[0].dataMax <= 0) chart.yAxis[0].update({
			max: 1
        })});
    });
}

graph();
