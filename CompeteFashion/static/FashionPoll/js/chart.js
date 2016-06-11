$(document).ready(function() {
    $('#xyz').click(function(){
        var options = {
            chart: {
                renderTo: 'container',
                type: 'spline'
            },
            series: [{}]
        };
        var username1 = $('#username').attr("username");
        $.get('/FashionPoll/graph/',{ username : username1 } function(data) {
            options.series[0].data = data;
            var chart = new Highcharts.Chart(options);
        });
    });
});