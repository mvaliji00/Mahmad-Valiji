d3.json("/get-data2").then(
    function tabulate(data) {
            var columns = d3.keys(data)
            for (i = 0; i < columns.length; i++) {
                data_json = [
                        { '0' : "", '1' : "missing",'2' : data[columns[i]]["missing"],'3' : "val"+"%"},
                        { '0' : data[columns[i]]["unique"], '1' : "unique",'2' : data[columns[i]]["unique"],'3' : "val"+"%" },
                        { '0' : "unique values", '1' : "valid",'2' : data[columns[i]]["valid"],'3' : "val"+"%"},
                        { '0' : "", '1' : "value",'2' : data[columns[i]]["value"],'3' : "val"+"%"},
                    ]

                var table = d3.select('#table_2').append('table' + i.toString()).attr("class", "details_table")
                var thead = table.append('thead')
                var	tbody = table.append('tbody');

                thead.append('tr')
                  .selectAll('th')
                  .data([columns[i]]).enter()
                  .append('th')
                  .text(d=>d);

                thead.append('tr')
                    .selectAll('th')
                    .data(['',columns[i]]).enter()
                    .append('th')
                    .attr("id", function(d){
                        if (d != "") {return "table2_" +columns[i]}
                    })
                    .attr("colspan", function(d){
                        if (d === columns[i]) {return 3}
                    });
//                    .attr("id", function(d){
//                        if (d === columns[i]) {bar(columns[i])}
//                    })

                var rows = tbody.selectAll('tr')
                  .data(data_json)
                  .enter()
                  .append('tr')
                  .attr("id", (d,k)=>"row" + k);

                var cells = rows.selectAll("td")
                 .data(function(d, i) { return Object.values(d); })
                 .enter().append("td")
                 .text(function(d, k) {
                    return d;
                 })
                 .attr("id", (d,k)=>"cell"+k);

                //call bar plot
                bar('#table2_' + columns[i],data[columns[i]]["valid"],data[columns[i]]["missing"]);

                //bar(columns[i],data[columns[i]]["valid"],data[columns[i]]["missing"]);


                //d3.selectAll("#cell0")
//                .attr("rowspan", function(d){
//                    if (d != "") {return 2}
//                });
                //.attr("id", 2)




            }
    }
)