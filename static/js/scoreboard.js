function graph() {
    $.post("/api/export_data", {
        scoreboard: true
    }, function(data) {
        var series = [];
        teams = $.parseJSON(JSON.stringify(data));
        teams = teams["data"]["scoreboard"].splice(0, 5); // Only top 5
        for (var i = 0; i < teams.length; i++) {
            var team = {};
            var data = [];
            team["name"] = teams[i]["name"];
            var progression = teams[i]["progression"].split(",");
            for (var j = 0; j < progression.length; j+=2) {
                data.push([parseFloat(progression[j+1]), parseInt(progression[j])]);
            }
            team["data"] = data;
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
                floor: 0
            },
            tooltip: {
                valueSuffix: " points"
            },
            series: series
        });
    });
}

graph();
