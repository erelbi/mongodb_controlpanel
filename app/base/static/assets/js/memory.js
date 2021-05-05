
        var mongo_data=[];
          function mongostatus(){

                    $.getJSON('http://localhost:5000/status', function(data) {
                    mem = data['mem']['virtual']
                    bits = data['mem']['bits']
                    netin = data['network']['bytesIn']
                    netout = data['network']['bytesOut']
                    insert = data['opcounters']['insert']
                    query = data['opcounters']['query']
                    update = data['opcounters']['update']
                    deletecommand = data['opcounters']['delete']
                    getmore = data['opcounters']['getmore']
                    command = data['opcounters']['command']
                    mongo_data = [mem,bits,netin,netout,insert,query,update,deletecommand,getmore,command]
                    }
                    );
                /*     return [mem,bits,netin,netout]*/
                    }
        window.onload = function () {


        var dps = []; // dataPoints
        var dps2 = [];
        var dps3 = [];
        var dps4 = [];
        var dps5 = [];
        var dps6 = [];
        var dps7 = [];
        var dps8 = [];
        var dps9 = [];
        var dps10 = [];
        var xVal = 0;
        var yVal = 100;
        var updateInterval = 1000;
        var dataLength = 20;


        /*Memory Chart*/
        var chart = new CanvasJS.Chart("chartContainer", {
            title :{
                text: "Mongo Memory"
            },
            	data: [{
		type: "line",

		yValueFormatString: "#### MB",

		showInLegend: true,
		name: "virtual memory",
		dataPoints: dps
		},
		{
			type: "line",

			yValueFormatString: "#### MB",
			showInLegend: true,
			name: "bits" ,
			dataPoints: dps2
	}]
        });



        var updateChart = function (count) {


            count = count || 1;

            for (var j = 0; j < count; j++) {

                virtual_mem = mongo_data[0]
                bits_mem= mongo_data[1]

                dps.push({
                    x: xVal,
                    y: virtual_mem
                });
                dps2.push({
                    x: xVal,
                    y: bits_mem
                });
                xVal++;
            }

            if (dps.length > dataLength) {
                dps.shift();
                dps2.shift()
            }
            chart.options.data[0].legendText = "bits:" + mongo_data[0]+"  MB";
            chart.options.data[1].legendText = "virtual:" + mongo_data[1]+"  MB";
            chart.render();
        };



        /*
        Network Chart*/

        var chartnetwork = new CanvasJS.Chart("chartnetwork", {
            title :{
                text: "Mongo  Network"
            },
            	data: [{
		type: "line",

		yValueFormatString: "#### KB",
		showInLegend: true,
		name: "input",
		dataPoints: dps3
		},
		{
			type: "line",
           	yValueFormatString: "#### KB",
			showInLegend: true,
			name: "output" ,
			dataPoints: dps4
	}]
        });


        var updateChart2 = function (count) {

            count = count || 1;

            for (var j = 0; j < count; j++) {

                input = mongo_data[2]
                output = mongo_data[3]


                dps3.push({
                    x: xVal,
                    y: input
                });
                dps4.push({
                    x: xVal,
                    y: output
                });
                xVal++;
            }

            if (dps3.length > dataLength) {
                dps3.shift();
                dps4.shift()
            }
            chartnetwork.options.data[0].legendText = "input:" + mongo_data[2]+"  KB";
            chartnetwork.options.data[1].legendText = "output:" + mongo_data[3]+"  KB";
            chartnetwork.render();
        };



        var chartopertion = new CanvasJS.Chart("chartopertion", {
            title :{
                text: "Mongo  Operation"
            },
            	data: [{
		type: "line",

		yValueFormatString: "#####",
		showInLegend: true,
		name: "insert",
		dataPoints: dps5
		},
		{
			type: "line",
           	yValueFormatString: "######",
			showInLegend: true,
			name: "query" ,
			dataPoints: dps6
	},
		{
			type: "line",
           	yValueFormatString: "######",
			showInLegend: true,
			name: "update" ,
			dataPoints: dps7
	},
		{
			type: "line",
           	yValueFormatString: "######",
			showInLegend: true,
			name: "delete" ,
			dataPoints: dps8
	},
		{
			type: "line",
           	yValueFormatString: "######",
			showInLegend: true,
			name: "getmore" ,
			dataPoints: dps9
	},
		{
			type: "line",
           	yValueFormatString: "######",
			showInLegend: true,
			name: "command" ,
			dataPoints: dps10
	},

	]
        });
            var updateChart3 = function (count) {

            count = count || 1;

            for (var j = 0; j < count; j++) {



                console.log(mongo_data[4],mongo_data[5],mongo_data[6],mongo_data[7],mongo_data[8],mongo_data[9])
                dps5.push({
                    x: xVal,
                    y: mongo_data[4]
                });
                dps6.push({
                    x: xVal,
                    y: mongo_data[5]
                });
                dps7.push({
                    x: xVal,
                    y: mongo_data[6]
                });
                  dps8.push({
                    x: xVal,
                    y: mongo_data[7]
                });
                  dps9.push({
                    x: xVal,
                    y: mongo_data[8]
                });
                   dps10.push({
                    x: xVal,
                    y: mongo_data[9]
                });
                xVal++;
            }

            if (dps5.length > dataLength) {
                dps5.shift();
                dps6.shift();
                dps7.shift();
                dps8.shift();
                dps9.shift();
                dps10.shift();


            }
            chartopertion.options.data[0].legendText = "insert:" + mongo_data[4];
            chartopertion.options.data[1].legendText = "query:" + mongo_data[5];
            chartopertion.options.data[2].legendText = "update:" + mongo_data[6];
            chartopertion.options.data[3].legendText = "delete:" + mongo_data[7];
            chartopertion.options.data[4].legendText = "getmore:" + mongo_data[8];
            chartopertion.options.data[5].legendText = "command:" + mongo_data[9];
            chartopertion.render();
        };




updateChart(dataLength);
updateChart2(dataLength);
updateChart3(dataLength);
setInterval(function(){updateChart(),updateChart2(),updateChart3(),mongostatus()}, updateInterval);
}

