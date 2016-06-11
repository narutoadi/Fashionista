$(document).ready(function() {

    // time vs like graph
     var graph = {
        chart: {
            renderTo: 'container',
            type: 'line',
        },
        legend: {enabled: false},
        title: {text: 'Time vs Like Graph'},
        subtitle: {text: 'from starting of competition'},
        xAxis: {type: 'datetime', dateTimeLabelFormats:{ month:'%e.%b', year:'%b' }, labels: {rotation: -45}},
        yAxis: {title: {text: null}},
        series: [{}],
    };
    var uname = $('#username').attr("uname");
    var graphUrl = "/FashionPoll/graph/"+uname+"/";
    $.getJSON(graphUrl,
        function(data) {
            graph.series[0].name = 'Likes';
            graph.series[0].data = data;
            var chart = new Highcharts.Chart(graph);
    });

} );