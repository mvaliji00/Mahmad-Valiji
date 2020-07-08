//window.onload = function () {
//    var names = ['Frank', 'Tom', 'Peter', 'Mary'];
//
//	var ul = d3.select('#dataList').append('ul');
//
//	ul.selectAll('a')
//	.data(names)
//	.enter()
//	.append('a')
//	.html(String);
//
//}


d3.json('/get-data4').then(function(data){
    var ul = d3.select('#dataList').append('ul');

	ul.selectAll('a')
	.data(data)
	.enter()
	.append('a')
	.html(String)
})


