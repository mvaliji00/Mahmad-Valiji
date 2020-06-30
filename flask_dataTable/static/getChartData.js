//window.addEventListener("load", function(event) {
//
//  console.log('page is fully loaded');

function chart(id) {
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Mushrooms', 3],
          ['Onions', 1]
        ]);

        // Set chart options
        var options = {'title':'How Much Pizza I Ate Last Night',
                       'width':400,
                       'height':300};

        var chart = new google.visualization.PieChart(document.getElementById(id));
        chart.draw(data, options);
      }

}

//});
