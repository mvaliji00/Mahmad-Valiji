//d3.json('/data).then(
//    function rest(data) {
//        console.log(data)
//    }
//
//)

d3.json("/data?user=123").then(function(data) {
    console.log(data);
});