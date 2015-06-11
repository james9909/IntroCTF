function makeChart()
    {new Chartist.Line('.ct-chart', {
  labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
  series: [
    [2, 3, 2, 4,4],
    [0, 2.5, 3, 2, 3],
    [1, 2, 2.5, 3.5, 4]
  ]
});}
