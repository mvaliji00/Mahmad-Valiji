//window.addEventListener("load", function(event) {
//
//  console.log('page is fully loaded');

function hbar_stacked() {
//      google.charts.load('current', {'packages':['corechart']});
//      google.charts.setOnLoadCallback(drawChart);
//
//      function drawChart() {
//        var data = new google.visualization.DataTable();
//        data.addColumn('string', 'Topping');
//        data.addColumn('number', 'Slices');
//        data.addRows([
//          ['Mushrooms', 3],
//          ['Onions', 1]
//        ]);
//
//        // Set chart options
//        var options = {'title':'How Much Pizza I Ate Last Night',
//                       'width':400,
//                       'height':300};
//
//        var chart = new google.visualization.PieChart(document.getElementById(id));
//        chart.draw(data, options);
//      }

      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawVisualization);
      // Create and populate the data table.

        function drawVisualization() {
          // Create and populate the data table.
          var data = google.visualization.arrayToDataTable([
            ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
             'Western', 'Literature', { role: 'annotation' } ],
            ['2010', 10, 24, 20, 32, 18, 5, ''],
          ]);

          // Create and draw the visualization.
          new google.visualization.BarChart(document.getElementById('Id')).
              draw(data,
                           {
                    width: 600,
                    height: 400,
                    legend: {position: 'none'},
                    bar: { groupWidth: '100%' },
                    vAxis: {
                      gridlines: {
                        count: 0
                      }
                    },
                    isStacked: true
                  }
              );
        }

//      function drawVisualization() {
//          var data = google.visualization.arrayToDataTable([
//            ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
//             'Western', 'Literature', { role: 'annotation' } ],
//            ['2010', 10, 24, 20, 32, 18, 5, ''],
//          ]);
//
//          var options = {
//            width: 600,
//            height: 400,
//            legend: { position: 'top', maxLines: 3 },
//            bar: { groupWidth: '75%' },
//            isStacked: true
//          };
//      }
//      // Create and draw the visualization.
//      var chart = new google.visualization.ColumnChart(document.getElementById('Id'));
//      chart.draw(data,options);
}


//});
