const svg_width = 960;
const svg_height = 800;

var svg = d3.select("#peterson_graph")
  .append("svg")
    .attr("viewBox", "0 0 " + svg_width + " " + svg_height);

const inner_circle_radius = 120;
const outer_circle_radius = 160;
const x_center = svg_width/2;
const y_center = svg_height/2;

var N = 33;
var k = 10;

var angle_size = (Math.PI*2)/N;

for (var i = 0; i < N; i++) {
	var outer_x1 = x_center + 
		outer_circle_radius*Math.cos(Math.PI/2 + i*angle_size);
	var outer_y1 = y_center + 
		outer_circle_radius*Math.sin(Math.PI/2 + i*angle_size);
	var outer_x2 = x_center + 
		outer_circle_radius*Math.cos(Math.PI/2 + 
		(i+1)*angle_size);
	var outer_y2 = y_center + 
		outer_circle_radius*Math.sin(Math.PI/2 + 
		(i+1)*angle_size);

	svg.append("line")
	    .attr("x1", outer_x1)
	    .attr("y1", outer_y1)
	    .attr("x2", outer_x2)
	    .attr("y2", outer_y2)
	    .attr("stroke", "#696a61")
	    .attr("stroke-width", 2);

	var inner_x1 = x_center + 
		inner_circle_radius*Math.cos(Math.PI/2 + i*angle_size)
	var inner_y1 = y_center + 
		inner_circle_radius*Math.sin(Math.PI/2 + i*angle_size)
	var inner_x2 = x_center + 
		inner_circle_radius*Math.cos(Math.PI/2 + 
		(i+k)*angle_size);
	var inner_y2 = y_center + 
		inner_circle_radius*Math.sin(Math.PI/2 + 
		(i+k)*angle_size);

	svg.append("line")
	    .attr("x1", inner_x1)
	    .attr("y1", inner_y1)
	    .attr("x2", inner_x2)
	    .attr("y2", inner_y2)
	    .attr("stroke", "#696a61")
	    .attr("stroke-width", 2);
}
