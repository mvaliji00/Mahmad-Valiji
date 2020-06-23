d3.json("/get-data").then(
    function tabulate(data) {
            data = [
                    { "date" : "2013-01-01", "close" : 45 },
                    { "date" : "2013-02-01", "close" : 50 },
                ]

//            var table = d3.select('#table_2').append('table')
//            var thead = table.append('thead')
//            var	tbody = table.append('tbody');
            var columns = ['date','close']
            //var columns = ['date','close']

            for (i = 0; i < 2; i++) {
                var col = ['date']
                var table = d3.select('#table_2').append('table' + i.toString())
                var thead = table.append('thead')
                var	tbody = table.append('tbody');

                thead.append('tr')
                  .selectAll('th')
                  .data([columns[i]]).enter()
                  .append('th')
                  .text(d=>d);

                var rows = tbody.selectAll('tr')
                  .data([data[i]])
                  .enter()
                  .append('tr')

                var cells = rows.selectAll('td')
                  .data(function (row) {
                    return columns.map(function (column) {
                      return {column: column, value: row[column]};
                    });
                  })
                  .enter()
                  .append('td')
                   .text(function (d) { return d.value; })
//
//                      .append('th')
//                        .text(function (column) { return column; });
  }


//            thead.append('tr')
//              .selectAll('th')
//              .data(columns).enter()
//              .append('th')
//              .attr("id", (column) => {return column})
//
//            // create a row for each object in the data
//            var rows = tbody.selectAll('tr')
//              .data(data)
//              .enter()
//              .append('tr')
//
//            // create a cell in each row for each column
//            var cells = rows.selectAll('td')
//              .data(function (row) {
//                return columns.map(function (column) {
//                  return {column: column, value: row[column]};
//                });
//              })
//              .enter()
//              .append('td')
//                .text(function (d) { return d.value; })
})