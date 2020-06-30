function chartd3 (id) {
    var data = window.chartData[id]

    var sliceNumber = Object.values(data).findIndex(rank => rank === "")/2

    if (sliceNumber != -0.5 && sliceNumber <= 10) {
        var values = Object.values(data).slice(0,sliceNumber)
        var freq = Object.values(data).slice(sliceNumber,sliceNumber*2)
    }
    else  {
        var values = Object.values(data).slice(0,10)
        var freq = Object.values(data).slice(10,20)
    }

    // index of
    var dataset = freq
    //Width and height
    var w = 300;
    var h = 100;
    var barPadding = 1;

    id2 = '#table1_' + id
    //Create SVG element
    var svg = d3.selectAll(id2)
                .append("svg")
                .attr("width", w)
                .attr("height", h);

    svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
//        .attr("x", 0)
//        .attr("y", 0)
    .attr("width", 20)
    .attr("height", 100)
    .attr("x", function(d, i) {
        return i * (w / dataset.length-barPadding);
    })
    .attr("y", function(d) {
        return h - d;  //Height minus data value
    })
    .attr("height", function(d) {
        return d*100;  //Just the data value
    })
    .attr("fill", '#87CEFA');
}

    //        var svgWidth = 500;
    //        var svgHeight = 300;
    //
    //        var svg = d3.select('#chart')
    //            .attr("width", svgWidth)
    //            .attr("height", svgHeight)
    //            .attr("class", "bar-chart");
    //
    //        var dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];
    //
    //        var barPadding = 5;
    //        var barWidth = (svgWidth / dataset.length);
    //
    //        svg.selectAll("rect")
    //            .data(dataset)
    //            .enter()
    //            .append("rect")
    //            .attr("y", function(d) {
    //                return svgHeight - d + 'px'
    //            })
    //            .attr("height", function(d) {
    //                return d;
    //            })
    //            .attr("width", barWidth - barPadding +'px')
    //            .attr("transform", function (d, i) {
    //                 var translate = [barWidth * i, 0];
    //                 return "translate("+ translate +")";
    //            });

    //        var data = [30, 86, 168, 281, 303, 365];
    //
    //        var svg = d3.select('#chart')
    //            .append('svg')
    //            .attr('width', 600)
    //            .attr('height', 10);
    //
    //        svg.selectAll('rect')
    //        .data(data)
    //        .enter()
    //        .append('rect')
    //        .attr('width', function(d){
    //            return d;})
    //        .attr('x',function(d, i){
    //            return prev_width[i]; })
    //        .attr('fill', function(d, i){ return colors[i]; })
    //        .attr('y',0)
    //        .attr('height', 10);
      //  }
//    )
//}
