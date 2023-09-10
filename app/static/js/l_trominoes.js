const svg_width = 960;
const svg_height = 700;

var svg = d3.select("#board")
  .append("svg")
    .attr("viewBox", "0 0 " + svg_width + " " + svg_height);

const bottom_offset = 20;
const board_bottom = bottom_offset;

const board_width = 600;
const left_offset = 200;

var user_chosen_segmentation = 1;
var tile_width = board_width/(2**user_chosen_segmentation);

var dataset_x = [];

for(var k = 0; k < (2**user_chosen_segmentation) + 1; k++) {
	dataset_x[k] = 
		k*(board_width/(2**user_chosen_segmentation)) + 
		left_offset;
}

for(var j = 0; j < (2**user_chosen_segmentation); j++) {
	for(var i = 0; i < (2**user_chosen_segmentation); i++) {
		svg.append("rect")
		    .attr("class", "tile")
		    .attr("x", dataset_x[i])
		    .attr("y", board_bottom + (j*tile_width))
		    .attr("width", tile_width)
		    .attr("height", tile_width)
		    .attr("stroke", "#9977bd")
		    .attr("stroke-width", 1)
		    .attr("fill", "none");
	}
}
