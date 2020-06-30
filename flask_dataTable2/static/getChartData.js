d3.json("/get-data3")
  .then(function(data){
    window.chartData = data
  });