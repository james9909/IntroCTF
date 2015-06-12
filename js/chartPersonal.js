//Syntax for graph making is (name,data,options,responsive-options)
function readFile(path) {
    var request = new XMLHttpRequest();
    request.open("GET", path, false);
    request.send(null);
    return request.responseText;
}
//Assume I have the file.

function makeChart()
    {var graphOptions = {
        low: 0,
        high:10,
        axisX:{
            
        },
        axisY:{
            onlyInteger:true,//change to 10
        },
        series:{
            'series-1': {
                lineSmooth: Chartist.Interpolation.step({postpone:false}),
                showArea:true
            },
        },
        //showLine:false,
        showPoint:false,
        fullWidth:true,
        };
    new Chartist.Line('.ct-chart', {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat','Sun'],
        series: [
            {name:"series-1",
            data:[0, 1, 1, 2,4,6,7]}
            ]
        },
        graphOptions
  
  );}
