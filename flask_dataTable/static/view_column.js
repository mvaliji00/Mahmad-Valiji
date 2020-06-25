d3.json("/get-data2").then(
    function tabulate(data) {
//            dt = [
//                    { '0' : "2013-01-01", '1' : 45 },
//                    { '0' : "2013-02-01", '1' : 50 },
//                ]
            dt = d3.values(data)
//            var table = d3.select('#table_2').append('table')
//            var thead = table.append('thead')
//            var	tbody = table.append('tbody');
            var columns = d3.keys(data)
            //var columns = ['date','close']

            for (i = 0; i < 2; i++) {
                var table = d3.select('#table_2').append('table' + i.toString())
                var thead = table.append('thead')
                var	tbody = table.append('tbody');

                thead.append('tr')
                  .selectAll('th')
                  .data([columns[i]]).enter()
                  .append('th')
                  .text(d=>d);

                var rows = tbody.selectAll('tr')
                  .data([dt[i]])
                  .enter()
                  .append('tr')

                 var td = rows.selectAll("td")
                 .data(function(d, i) { return Object.values(d); })
                 .enter().append("td")
                   .text(function(d) { return d; });

//                var cells = rows.selectAll('td')
//                  .data(function (row) {
//                    return columns.map(function (column) {
//                      return {column: column, value: row[column]};
//                    });
//                  })
//                  .enter()
//                  .append('td')
//                   .text(function (d) { return d.value; })
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