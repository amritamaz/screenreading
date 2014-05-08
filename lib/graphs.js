$(window).load(function() {
var ctx = document.getElementById("myChart").getContext("2d");
var myNewChart = new Chart(ctx).PolarArea(data);

var data = [
    {
	value : 30,
	color: "#D97041"
    },
    {
	value : 90,
	color: "#C7604C"
    },
    {
	value : 24,
	color: "#21323D"
    },
    {
	value : 58,
	color: "#9D9B7F"
    },
    {
	value : 82,
	color: "#7D4F6D"
    },
    {
	value : 8,
	color: "#584A5E"
    }
]
		
    })(jQuery);	
