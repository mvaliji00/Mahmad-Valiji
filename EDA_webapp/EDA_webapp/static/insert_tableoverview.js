function insertOverviewTable() {
    d3.json("/get-overviewtable-data?source="+window.source).then(
    function tabulate(data) {
        var table = d3.select('#table_overview').append('table_overview')
        var thead = table.append('thead')
        var	tbody = table.append('tbody');
        var columns = Object.keys(d3.values(data)[0])
        //var columns = ['description','warning']

        // append the header row
        thead.append('tr')
          .selectAll('th')
          .data(columns).enter()
          .append('th')
          .text(function (column,i) {
            return column;
          })

        // create a row for each object in the data
        var rows = tbody.selectAll('tr')
          .data(d3.values(data))
          .enter()
          .append('tr')

        // create a cell in each row for each column
        var cells = rows.selectAll('td')
          .data(function (row) {
            return columns.map(function (column) {
              return {column: column, value: row[column]};
            });
          })
          .enter()
          .append('td')

        warning_type = ['High Cardinality','Correlation','Missing','Skewness','Unique Values','Zeros']
        class_list = ["btn btn-primary","btn btn-info","btn btn-warning","btn btn-info","btn btn-primary","btn btn-warning"]

        cells.append('a')
          .text(function (d,i) {
              if (i==0){
                var words = d.value
                var firstWord = words.replace(/ .*/, '');
                return firstWord
              }
              else {
                return d.value
              }
          })
          .attr("class", (d,i) => {
            if (i==0){
                return "anchor"
            }
            else {
                var index =  warning_type.findIndex(rank => rank === d.value)
                return class_list[index] + ' disabled'
            }
          });

//          .attr('aria-disabled', (d,i) => {
//            if (i!=0){
//                return "true"
//            }
//            });


        rows.select('td')
          .attr('width',(d,i) => {
            if (i==0) {
                return "85%"
            }
          })
          .append('a')
          .text(function (d,i) {
            //if (i==0) {
                var words = d.Desc
                string = words.split(' ')
                string.shift()
                return ' ' + string.join(' ')
            //}
          });
    })
}

