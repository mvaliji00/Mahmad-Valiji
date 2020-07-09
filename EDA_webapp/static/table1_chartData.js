function chartDataTable1() {
    d3.json("/get-table1-chartdata?source="+window.source)
      .then(function(data){
        window.chartData = data
      });
}

