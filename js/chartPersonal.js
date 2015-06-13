//Syntax for graph making is (name,data,options,responsive-options)
function readFile(path) {
    var request = new XMLHttpRequest();
    request.open("GET", path, false);
    request.send(null);
    return request.responseText;
}
//Assume I have the file. Comma seperated tuples (problem,day - code MO TU WE TH FR SA SU).
var data = {};
function load(data){
    var out = [];
    var day = ["MO","TU","WE","TH","FR","SA","SU"];
    for(i=0;i<data.length;i++){
        out.push(0);
        out[day.indexOf(data[i][1])] += data[i][0];
    }
    
}

function toBullet(tuple){
    var out = "&bull; ";
    out += tuple[0].toString();
    out += ": ";
    out += points;
    out += " - ";
    out += tuple[1];
    return out;
}

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
        showLine:true,
        showPoint:true,
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
