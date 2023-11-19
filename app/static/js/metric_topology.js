// Drawing a rectangular block to represent the BLOCK OF BUTTER --------------
// 
//
var w_block = 960;
var h_block = 300;

var svg_block = d3.select("#block0")
  .append("svg")
    .attr("viewBox", "0 0 " + w_block + " " + h_block);

// BLOCK OF BUTTER label
svg_block.append("text")
    .text("BLOCK OF BUTTER")
    .attr("x", w_block*(5/15))
    .attr("y", h_block*(3/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "32px")
    .attr("fill", "#3a3a36");


// back-facing long edge of block
// top line
svg_block.append("line")
    .attr("x1", w_block*(2.87/15))
    .attr("y1", h_block*(1/10))
    .attr("x2", w_block*(13.87/15))
    .attr("y2", h_block*(1/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_block.append("line")
    .attr("x1", w_block*(2.87/15))
    .attr("y1", h_block*(6/10))
    .attr("x2", w_block*(13.87/15))
    .attr("y2", h_block*(6/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// front-facing long edge of block
// top line
svg_block.append("line")
    .attr("x1", w_block*(1/15))
    .attr("y1", h_block*(4/10))
    .attr("x2", w_block*(12/15))
    .attr("y2", h_block*(4/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_block.append("line")
    .attr("x1", w_block*(1/15))
    .attr("y1", h_block*(9/10))
    .attr("x2", w_block*(12/15))
    .attr("y2", h_block*(9/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right-facing short edge of block
// top line
svg_block.append("line")
    .attr("x1", w_block*(12/15))
    .attr("y1", h_block*(4/10))
    .attr("x2", w_block*(13.87/15))
    .attr("y2", h_block*(1/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_block.append("line")
    .attr("x1", w_block*(12/15))
    .attr("y1", h_block*(4/10))
    .attr("x2", w_block*(12/15))
    .attr("y2", h_block*(9/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_block.append("line")
    .attr("x1", w_block*(12/15))
    .attr("y1", h_block*(9/10))
    .attr("x2", w_block*(13.87/15))
    .attr("y2", h_block*(6/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_block.append("line")
    .attr("x1", w_block*(13.87/15))
    .attr("y1", h_block*(6/10))
    .attr("x2", w_block*(13.87/15))
    .attr("y2", h_block*(1/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left-facing short edge of block
// top line
svg_block.append("line")
    .attr("x1", w_block*(2.87/15))
    .attr("y1", h_block*(1/10))
    .attr("x2", w_block*(1/15))
    .attr("y2", h_block*(4/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_block.append("line")
    .attr("x1", w_block*(1/15))
    .attr("y1", h_block*(4/10))
    .attr("x2", w_block*(1/15))
    .attr("y2", h_block*(9/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_block.append("line")
    .attr("x1", w_block*(1/15))
    .attr("y1", h_block*(9/10))
    .attr("x2", w_block*(2.87/15))
    .attr("y2", h_block*(6/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_block.append("line")
    .attr("x1", w_block*(2.87/15))
    .attr("y1", h_block*(6/10))
    .attr("x2", w_block*(2.87/15))
    .attr("y2", h_block*(1/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// Big R indicating the Right Face of this rectangular block of butter
svg_block.append("text")
    .text("R")
    .attr("x", w_block*(51/60))
    .attr("y", h_block*(11/20))
    .attr("font-family", "sans-serif")
    .attr("font-size", "82px")
    .attr("fill", "#6b4691")
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 2);

// Drawing a cross section of the BLOCK OF BUTTER ----------------------------
// 
//
var w_cross_block = 480;
var h_cross_block = 380;
var svg_cross_1_block = d3.select("#block1")
  .append("svg")
    .attr("viewBox", "0 0 " + w_cross_block + " " + h_cross_block);

// i) label
svg_cross_1_block.append("text")
    .text("i)")
    .attr("x", w_cross_block/2)
    .attr("y", h_cross_block*(1/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "32px")
    .attr("fill", "#3a3a36");

// top line
svg_cross_1_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_cross_1_block.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_cross_1_block.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_cross_1_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");


// Drawing a cross section of the BLOCK OF BUTTER after breaking it down -----
// to 4 sticks of butter -----------------------------------------------------
// 
//
var svg_cross_4_block = d3.select("#block2")
  .append("svg")
    .attr("viewBox", "0 0 " + w_cross_block + " " + h_cross_block);

// ii) label
svg_cross_4_block.append("text")
    .text("ii)")
    .attr("x", w_cross_block/2)
    .attr("y", h_cross_block*(1/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "32px")
    .attr("fill", "#3a3a36");

// top line
svg_cross_4_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_cross_4_block.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_cross_4_block.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_cross_4_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle horizontal line
svg_cross_4_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(5/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(5/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle vertical line
svg_cross_4_block.append("line")
    .attr("x1", w_cross_block*(7.5/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(7.5/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");



// Cross sections of butter bearing center points ----------------------------
//
//
d3.select("#center_point")
    .on("click", function() {
	// Drawing a cross section of the BLOCK OF BUTTER with a center point -
	// 
	//
	
	// center point
	svg_cross_1_block.append("circle")
	    .style("fill", "#3a3a36")
	    .attr("cx", w_cross_block*(7.5/15))
	    .attr("cy", h_cross_block*(5/10))
	    .attr("r", 5);

	
	
	// Drawing a cross section of the BLOCK OF BUTTER after breaking it --
	// down to 4 sticks of butter with center points ---------------------
	// 
	//
	// center points
	// top left
	svg_cross_4_block.append("circle")
	    .style("fill", "#3a3a36")
	    .attr("cx", w_cross_block*(5.25/15))
	    .attr("cy", h_cross_block*(3.5/10))
	    .attr("r", 5);
	
	// top right
	svg_cross_4_block.append("circle")
	    .style("fill", "#3a3a36")
	    .attr("cx", w_cross_block*(9.75/15))
	    .attr("cy", h_cross_block*(3.5/10))
	    .attr("r", 5);

	// bottom left
	svg_cross_4_block.append("circle")
	    .style("fill", "#3a3a36")
	    .attr("cx", w_cross_block*(5.25/15))
	    .attr("cy", h_cross_block*(6.5/10))
	    .attr("r", 5);

	// bottom right
	svg_cross_4_block.append("circle")
	    .style("fill", "#3a3a36")
	    .attr("cx", w_cross_block*(9.75/15))
	    .attr("cy", h_cross_block*(6.5/10))
	    .attr("r", 5);
});


// Drawing a cross section of the BLOCK OF BUTTER after breaking it-----------
// down to 3 sticks of butter of one size and several sticks of butter -------
// of a different size -------------------------------------------------------
//
//
var svg_cross_3_and_1_several_block = d3.select("#block3")
  .append("svg")
    .attr("viewBox", "0 0 " + w_cross_block + " " + h_cross_block);


// top line
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle horizontal line
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(5/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(5/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle vertical line
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(7.5/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(7.5/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line in bottom right stick of butter
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(9/15))
    .attr("y1", h_cross_block*(5/10))
    .attr("x2", w_cross_block*(9/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line in bottom right stick of butter
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(10.5/15))
    .attr("y1", h_cross_block*(5/10))
    .attr("x2", w_cross_block*(10.5/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// top horizontal line in bottom right stick of butter
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(7.5/15))
    .attr("y1", h_cross_block*(6/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(6/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom horizontal line in bottom right stick of butter
svg_cross_3_and_1_several_block.append("line")
    .attr("x1", w_cross_block*(7.5/15))
    .attr("y1", h_cross_block*(7/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(7/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// center points
// top left
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(5.25/15))
    .attr("cy", h_cross_block*(3.5/10))
    .attr("r", 5);

// top right
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(9.75/15))
    .attr("cy", h_cross_block*(3.5/10))
    .attr("r", 5);

// bottom left
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(5.25/15))
    .attr("cy", h_cross_block*(6.5/10))
    .attr("r", 5);

// bottom right, r1, c1
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(8.25/15))
    .attr("cy", h_cross_block*(5.5/10))
    .attr("r", 5);

// bottom right, r1, c2
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(9.75/15))
    .attr("cy", h_cross_block*(5.5/10))
    .attr("r", 5);

// bottom right, r1, c3
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(11.25/15))
    .attr("cy", h_cross_block*(5.5/10))
    .attr("r", 5);

// bottom right, r2, c1
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(8.25/15))
    .attr("cy", h_cross_block*(6.5/10))
    .attr("r", 5);

// bottom right, r2, c2
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(9.75/15))
    .attr("cy", h_cross_block*(6.5/10))
    .attr("r", 5);

// bottom right, r2, c3
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(11.25/15))
    .attr("cy", h_cross_block*(6.5/10))
    .attr("r", 5);

// bottom right, r3, c1
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(8.25/15))
    .attr("cy", h_cross_block*(7.5/10))
    .attr("r", 5);

// bottom right, r3, c2
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(9.75/15))
    .attr("cy", h_cross_block*(7.5/10))
    .attr("r", 5);

// bottom right, r3, c3
svg_cross_3_and_1_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(11.25/15))
    .attr("cy", h_cross_block*(7.5/10))
    .attr("r", 5);



// Drawing a cross section of the BLOCK OF BUTTER after breaking it-----------
// down to 2 sticks of butter of one size, several sticks of butter ----------
// of a second size, and several sticks of butter of a third size ------------
//
//
var svg_cross_2_and_2_several_block = d3.select("#block4")
  .append("svg")
    .attr("viewBox", "0 0 " + w_cross_block + " " + h_cross_block);

// top line
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle vertical line in top left stick of butter
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(5.25/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(5.25/15))
    .attr("y2", h_cross_block*(5/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle horizontal line in top left stick of butter
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(3.5/10))
    .attr("x2", w_cross_block*(7.5/15))
    .attr("y2", h_cross_block*(3.5/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle horizontal line
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(5/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(5/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle vertical line
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(7.5/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(7.5/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line in bottom right stick of butter
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(9/15))
    .attr("y1", h_cross_block*(5/10))
    .attr("x2", w_cross_block*(9/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical vertical line in bottom right stick of butter
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(10.5/15))
    .attr("y1", h_cross_block*(5/10))
    .attr("x2", w_cross_block*(10.5/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// top horizontal line in bottom right stick of butter
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(7.5/15))
    .attr("y1", h_cross_block*(6/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(6/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom horizontal line in bottom right stick of butter
svg_cross_2_and_2_several_block.append("line")
    .attr("x1", w_cross_block*(7.5/15))
    .attr("y1", h_cross_block*(7/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(7/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// center points
// top left, r1, c1
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(4.13/15))
    .attr("cy", h_cross_block*(2.75/10))
    .attr("r", 5)

// top left, r1, c2
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(6.38/15))
    .attr("cy", h_cross_block*(2.75/10))
    .attr("r", 5)

// top left, r2, c1
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(4.13/15))
    .attr("cy", h_cross_block*(4.25/10))
    .attr("r", 5)

// top left, r2, c2
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(6.38/15))
    .attr("cy", h_cross_block*(4.25/10))
    .attr("r", 5)

// top right
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(9.75/15))
    .attr("cy", h_cross_block*(3.5/10))
    .attr("r", 5);

// bottom left
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(5.25/15))
    .attr("cy", h_cross_block*(6.5/10))
    .attr("r", 5);

// bottom right, r1, c1
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(8.25/15))
    .attr("cy", h_cross_block*(5.5/10))
    .attr("r", 5);

// bottom right, r1, c2
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(9.75/15))
    .attr("cy", h_cross_block*(5.5/10))
    .attr("r", 5);

// bottom right, r1, c3
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(11.25/15))
    .attr("cy", h_cross_block*(5.5/10))
    .attr("r", 5);

// bottom right, r2, c1
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(8.25/15))
    .attr("cy", h_cross_block*(6.5/10))
    .attr("r", 5);

// bottom right, r2, c2
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(9.75/15))
    .attr("cy", h_cross_block*(6.5/10))
    .attr("r", 5);

// bottom right, r2, c3
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(11.25/15))
    .attr("cy", h_cross_block*(6.5/10))
    .attr("r", 5);

// bottom right, r3, c1
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(8.25/15))
    .attr("cy", h_cross_block*(7.5/10))
    .attr("r", 5);

// bottom right, r3, c2
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(9.75/15))
    .attr("cy", h_cross_block*(7.5/10))
    .attr("r", 5);

// bottom right, r3, c3
svg_cross_2_and_2_several_block.append("circle")
    .style("fill", "#3a3a36")
    .attr("cx", w_cross_block*(11.25/15))
    .attr("cy", h_cross_block*(7.5/10))
    .attr("r", 5);



// Drawing a rectangle; ------------------------------------------------------
// then allowing the user to draw another rectangle --------------------------
// within by the click of ----------------------------------------------------
// a button. The user has buttons for all three choices: drawing a rectangle -
// of a medium size; smaller; or bigger --------------------------------------
// 
//
var svg_rect_1_plus_3 = d3.select("#block5")
  .append("svg")
    .attr("viewBox", "0 0 " + w_cross_block + " " + h_cross_block);

// top line
svg_rect_1_plus_3.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_rect_1_plus_3.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_rect_1_plus_3.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_rect_1_plus_3.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// Drawing a medium size rectangle within ------------------------------------
//
//
d3.select("#medium_size_rect_1_plus_3")
    .on("click", function() {
	    // top
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(4/15))
	        .attr("y1", h_cross_block*(4/10))
	        .attr("x2", w_cross_block*(7/15))
	        .attr("y2", h_cross_block*(4/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // right vertical side
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(7/15))
	        .attr("y1", h_cross_block*(4/10))
	        .attr("x2", w_cross_block*(7/15))
	        .attr("y2", h_cross_block*(6/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
	    
	    // bottom
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(7/15))
	        .attr("y1", h_cross_block*(6/10))
	        .attr("x2", w_cross_block*(4/15))
	        .attr("y2", h_cross_block*(6/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // left vertical side
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(4/15))
	        .attr("y1", h_cross_block*(6/10))
	        .attr("x2", w_cross_block*(4/15))
	        .attr("y2", h_cross_block*(4/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
    });

// Drawing the smaller rectangle within --------------------------------------
//
//
d3.select("#smaller_size_rect_1_plus_3")
    .on("click", function() {
	    // top
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(3.5/15))
	        .attr("y1", h_cross_block*(2.5/10))
	        .attr("x2", w_cross_block*(4.5/15))
	        .attr("y2", h_cross_block*(2.5/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // right vertical side
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(4.5/15))
	        .attr("y1", h_cross_block*(2.5/10))
	        .attr("x2", w_cross_block*(4.5/15))
	        .attr("y2", h_cross_block*(3.16/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
	    
	    // bottom
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(4.5/15))
	        .attr("y1", h_cross_block*(3.16/10))
	        .attr("x2", w_cross_block*(3.5/15))
	        .attr("y2", h_cross_block*(3.16/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // left vertical side
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(3.5/15))
	        .attr("y1", h_cross_block*(3.16/10))
	        .attr("x2", w_cross_block*(3.5/15))
	        .attr("y2", h_cross_block*(2.5/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
    });

// Drawing the larger rectangle within ---------------------------------------
//
//
d3.select("#larger_size_rect_1_plus_3")
    .on("click", function() {
	    // top
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(5.5/15))
	        .attr("y1", h_cross_block*(3.25/10))
	        .attr("x2", w_cross_block*(11.5/15))
	        .attr("y2", h_cross_block*(3.25/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // right vertical side
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(11.5/15))
	        .attr("y1", h_cross_block*(3.25/10))
	        .attr("x2", w_cross_block*(11.5/15))
	        .attr("y2", h_cross_block*(7.25/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
	    
	    // bottom
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(11.5/15))
	        .attr("y1", h_cross_block*(7.25/10))
	        .attr("x2", w_cross_block*(5.5/15))
	        .attr("y2", h_cross_block*(7.25/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // left vertical side
	    svg_rect_1_plus_3.append("line")
	        .attr("x1", w_cross_block*(5.5/15))
	        .attr("y1", h_cross_block*(7.25/10))
	        .attr("x2", w_cross_block*(5.5/15))
	        .attr("y2", h_cross_block*(3.25/10))
	        .style("stroke", "#91d5e4")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
    });




// Drawing a rectangle; breaking it down -------------------------------------
// to 4 subrectangles; then allowing the user to draw another rectangle ------
// within by the click of ----------------------------------------------------
// a button. The user has buttons for all three choices: drawing a rectangle -
// of a medium size; smaller; or bigger --------------------------------------
// 
//


var svg_rect_4_plus_3 = d3.select("#block6")
  .append("svg")
    .attr("viewBox", "0 0 " + w_cross_block + " " + h_cross_block);


// top line
svg_rect_4_plus_3.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_rect_4_plus_3.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_rect_4_plus_3.append("line")
    .attr("x1", w_cross_block*(12/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_rect_4_plus_3.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(8/10))
    .attr("x2", w_cross_block*(3/15))
    .attr("y2", h_cross_block*(2/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle horizontal line
svg_rect_4_plus_3.append("line")
    .attr("x1", w_cross_block*(3/15))
    .attr("y1", h_cross_block*(5/10))
    .attr("x2", w_cross_block*(12/15))
    .attr("y2", h_cross_block*(5/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// middle vertical line
svg_rect_4_plus_3.append("line")
    .attr("x1", w_cross_block*(7.5/15))
    .attr("y1", h_cross_block*(2/10))
    .attr("x2", w_cross_block*(7.5/15))
    .attr("y2", h_cross_block*(8/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");



// Drawing a medium size rectangle within ------------------------------------
//
//
d3.select("#medium_size_rect_4_plus_3")
    .on("click", function() {
	    // top
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(4/15))
	        .attr("y1", h_cross_block*(4/10))
	        .attr("x2", w_cross_block*(7/15))
	        .attr("y2", h_cross_block*(4/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // right vertical side
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(7/15))
	        .attr("y1", h_cross_block*(4/10))
	        .attr("x2", w_cross_block*(7/15))
	        .attr("y2", h_cross_block*(6/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
	    
	    // bottom
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(7/15))
	        .attr("y1", h_cross_block*(6/10))
	        .attr("x2", w_cross_block*(4/15))
	        .attr("y2", h_cross_block*(6/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // left vertical side
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(4/15))
	        .attr("y1", h_cross_block*(6/10))
	        .attr("x2", w_cross_block*(4/15))
	        .attr("y2", h_cross_block*(4/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
    });

// Drawing the smaller rectangle within --------------------------------------
//
//
d3.select("#smaller_size_rect_4_plus_3")
    .on("click", function() {
	    // top
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(3.5/15))
	        .attr("y1", h_cross_block*(2.5/10))
	        .attr("x2", w_cross_block*(4.5/15))
	        .attr("y2", h_cross_block*(2.5/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // right vertical side
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(4.5/15))
	        .attr("y1", h_cross_block*(2.5/10))
	        .attr("x2", w_cross_block*(4.5/15))
	        .attr("y2", h_cross_block*(3.16/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
	    
	    // bottom
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(4.5/15))
	        .attr("y1", h_cross_block*(3.16/10))
	        .attr("x2", w_cross_block*(3.4/15))
	        .attr("y2", h_cross_block*(3.16/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // left vertical side
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(3.5/15))
	        .attr("y1", h_cross_block*(3.16/10))
	        .attr("x2", w_cross_block*(3.5/15))
	        .attr("y2", h_cross_block*(2.5/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
    });

// Drawing the larger rectangle within ---------------------------------------
//
//
d3.select("#larger_size_rect_4_plus_3")
    .on("click", function() {
	    // top
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(5.5/15))
	        .attr("y1", h_cross_block*(3.25/10))
	        .attr("x2", w_cross_block*(11.5/15))
	        .attr("y2", h_cross_block*(3.25/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // right vertical side
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(11.5/15))
	        .attr("y1", h_cross_block*(3.25/10))
	        .attr("x2", w_cross_block*(11.5/15))
	        .attr("y2", h_cross_block*(7.25/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
	    
	    // bottom
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(11.5/15))
	        .attr("y1", h_cross_block*(7.25/10))
	        .attr("x2", w_cross_block*(5.5/15))
	        .attr("y2", h_cross_block*(7.25/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");

	    // left vertical side
	    svg_rect_4_plus_3.append("line")
	        .attr("x1", w_cross_block*(5.5/15))
	        .attr("y1", h_cross_block*(7.25/10))
	        .attr("x2", w_cross_block*(5.5/15))
	        .attr("y2", h_cross_block*(3.25/10))
	        .style("stroke", "#d079a2")
	        .style("stroke-width", 5)
	        .style("stroke-dasharray", "12 3");
    });









// Draw a rectangle; allow user as many clicks of a button as they wish, -----
// each drawing a randomly ---------------------------------------------------
// sized rectangle within the larger rectangle -------------------------------

var w_rect = 960;
var h_rect = 480;

var svg_rect_1_plus_many = d3.select("#block9")
  .append("svg")
    .attr("viewBox", "0 0 " + w_rect + " " + h_rect);

// top line
svg_rect_1_plus_many.append("line")
    .attr("x1", w_rect*(3/15))
    .attr("y1", h_rect*(1/10))
    .attr("x2", w_rect*(12/15))
    .attr("y2", h_rect*(1/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// right vertical line
svg_rect_1_plus_many.append("line")
    .attr("x1", w_rect*(12/15))
    .attr("y1", h_rect*(1/10))
    .attr("x2", w_rect*(12/15))
    .attr("y2", h_rect*(9/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// bottom line
svg_rect_1_plus_many.append("line")
    .attr("x1", w_rect*(12/15))
    .attr("y1", h_rect*(9/10))
    .attr("x2", w_rect*(3/15))
    .attr("y2", h_rect*(9/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

// left vertical line
svg_rect_1_plus_many.append("line")
    .attr("x1", w_rect*(3/15))
    .attr("y1", h_rect*(9/10))
    .attr("x2", w_rect*(3/15))
    .attr("y2", h_rect*(1/10))
    .style("stroke", "#3a3a36")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3");

d3.select("#rect_1_plus_many")
    .on("click", function() {

	    var colors = ["#6b4691", "#91d5e4", "#d079a2"];

	    const random_color = Math.floor(Math.random()*colors.length);
    	
	    var i = Math.floor(Math.random()*12);
	    var k = Math.floor(Math.random()*13);

	    while (i < 3) {
		    i = Math.floor(Math.random()*12);
	    }

	    while (k <= i) {
    	    	    k = Math.floor(Math.random()*13);
	    }

	    var k_minus_i = k-i;


	    if (k_minus_i == 1) {
		    let j = 1;
		    let n = 1.66;
		    let scalar = Math.random()*(2 - (-0.5)) + (-0.5);
	    

            	    // top
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(i/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(k/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");


            	    // right vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(k/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(k/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // bottom
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(k/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(i/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // left vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(i/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(i/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
	    }
	    else if (k_minus_i == 2) {
		    let j = 1;
		    let n = 2.33;
		    let scalar = Math.random()*(2.17);
	    

            	    // top
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(i/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(k/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");


            	    // right vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(k/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(k/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // bottom
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(k/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(i/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // left vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(i/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(i/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
	    } 
	    else if (k_minus_i == 3) {
		    let j = 1;
		    let n = 3;
		    let scalar = Math.random()*(1.5);
	    

            	    // top
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(i/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(k/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");


            	    // right vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(k/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(k/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // bottom
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(k/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(i/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // left vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(i/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(i/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
	    }
	    else if (k_minus_i == 4) {
		    let j = 1;
		    let n = 3.66;
		    let scalar = Math.random()*(0.84);
	    

            	    // top
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(i/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(k/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");


            	    // right vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(k/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(k/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // bottom
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(k/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(i/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // left vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(i/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(i/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
	    } 
	    else {
		    let p = Math.floor(Math.random()*9) + 3;
		    let q = p+1;
		    let j = 1;
		    let n = 1.66;
		    let scalar = Math.random()*(2 - (-0.5)) + (-0.5);
	    

            	    // top
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(p/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(q/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");


            	    // right vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(q/15))
	    	        .attr("y1", w_rect*((j+scalar)/10))
	    	        .attr("x2", w_rect*(q/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // bottom
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(q/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(p/15))
	    	        .attr("y2", w_rect*((n+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
            	    
	    	    // left vertical
	    	    svg_rect_1_plus_many.append("line")
	    	        .attr("x1", w_rect*(p/15))
	    	        .attr("y1", w_rect*((n+scalar)/10))
	    	        .attr("x2", w_rect*(p/15))
	    	        .attr("y2", w_rect*((j+scalar)/10))
	    	        .style("stroke", colors[random_color])
	    	        .style("stroke-width", 5)
	    	        .style("stroke-dasharray", "12 3");
	    } 
    });




// Union of elements ---------------------------------------------------------
//
// Two boxes of different-sized circles unioned to one box -------------------

var circle_union_dataset_1 = [15, 20, 25];
var circle_union_dataset_2 = [18, 23, 28];

var w_union = 960;
var h_union = 230;

var svg_union = d3.select("#union")
  .append("svg")
    .attr("viewBox", "0 0 " + w_union + " " + h_union);

// box of circles set 1 label
svg_union.append("text")
    .text("Set A")
    .attr("x", 65)
    .attr("y", ((h_union/2) - 60))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

// box of circles set 2 label
svg_union.append("text")
    .text("Set B")
    .attr("x", 300)
    .attr("y", ((h_union/2) - 60))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

// box of circles sets 1 and 2 label
svg_union.append("text")
    .text("Set C")
    .attr("x", 640)
    .attr("y", ((h_union/2) - 60))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

// box of circles set 1
//
// top line
svg_union.append("line")
    .attr("x1", 5)
    .attr("y1", ((h_union/2) - 50))
    .attr("x2", 190)
    .attr("y2", ((h_union/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// right vertical line
svg_union.append("line")
    .attr("x1", 190)
    .attr("y1", ((h_union/2) - 50))
    .attr("x2", 190)
    .attr("y2", ((h_union/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// bottom line
svg_union.append("line")
    .attr("x1", 190)
    .attr("y1", ((h_union/2) + 50))
    .attr("x2", 5)
    .attr("y2", ((h_union/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// left vertical line
svg_union.append("line")
    .attr("x1", 5)
    .attr("y1", ((h_union/2) + 50))
    .attr("x2", 5)
    .attr("y2", ((h_union/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);
    
// box of circles set 2
//
// top line
svg_union.append("line")
    .attr("x1", 220)
    .attr("y1", ((h_union/2) - 50))
    .attr("x2", 430)
    .attr("y2", ((h_union/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// right vertical line
svg_union.append("line")
    .attr("x1", 430)
    .attr("y1", ((h_union/2) - 50))
    .attr("x2", 430)
    .attr("y2", ((h_union/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// bottom line
svg_union.append("line")
    .attr("x1", 430)
    .attr("y1", ((h_union/2) + 50))
    .attr("x2", 220)
    .attr("y2", ((h_union/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// left vertical line
svg_union.append("line")
    .attr("x1", 220)
    .attr("y1", ((h_union/2) + 50))
    .attr("x2", 220)
    .attr("y2", ((h_union/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// box of circles sets 1 and 2
//
// top line
svg_union.append("line")
    .attr("x1", 450)
    .attr("y1", ((h_union/2) - 50))
    .attr("x2", 880)
    .attr("y2", ((h_union/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// right vertical line
svg_union.append("line")
    .attr("x1", 880)
    .attr("y1", ((h_union/2) - 50))
    .attr("x2", 880)
    .attr("y2", ((h_union/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// bottom line
svg_union.append("line")
    .attr("x1", 880)
    .attr("y1", ((h_union/2) + 50))
    .attr("x2", 450)
    .attr("y2", ((h_union/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// left vertical line
svg_union.append("line")
    .attr("x1", 450)
    .attr("y1", ((h_union/2) + 50))
    .attr("x2", 450)
    .attr("y2", ((h_union/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

var circle_union_set_1 = svg_union.selectAll(".circle_union_set_1")
    .data(circle_union_dataset_1)
    .enter()
  .append("circle");

circle_union_set_1.attr("cx", function(d, i) {
		return (i*60)+30;
	})
	.attr("cy", h_union/2)
	.attr("r", function(d) {
		return d;
	})
	.attr("fill", "#f5ffde")
	.attr("stroke", "#759e16")
	.attr("stroke-width", 3)
	.attr("stroke-dasharray", "12 3")
	.attr("class", "circle_union_set_1");

svg_union.selectAll(".text_union_set_1")
    .data(circle_union_dataset_1)
    .enter()
  .append("text")
    .text(function(d) {
	    return d;
    })
    .attr("text-anchor", "middle")
    .attr("x", function(d, i) {
		return (i*60)+30;
	})
    .attr("y", (h_union/2)+5)
    .attr("font-family", "sans-serif")
    .attr("font-size", "18px")
    .attr("font-weight", "900")
    .attr("fill", "#3a3a36")
    .attr("class", "text_union_set_1");
    

var circle_union_set_2 = svg_union.selectAll(".circle_union_set_2")
    .data(circle_union_dataset_2)
    .enter()
  .append("circle");

circle_union_set_2.attr("cx", function(d, i) {
		return (i*70) + 250;
	})
	.attr("cy", h_union/2)
	.attr("r", function(d) {
		return d;
	})
	.attr("fill", "#f5ffde")
	.attr("stroke", "#759e16")
	.attr("stroke-width", 3)
	.attr("stroke-dasharray", "12 3")
	.attr("class", "circle_union_set_2");

svg_union.selectAll(".text_union_set_2")
    .data(circle_union_dataset_2)
    .enter()
  .append("text")
    .text(function(d) {
	    return d;
    })
    .attr("text-anchor", "middle")
    .attr("x", function(d, i) {
		return (i*70)+250;
	})
    .attr("y", (h_union/2)+5)
    .attr("font-family", "sans-serif")
    .attr("font-size", "18px")
    .attr("font-weight", "900")
    .attr("fill", "#3a3a36")
    .attr("class", "text_union_set_2");

d3.select("#union_button")
    .on("click", function() {
	    var union_dataset = [15, 18, 20, 23, 25, 28];
	    var circle_union_set = svg_union.selectAll(".union_circles")
	        .data(union_dataset)
	        .enter()
	      .append("circle")
	        .transition()
	        .duration(2000)
	        .on("start", function() {
			d3.select(this)
			    .attr("fill", "#3a3a36")
			    .attr("r", 3);
		})
	        .attr("cx", function(d, i) {
	    		return 450+(i*70)+30;
	    	})
	    	.attr("cy", h_union/2)
	        .on("end", function() {
			d3.select(this)
			    .transition()
			    .duration(1000)
			    .ease(d3.easeLinear)
	    		    .attr("fill", "#f5ffde")
	    		    .attr("stroke", "#759e16")
	    		    .attr("stroke-width", 3)
			    .attr("stroke-dasharray", "12 3")
	    		    .attr("r", function(d) {
	    			return d;
	    		    })

		})
	        .attr("class", "union_circles");

	    svg_union.selectAll(".union_text")
	        .data(union_dataset)
	        .enter()
	      .append("text")
	        .transition()
	        .duration(2000)
	        .on("start", function() {
			d3.select(this)
	        	    .attr("font-size", "1px")
		})
	        .text(function(d) {
	    	    return d;
	        })
	        .attr("text-anchor", "middle")
	        .attr("x", function(d, i) {
	    		return 450+(i*70)+30;
	    	})
	        .attr("y", (h_union/2)+5)
	        .attr("font-family", "sans-serif")
	        .attr("fill", "#3a3a36")
	        .on("end", function() {
			d3.select(this)
			    .transition()
			    .duration(1000)
			    .ease(d3.easeLinear)
   			    .attr("font-size", "18px")
   			    .attr("font-weight", "900");
		})
	        .attr("class", "union_text");

    });











// Intersection of elements --------------------------------------------------
//
// Two boxes of different- and same-size circles intersected to one box ------

var circle_intersection_dataset_1 = [15, 20, 25];
var circle_intersection_dataset_2 = [15, 23, 25];

var w_intersection = 960;
var h_intersection = 230;

var svg_intersection = d3.select("#intersection")
  .append("svg")
    .attr("viewBox", "0 0 " + w_intersection + " " + h_intersection);

// box of circles set 1 label
svg_intersection.append("text")
    .text("Set A")
    .attr("x", 65)
    .attr("y", ((h_intersection/2) - 60))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

// box of circles set 2 label
svg_intersection.append("text")
    .text("Set B")
    .attr("x", 300)
    .attr("y", ((h_intersection/2) - 60))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

// box of circles set 1 intersected with set 2 label
svg_intersection.append("text")
    .text("Set C")
    .attr("x", 490)
    .attr("y", ((h_intersection/2) - 60))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

// box of circles set 1
//
// top line
svg_intersection.append("line")
    .attr("x1", 5)
    .attr("y1", ((h_intersection/2) - 50))
    .attr("x2", 190)
    .attr("y2", ((h_intersection/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// right vertical line
svg_intersection.append("line")
    .attr("x1", 190)
    .attr("y1", ((h_intersection/2) - 50))
    .attr("x2", 190)
    .attr("y2", ((h_intersection/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// bottom line
svg_intersection.append("line")
    .attr("x1", 190)
    .attr("y1", ((h_intersection/2) + 50))
    .attr("x2", 5)
    .attr("y2", ((h_intersection/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// left vertical line
svg_intersection.append("line")
    .attr("x1", 5)
    .attr("y1", ((h_intersection/2) + 50))
    .attr("x2", 5)
    .attr("y2", ((h_intersection/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);
    
// box of circles set 2
//
// top line
svg_intersection.append("line")
    .attr("x1", 220)
    .attr("y1", ((h_intersection/2) - 50))
    .attr("x2", 430)
    .attr("y2", ((h_intersection/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// right vertical line
svg_intersection.append("line")
    .attr("x1", 430)
    .attr("y1", ((h_intersection/2) - 50))
    .attr("x2", 430)
    .attr("y2", ((h_intersection/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// bottom line
svg_intersection.append("line")
    .attr("x1", 430)
    .attr("y1", ((h_intersection/2) + 50))
    .attr("x2", 220)
    .attr("y2", ((h_intersection/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// left vertical line
svg_intersection.append("line")
    .attr("x1", 220)
    .attr("y1", ((h_intersection/2) + 50))
    .attr("x2", 220)
    .attr("y2", ((h_intersection/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// box of circles set 1 intersected with set 2
//
// top line
svg_intersection.append("line")
    .attr("x1", 450)
    .attr("y1", ((h_intersection/2) - 50))
    .attr("x2", 590)
    .attr("y2", ((h_intersection/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// right vertical line
svg_intersection.append("line")
    .attr("x1", 590)
    .attr("y1", ((h_intersection/2) - 50))
    .attr("x2", 590)
    .attr("y2", ((h_intersection/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// bottom line
svg_intersection.append("line")
    .attr("x1", 590)
    .attr("y1", ((h_intersection/2) + 50))
    .attr("x2", 450)
    .attr("y2", ((h_intersection/2) + 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

// left vertical line
svg_intersection.append("line")
    .attr("x1", 450)
    .attr("y1", ((h_intersection/2) + 50))
    .attr("x2", 450)
    .attr("y2", ((h_intersection/2) - 50))
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 3);

var circle_intersection_set_1 = svg_intersection.selectAll(".circle_intersection_set_1")
    .data(circle_intersection_dataset_1)
    .enter()
  .append("circle");

circle_intersection_set_1.attr("cx", function(d, i) {
		return (i*60)+30;
	})
	.attr("cy", h_intersection/2)
	.attr("r", function(d) {
		return d;
	})
	.attr("fill", "#f5ffde")
	.attr("stroke", "#759e16")
	.attr("stroke-width", 3)
	.attr("stroke-dasharray", "12 3")
	.attr("class", "circle_intersection_set_1");

svg_intersection.selectAll(".text_intersection_set_1")
    .data(circle_intersection_dataset_1)
    .enter()
  .append("text")
    .text(function(d) {
	    return d;
    })
    .attr("text-anchor", "middle")
    .attr("x", function(d, i) {
		return (i*60)+30;
	})
    .attr("y", (h_intersection/2)+5)
    .attr("font-family", "sans-serif")
    .attr("font-size", "18px")
    .attr("font-weight", "900")
    .attr("fill", "#3a3a36")
    .attr("class", "text_intersection_set_1");
    

var circle_intersection_set_2 = svg_intersection.selectAll(".circle_intersection_set_2")
    .data(circle_intersection_dataset_2)
    .enter()
  .append("circle");

circle_intersection_set_2.attr("cx", function(d, i) {
		return (i*70) + 250;
	})
	.attr("cy", h_intersection/2)
	.attr("r", function(d) {
		return d;
	})
	.attr("fill", "#f5ffde")
	.attr("stroke", "#759e16")
	.attr("stroke-width", 3)
	.attr("stroke-dasharray", "12 3")
	.attr("class", "circle_intersection_set_2");

svg_intersection.selectAll(".text_intersection_set_2")
    .data(circle_intersection_dataset_2)
    .enter()
  .append("text")
    .text(function(d) {
	    return d;
    })
    .attr("text-anchor", "middle")
    .attr("x", function(d, i) {
		return (i*70)+250;
	})
    .attr("y", (h_intersection/2)+5)
    .attr("font-family", "sans-serif")
    .attr("font-size", "18px")
    .attr("font-weight", "900")
    .attr("fill", "#3a3a36")
    .attr("class", "text_intersection_set_2");

d3.select("#intersection_button")
    .on("click", function() {
	    var intersection_dataset = [15, 25];
	    var circle_intersection_set = svg_intersection.selectAll(".intersection_circles")
	        .data(intersection_dataset)
	        .enter()
	      .append("circle")
	        .transition()
	        .duration(2000)
	        .on("start", function() {
			d3.select(this)
			    .attr("fill", "#3a3a36")
			    .attr("r", 3);
		})
	        .attr("cx", function(d, i) {
	    		return 450+(i*70)+30;
	    	})
	    	.attr("cy", h_intersection/2)
	        .on("end", function() {
			d3.select(this)
			    .transition()
			    .duration(1000)
			    .ease(d3.easeLinear)
	    		    .attr("fill", "#f5ffde")
	    		    .attr("stroke", "#759e16")
	    		    .attr("stroke-width", 3)
			    .attr("stroke-dasharray", "12 3")
	    		    .attr("r", function(d) {
	    			return d;
	    		    })

		})
	        .attr("class", "intersection_circles");

	    svg_intersection.selectAll(".intersection_text")
	        .data(intersection_dataset)
	        .enter()
	      .append("text")
	        .transition()
	        .duration(2000)
	        .on("start", function() {
			d3.select(this)
	        	    .attr("font-size", "1px")
		})
	        .text(function(d) {
	    	    return d;
	        })
	        .attr("text-anchor", "middle")
	        .attr("x", function(d, i) {
	    		return 450+(i*70)+30;
	    	})
	        .attr("y", (h_intersection/2)+5)
	        .attr("font-family", "sans-serif")
	        .attr("fill", "#3a3a36")
	        .on("end", function() {
			d3.select(this)
			    .transition()
			    .duration(1000)
			    .ease(d3.easeLinear)
			    .attr("font-size","18px")
			    .attr("font-weight", "900");
		})
	        .attr("class", "intersection_text");

    });







// Basis Set B3 that is a subset of B1 intersect B2
var w_svg_basis_set_3 = 960;
var h_svg_basis_set_3 = 640;

var svg_basis_set_3 = d3.select("#basis_set_3")
  .append("svg")
    .attr("viewBox", "0 0 " + w_svg_basis_set_3 + " " + h_svg_basis_set_3);

// top line of outer square
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(2/10))
    .attr("y1", h_svg_basis_set_3*(0.5/10))
    .attr("x2", w_svg_basis_set_3*(8/10))
    .attr("y2", h_svg_basis_set_3*(0.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// right vertical line of outer square
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(8/10))
    .attr("y1", h_svg_basis_set_3*(0.5/10))
    .attr("x2", w_svg_basis_set_3*(8/10))
    .attr("y2", h_svg_basis_set_3*(9.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// bottom line of outer square
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(8/10))
    .attr("y1", h_svg_basis_set_3*(9.5/10))
    .attr("x2", w_svg_basis_set_3*(2/10))
    .attr("y2", h_svg_basis_set_3*(9.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// left vertical line of outer square
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(2/10))
    .attr("y1", h_svg_basis_set_3*(9.5/10))
    .attr("x2", w_svg_basis_set_3*(2/10))
    .attr("y2", h_svg_basis_set_3*(0.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// B1 basis set: top right square
svg_basis_set_3.append("text")
    .text("B")
    .attr("x", w_svg_basis_set_3*(6/10) + 50)
    .attr("y", h_svg_basis_set_3*(3.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
  .append("tspan")
    .text("1")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
    .attr("dx", ".1rem")
    .attr("dy", ".8rem");


// left vertical line of top right square B1
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(4/10))
    .attr("y1", h_svg_basis_set_3*(0.5/10))
    .attr("x2", w_svg_basis_set_3*(4/10))
    .attr("y2", h_svg_basis_set_3*(6.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// bottom line of top right square B1
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(4/10))
    .attr("y1", h_svg_basis_set_3*(6.5/10))
    .attr("x2", w_svg_basis_set_3*(8/10))
    .attr("y2", h_svg_basis_set_3*(6.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// B2 basis set: bottom left square
svg_basis_set_3.append("text")
    .text("B")
    .attr("x", w_svg_basis_set_3*(3.5/10) - 50)
    .attr("y", h_svg_basis_set_3*(6.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
  .append("tspan")
    .text("2")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
    .attr("dx", ".1rem")
    .attr("dy", ".8rem");

// right vertical line of bottom left square B2
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(6/10))
    .attr("y1", h_svg_basis_set_3*(9.5/10))
    .attr("x2", w_svg_basis_set_3*(6/10))
    .attr("y2", h_svg_basis_set_3*(3.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// top line of bottom left square B2
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(6/10))
    .attr("y1", h_svg_basis_set_3*(3.5/10))
    .attr("x2", w_svg_basis_set_3*(2/10))
    .attr("y2", h_svg_basis_set_3*(3.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// B3 basis set: middle square
svg_basis_set_3.append("text")
    .text("B")
    .attr("x", w_svg_basis_set_3*(4.6/10))
    .attr("y", h_svg_basis_set_3*(4.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
  .append("tspan")
    .text("3")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
    .attr("dx", ".1rem")
    .attr("dy", ".8rem");

// top line of middle square B3
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(4.5/10))
    .attr("y1", h_svg_basis_set_3*(4/10))
    .attr("x2", w_svg_basis_set_3*(5.5/10))
    .attr("y2", h_svg_basis_set_3*(4/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// right vertical line of middle square B3
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(5.5/10))
    .attr("y1", h_svg_basis_set_3*(4/10))
    .attr("x2", w_svg_basis_set_3*(5.5/10))
    .attr("y2", h_svg_basis_set_3*(5.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// bottom line of middle square B3
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(5.5/10))
    .attr("y1", h_svg_basis_set_3*(5.5/10))
    .attr("x2", w_svg_basis_set_3*(4.5/10))
    .attr("y2", h_svg_basis_set_3*(5.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// left vertical line of middle square B3
svg_basis_set_3.append("line")
    .attr("x1", w_svg_basis_set_3*(4.5/10))
    .attr("y1", h_svg_basis_set_3*(5.5/10))
    .attr("x2", w_svg_basis_set_3*(4.5/10))
    .attr("y2", h_svg_basis_set_3*(4/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// point z in the intersection of B1 and B2
svg_basis_set_3.append("text")
    .text("z")
    .attr("x", w_svg_basis_set_3*(5.25/10))
    .attr("y", h_svg_basis_set_3*(5.1/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");
    
svg_basis_set_3.append("circle")
    .attr("cx", w_svg_basis_set_3*(5.1/10))
    .attr("cy", h_svg_basis_set_3*(5.1/10))
    .attr("r", 10)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 1)
    .attr("fill", "#3a3a36");









// Basis B contained within open set U
var w_svg_basis_in_open_set = 960;
var h_svg_basis_in_open_set = 640;

var svg_basis_in_open_set = d3.select("#basis_in_open_set")
  .append("svg")
    .attr("viewBox", 
	    "0 0 " + w_svg_basis_in_open_set + " " + h_svg_basis_in_open_set);

// space X
svg_basis_in_open_set.append("text")
    .text("X")
    .attr("x", w_svg_basis_in_open_set*(2.5/10))
    .attr("y", h_svg_basis_in_open_set*(1.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "60px")
    .attr("fill", "#3a3a36");

// top line of outer square space X
svg_basis_in_open_set.append("line")
    .attr("x1", w_svg_basis_in_open_set*(2/10))
    .attr("y1", h_svg_basis_in_open_set*(0.5/10))
    .attr("x2", w_svg_basis_in_open_set*(8/10))
    .attr("y2", h_svg_basis_in_open_set*(0.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// right vertical line of outer square space X
svg_basis_in_open_set.append("line")
    .attr("x1", w_svg_basis_in_open_set*(8/10))
    .attr("y1", h_svg_basis_in_open_set*(0.5/10))
    .attr("x2", w_svg_basis_in_open_set*(8/10))
    .attr("y2", h_svg_basis_in_open_set*(9.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// bottom line of outer square space X
svg_basis_in_open_set.append("line")
    .attr("x1", w_svg_basis_in_open_set*(8/10))
    .attr("y1", h_svg_basis_in_open_set*(9.5/10))
    .attr("x2", w_svg_basis_in_open_set*(2/10))
    .attr("y2", h_svg_basis_in_open_set*(9.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// left vertical line of outer square space X
svg_basis_in_open_set.append("line")
    .attr("x1", w_svg_basis_in_open_set*(2/10))
    .attr("y1", h_svg_basis_in_open_set*(9.5/10))
    .attr("x2", w_svg_basis_in_open_set*(2/10))
    .attr("y2", h_svg_basis_in_open_set*(0.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// open set U in space X
svg_basis_in_open_set.append("text")
    .text("U")
    .attr("x", w_svg_basis_in_open_set*(4.2/10))
    .attr("y", h_svg_basis_in_open_set*(3.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "50px")
    .attr("fill", "#3a3a36");

svg_basis_in_open_set.append("circle")
    .attr("cx", w_svg_basis_in_open_set*(5.5/10))
    .attr("cy", h_svg_basis_in_open_set*(5.5/10))
    .attr("r", 215)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 5)
    .attr("stroke-dasharray", "12 3")
    .attr("fill", "none");

// basis element B in open set U
svg_basis_in_open_set.append("text")
    .text("B")
    .attr("x", w_svg_basis_in_open_set*(6.5/10))
    .attr("y", h_svg_basis_in_open_set*(4.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "50px")
    .attr("fill", "#3a3a36");

// top line of basis element
svg_basis_in_open_set.append("line")
    .attr("x1", w_svg_basis_in_open_set*(5/10))
    .attr("y1", h_svg_basis_in_open_set*(3.5/10))
    .attr("x2", w_svg_basis_in_open_set*(7/10))
    .attr("y2", h_svg_basis_in_open_set*(3.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// right vertical line of basis element
svg_basis_in_open_set.append("line")
    .attr("x1", w_svg_basis_in_open_set*(7/10))
    .attr("y1", h_svg_basis_in_open_set*(3.5/10))
    .attr("x2", w_svg_basis_in_open_set*(7/10))
    .attr("y2", h_svg_basis_in_open_set*(6.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// bottom line of basis element
svg_basis_in_open_set.append("line")
    .attr("x1", w_svg_basis_in_open_set*(7/10))
    .attr("y1", h_svg_basis_in_open_set*(6.5/10))
    .attr("x2", w_svg_basis_in_open_set*(5/10))
    .attr("y2", h_svg_basis_in_open_set*(6.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// left vertical line of basis element
svg_basis_in_open_set.append("line")
    .attr("x1", w_svg_basis_in_open_set*(5/10))
    .attr("y1", h_svg_basis_in_open_set*(6.5/10))
    .attr("x2", w_svg_basis_in_open_set*(5/10))
    .attr("y2", h_svg_basis_in_open_set*(3.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// little z element of open set U
svg_basis_in_open_set.append("text")
    .text("z")
    .attr("x", w_svg_basis_in_open_set*(5.65/10))
    .attr("y", h_svg_basis_in_open_set*(5.7/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

svg_basis_in_open_set.append("circle")
    .attr("cx", w_svg_basis_in_open_set*(5.5/10))
    .attr("cy", h_svg_basis_in_open_set*(5.5/10))
    .attr("r", 10)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 1)
    .attr("fill", "#3a3a36");





// Distance between a point y in open set U and the boundary of U
//
//
//
var w_svg_boundary_distance = 960;
var h_svg_boundary_distance = 640;

var svg_boundary_distance = d3.select("#boundary_distance")
  .append("svg")
    .attr("viewBox", 
    	"0 0 " + w_svg_boundary_distance + " " + h_svg_boundary_distance);

// open set U
svg_boundary_distance.append("text")
    .text("U")
    .attr("x", w_svg_boundary_distance*(2.5/10))
    .attr("y", h_svg_boundary_distance*(1.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "60px")
    .attr("fill", "#3a3a36");

// top line of outer square open U
svg_boundary_distance.append("line")
    .attr("x1", w_svg_boundary_distance*(2/10))
    .attr("y1", h_svg_boundary_distance*(0.5/10))
    .attr("x2", w_svg_boundary_distance*(8/10))
    .attr("y2", h_svg_boundary_distance*(0.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// right vertical line of outer square open U
svg_boundary_distance.append("line")
    .attr("x1", w_svg_boundary_distance*(8/10))
    .attr("y1", h_svg_boundary_distance*(0.5/10))
    .attr("x2", w_svg_boundary_distance*(8/10))
    .attr("y2", h_svg_boundary_distance*(9.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// bottom line of outer square open U
svg_boundary_distance.append("line")
    .attr("x1", w_svg_boundary_distance*(8/10))
    .attr("y1", h_svg_boundary_distance*(9.5/10))
    .attr("x2", w_svg_boundary_distance*(2/10))
    .attr("y2", h_svg_boundary_distance*(9.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// left vertical line of outer square open U
svg_boundary_distance.append("line")
    .attr("x1", w_svg_boundary_distance*(2/10))
    .attr("y1", h_svg_boundary_distance*(9.5/10))
    .attr("x2", w_svg_boundary_distance*(2/10))
    .attr("y2", h_svg_boundary_distance*(0.5/10))
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// basis element B_d(x) in open U
svg_boundary_distance.append("text")
    .text("B")
    .attr("x", w_svg_boundary_distance*(4.2/10))
    .attr("y", h_svg_boundary_distance*(3.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "50px")
    .attr("fill", "#3a3a36")
  .append("tspan")
    .text("d")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
    .attr("dx", ".1rem")
    .attr("dy", ".8rem");

svg_boundary_distance.append("text")
    .text("(x)")
    .attr("x", w_svg_boundary_distance*(4.8/10))
    .attr("y", h_svg_boundary_distance*(3.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "50px")
    .attr("fill", "#3a3a36");

svg_boundary_distance.append("circle")
    .attr("cx", w_svg_boundary_distance*(5.5/10))
    .attr("cy", h_svg_boundary_distance*(5.5/10))
    .attr("r", 215)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 5)
    .attr("stroke-dasharray", "12 3")
    .attr("fill", "none");

// little x center point of basis element B_d(x)
svg_boundary_distance.append("text")
    .text("x")
    .attr("x", w_svg_boundary_distance*(5.65/10))
    .attr("y", h_svg_boundary_distance*(5.7/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

svg_boundary_distance.append("circle")
    .attr("cx", w_svg_boundary_distance*(5.5/10))
    .attr("cy", h_svg_boundary_distance*(5.5/10))
    .attr("r", 10)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 1)
    .attr("fill", "#3a3a36");

// little y element of basis element B_d(x)
svg_boundary_distance.append("text")
    .text("y")
    .attr("x", w_svg_boundary_distance*(6.85/10))
    .attr("y", h_svg_boundary_distance*(4.35/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

svg_boundary_distance.append("circle")
    .attr("cx", w_svg_boundary_distance*(6.7/10))
    .attr("cy", h_svg_boundary_distance*(4.4/10))
    .attr("r", 10)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 1)
    .attr("fill", "#3a3a36");

// Epsilon Ball for distance between point y in U and the boundary of U
//
//
//
var w_svg_epsilon_ball = 960;
var h_svg_epsilon_ball = 640;

var svg_epsilon_ball = d3.select("#epsilon_ball")
  .append("svg")
    .attr("viewBox", 
    	"0 0 " + w_svg_epsilon_ball + " " + h_svg_epsilon_ball);

// basis element B_d(x) in open U
svg_epsilon_ball.append("text")
    .text("B")
    .attr("x", w_svg_epsilon_ball*(3.2/10))
    .attr("y", h_svg_epsilon_ball*(2.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "50px")
    .attr("fill", "#3a3a36")
  .append("tspan")
    .text("d")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
    .attr("dx", ".1rem")
    .attr("dy", ".8rem");

svg_epsilon_ball.append("text")
    .text("(x)")
    .attr("x", w_svg_epsilon_ball*(3.8/10))
    .attr("y", h_svg_epsilon_ball*(2.5/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "50px")
    .attr("fill", "#3a3a36");

svg_epsilon_ball.append("circle")
    .attr("cx", w_svg_epsilon_ball*(5/10))
    .attr("cy", h_svg_epsilon_ball*(5/10))
    .attr("r", 300)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 5)
    .attr("stroke-dasharray", "12 3")
    .attr("fill", "none");

// little x center point of basis element B_d(x)
svg_epsilon_ball.append("text")
    .text("x")
    .attr("x", w_svg_epsilon_ball*(5.2/10))
    .attr("y", h_svg_epsilon_ball*(5.3/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

var x_horizontal = 5/10;
var x_vertical = 5/10;

svg_epsilon_ball.append("circle")
    .attr("cx", w_svg_epsilon_ball*(x_horizontal))
    .attr("cy", h_svg_epsilon_ball*(x_vertical))
    .attr("r", 10)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 1)
    .attr("fill", "#3a3a36");

// little y element of basis element B_d(x)
svg_epsilon_ball.append("text")
    .text("y")
    .attr("x", w_svg_epsilon_ball*(6.85/10))
    .attr("y", h_svg_epsilon_ball*(4.7/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

var y_horizontal = 6.7/10;
var y_vertical = 4.4/10;

svg_epsilon_ball.append("circle")
    .attr("cx", w_svg_epsilon_ball*(y_horizontal))
    .attr("cy", h_svg_epsilon_ball*(y_vertical))
    .attr("r", 10)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 1)
    .attr("fill", "#3a3a36");

// Finding the distance from x to the boundary of B_d(x)
//
// right triangle with hypotenuse between x and y
var vertical_difference = Math.abs(
	h_svg_epsilon_ball*y_vertical - h_svg_epsilon_ball*x_vertical
);
var horizontal_difference = Math.abs(
	w_svg_epsilon_ball*y_horizontal - w_svg_epsilon_ball*x_horizontal
);
var euclidean_difference = Math.sqrt(
	(vertical_difference)**2 + (horizontal_difference)**2
);
// change in horizontal from x to boundary of B_d(x)
// along the line running through x and y
var x_boundary_horizontal = (300/euclidean_difference)*horizontal_difference;
var x_boundary_vertical = (300/euclidean_difference)*vertical_difference;

svg_epsilon_ball.append("circle")
    .attr("cx", w_svg_epsilon_ball*x_horizontal + x_boundary_horizontal)
    .attr("cy", h_svg_epsilon_ball*x_vertical - x_boundary_vertical)
    .attr("r", 10)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 1)
    .attr("fill", "#3a3a36");

// line between point x and the boundary, through point y
svg_epsilon_ball.append("line")
    .attr("x1", w_svg_epsilon_ball*x_horizontal)
    .attr("y1", h_svg_epsilon_ball*x_vertical)
    .attr("x2", w_svg_epsilon_ball*x_horizontal + x_boundary_horizontal)
    .attr("y2", h_svg_epsilon_ball*x_vertical - x_boundary_vertical)
    .attr("stroke", "#3a3a36")
    .attr("stroke-dasharray", "12 3")
    .attr("stroke-width", 5);

// drawing epsilon ball, B_e(y), of radius e around center y
svg_epsilon_ball.append("circle")
    .attr("cx", w_svg_epsilon_ball*(y_horizontal))
    .attr("cy", h_svg_epsilon_ball*(y_vertical))
    .attr("r", 115)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 5)
    .attr("stroke-dasharray", "12 3")
    .attr("fill", "none");

svg_epsilon_ball.append("text")
    .text("B")
    .attr("x", w_svg_epsilon_ball*(6/10))
    .attr("y", h_svg_epsilon_ball*(3.6/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "50px")
    .attr("fill", "#3a3a36")
  .append("tspan")
    .text("e")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36")
    .attr("dx", ".1rem")
    .attr("dy", ".8rem");

svg_epsilon_ball.append("text")
    .text("(y)")
    .attr("x", w_svg_epsilon_ball*(6.6/10))
    .attr("y", h_svg_epsilon_ball*(3.6/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "50px")
    .attr("fill", "#3a3a36");

// little z element of epsilon ball B_{e}(y)
svg_epsilon_ball.append("text")
    .text("z")
    .attr("x", w_svg_epsilon_ball*(7.65/10))
    .attr("y", h_svg_epsilon_ball*(4.7/10))
    .attr("font-family", "sans-serif")
    .attr("font-size", "30px")
    .attr("fill", "#3a3a36");

svg_epsilon_ball.append("circle")
    .attr("cx", w_svg_epsilon_ball*(7.5/10))
    .attr("cy", h_svg_epsilon_ball*(4.5/10))
    .attr("r", 10)
    .attr("stroke", "#3a3a36")
    .attr("stroke-width", 1)
    .attr("fill", "#3a3a36");
