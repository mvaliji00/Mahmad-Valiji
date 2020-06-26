function bar (id,valid,missing) {
    var global_width= 600

    var datavars = [((valid/100)*global_width),((missing/100)*global_width)]
    var prev_width = [0, datavars[0]] //, datavars[0] +  datavars[1]];

    var colors = ['#87CEFA', '#696969'];

    var svg = d3.select('#table2_'+id)
    .append('svg')
    .attr('width', 600)
    .attr('height', 10);

    svg.selectAll('rect')
    .data(datavars)
    .enter()
    .append('rect')
    .attr('width', function(d){
        return d;})
    .attr('x',function(d, i){
        return prev_width[i]; })
    .attr('fill', function(d, i){ return colors[i]; })
    .attr('y',0)
    .attr('height', 10);

 }
