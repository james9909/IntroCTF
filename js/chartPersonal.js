function makeChart()
    {console.log("Hello")
        new Chartist.Line('.ct-chart', {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
            {name:"series-1",
            data:[2, 3, 2, 4,4]}
            ]
        },
        {
            series:{
                'series-1': {
                    lineSmooth: Chartist.Interpolation.step({postpone:false}),
                    showArea:true
                },
        }}
  
  );}
