const svg_width = 960;
const svg_height = 800;

var svg = d3.select("#board")
  .append("svg")
    .attr("viewBox", "0 0 " + svg_width + " " + svg_height);

function generate_board(n){
	svg.selectAll("*").remove();

	
	const bottom_offset = 20;
	const board_bottom = bottom_offset;
	
	const board_width = 400;
	const left_offset = 100;
	
	var user_chosen_segmentation = n;
	var tile_width = board_width/(2**user_chosen_segmentation);
	
	var dataset_x = [];
	var padding = 20;
	for(var k = 0; k < (2**user_chosen_segmentation) + 1; k++) {
		dataset_x[k] = 
			k*(board_width/(2**user_chosen_segmentation)) + 
			left_offset + (k*padding);
	}
	
	for(var j = 0; j < (2**user_chosen_segmentation); j++) {
		for(var i = 0; i < (2**user_chosen_segmentation); i++) {
			svg.append("rect")
			    .attr("class", "tile")
			    .attr("x", dataset_x[i])
			    .attr("y", board_bottom + (j*tile_width) + (j*padding))
			    .attr("width", tile_width)
			    .attr("height", tile_width)
			    .attr("stroke", "#696a61")
			    .attr("stroke-width", 2)
			    .attr("fill", "none");
			svg.append("rect")
			    .attr("class", "tile")
			    .attr("x", dataset_x[i])
			    .attr("y", board_bottom + (j*tile_width) + (j*padding))
			    .attr("width", tile_width)
			    .attr("height", tile_width)
			    .attr("stroke", "#696a61")
			    .attr("stroke-width", 15)
			    .attr("stroke-opacity", 0)
			    .attr("fill", "none");
		}
	}
	
	var tile_color = "none";
	
	var change_tile_color_none = document.getElementById("none");
	var on_click_none = function(e) {
		console.log('tile_color was ', tile_color);
		tile_color = "none";
		console.log('Now, tile_color is ', tile_color);
	}
	change_tile_color_none.onclick = on_click_none;
	svg.selectAll("rect.tile")
	    .on("click", function() {
		    d3.select(this)
		        .attr("fill", tile_color);
	    });
	
	var change_tile_color_green = document.getElementById("green");
	var on_click_green = function(e) {
		console.log('tile_color was ', tile_color);
		tile_color = "#759e16";
		console.log('Now, tile_color is ', tile_color);
	}
	change_tile_color_green.onclick = on_click_green;
	svg.selectAll("rect.tile")
	    .on("click", function() {
		    d3.select(this)
		        .attr("fill", tile_color);
	    });
	
	var change_tile_color_purple = document.getElementById("purple");
	var on_click_purple = function(e) {
		console.log('tile_color was ', tile_color);
		tile_color = "#9977bd";
		console.log('Now, tile_color is ', tile_color);
	}
	change_tile_color_purple.onclick = on_click_purple;
	svg.selectAll("rect.tile")
	    .on("click", function() {
		    d3.select(this)
		        .attr("fill", tile_color);
	    });
	
	var change_tile_color_orange = document.getElementById("orange");
	var on_click_orange = function(e) {
		console.log('tile_color was ', tile_color);
		tile_color = "#e0620d";
		console.log('Now, tile_color is ', tile_color);
	}
	change_tile_color_orange.onclick = on_click_orange;
	svg.selectAll("rect.tile")
	    .on("click", function() {
		    d3.select(this)
		        .attr("fill", tile_color);
	    });
	
	var change_tile_color_blue = document.getElementById("blue");
	var on_click_blue = function(e) {
		console.log('tile_color was ', tile_color);
		tile_color = "#91d5e4";
		console.log('Now, tile_color is ', tile_color);
	}
	change_tile_color_blue.onclick = on_click_blue;
	svg.selectAll("rect.tile")
	    .on("click", function() {
		    d3.select(this)
		        .attr("fill", tile_color);
	    });
	
	var change_tile_color_brown = document.getElementById("brown");
	var on_click_brown = function(e) {
		console.log('tile_color was ', tile_color);
		tile_color = "#696a61";
		console.log('Now, tile_color is ', tile_color);
	}
	change_tile_color_brown.onclick = on_click_brown;
	svg.selectAll("rect.tile")
	    .on("click", function() {
		    d3.select(this)
		        .attr("fill", tile_color);
	    });
}
