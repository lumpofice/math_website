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











// One-dimensional real line filled with interval of a specified distance ----
//
//
// ---------------------------------------------------------------------------
// 4 intervals ---------------------------------------------------------------
var w_svg_for_line = 960;
var h_svg_for_line = 150;

var svg_for_line_0 = d3.select("#math0")
  .append("svg")
    .attr("viewBox", "0 0 " + w_svg_for_line + " " + h_svg_for_line);

svg_for_line_0.append("line")
    .style("stroke", "#759e16")
    .style("stroke-width", 5)
    .attr("x1", 0)
    .attr("y1", h_svg_for_line/2)
    .attr("x2", w_svg_for_line)
    .attr("y2", h_svg_for_line/2);


// Outer parentheses spanning the entire line
//
//
var parenthesis_open_0 = d3.path();
var parenthesis_close_0 = d3.path();

// Distance of right-most pixel of vertex of parenthesis to i is 18px 
// when convexity is 40
var convexity = 40;

var drawn_convexity = 18; // x distance from vertex to endpoints of parentheses
var vertical_distance = 90;

// The left-most pixel of the vertex of the parenthesis to i is 23px 
// when parenthesis_width is 5
var parenthesis_width = 5;

// Given n is "number of intervals", increment is 
// (960 - [ n*( (2*parenthesis_width) + (2*drawn_convexity) ) ] )/n
var increment_0 = 194; // x distance from endpoints of open parenthesis
// to endpoints of closed parenthesis

var distance_0 = increment_0 + (2*drawn_convexity) + (2*parenthesis_width);  

for (let i = 23; i < 960; i = i + distance_0) {
	parenthesis_open_0.moveTo(
		i, 
		(h_svg_for_line/2) + (vertical_distance/2)
	);
	parenthesis_open_0.quadraticCurveTo(
		i - convexity, 
		h_svg_for_line/2, 
		i, 
		(h_svg_for_line/2) - (vertical_distance/2)
	);
	
	svg_for_line_0.append("path")
	    .style("stroke", "#6b4691")
	    .style("stroke-width", parenthesis_width)
	    .attr("d", parenthesis_open_0)
	    .attr("fill", "none");
	
	parenthesis_close_0.moveTo(
		i + increment_0, 
		(h_svg_for_line/2) + (vertical_distance/2)
	);
	parenthesis_close_0.quadraticCurveTo(
		i + increment_0 + convexity, 
		h_svg_for_line/2,
		i + increment_0,
		(h_svg_for_line/2) - (vertical_distance/2)
	);

	svg_for_line_0.append("path")
	    .style("stroke", "#6b4691")
	    .style("stroke-width", parenthesis_width)
	    .attr("d", parenthesis_close_0)
	    .attr("fill", "none");
}


// Middle parentheses spanning located between the outer parentheses
// spanning the entire line
//
//
var parenthesis_middles_open_0 = d3.path();
var parenthesis_middles_close_0 = d3.path();


for (var i = 23 + distance_0/2; 
	i < 960 - distance_0; 
	i = i + distance_0) {
	parenthesis_middles_open_0.moveTo(
		i, 
		(h_svg_for_line/2) + (vertical_distance/3)
	);
	parenthesis_middles_open_0.quadraticCurveTo(
		i - convexity, 
		h_svg_for_line/2, 
		i, 
		(h_svg_for_line/2) - (vertical_distance/3)
	);
	
	svg_for_line_0.append("path")
	    .style("stroke", "#3a3a36")
	    .style("stroke-width", parenthesis_width)
	    .style("stroke-dasharray", "12 3")
	    .attr("d", parenthesis_middles_open_0)
	    .attr("fill", "none");
}

for (var i = 23 + distance_0 + distance_0/2; 
	i < 960; 
	i = i + distance_0) {
	parenthesis_middles_close_0.moveTo(
		i - 2*(drawn_convexity + parenthesis_width), 
		(h_svg_for_line/2) + (vertical_distance/3)
	);
	parenthesis_middles_close_0.quadraticCurveTo(
		i - 2*(drawn_convexity + parenthesis_width) + convexity, 
		h_svg_for_line/2,
		i -2*(drawn_convexity + parenthesis_width),
		(h_svg_for_line/2) - (vertical_distance/3)
	);

	svg_for_line_0.append("path")
	    .style("stroke", "#3a3a36")
	    .style("stroke-width", parenthesis_width)
	    .style("stroke-dasharray", "12 3")
	    .attr("d", parenthesis_middles_close_0)
	    .attr("fill", "none");
}



// ---------------------------------------------------------------------------
// 8 intervals ---------------------------------------------------------------
var svg_for_line_1 = d3.select("#math1")
  .append("svg")
    .attr("viewBox", "0 0 " + w_svg_for_line + " " + h_svg_for_line);

svg_for_line_1.append("line")
    .style("stroke", "#759e16")
    .style("stroke-width", 5)
    .attr("x1", 0)
    .attr("y1", h_svg_for_line/2)
    .attr("x2", w_svg_for_line)
    .attr("y2", h_svg_for_line/2);


// Outer parentheses spanning the entire line
//
//
var parenthesis_open_1 = d3.path();
var parenthesis_close_1 = d3.path();

// Distance of right-most pixel of vertex of parenthesis to i is 18px 
// when convexity is 40

// The left-most pixel of the vertex of the parenthesis to i is 23px 
// when parenthesis_width is 5

// Given n is "number of intervals", increment is 
// (960 - [ n*( (2*parenthesis_width) + (2*drawn_convexity) ) ] )/n
var increment_1 = 74; // x distance from endpoints of open parenthesis
// to endpoints of closed parenthesis

var distance_1 = increment_1 + (2*drawn_convexity) + (2*parenthesis_width);  

for (let i = 23; i < 960; i = i + distance_1) {
	parenthesis_open_1.moveTo(
		i, 
		(h_svg_for_line/2) + (vertical_distance/2)
	);
	parenthesis_open_1.quadraticCurveTo(
		i - convexity, 
		h_svg_for_line/2, 
		i, 
		(h_svg_for_line/2) - (vertical_distance/2)
	);
	
	svg_for_line_1.append("path")
	    .style("stroke", "#6b4691")
	    .style("stroke-width", parenthesis_width)
	    .attr("d", parenthesis_open_1)
	    .attr("fill", "none");

	parenthesis_close_1.moveTo(
		i + increment_1, 
		(h_svg_for_line/2) + (vertical_distance/2)
	);
	parenthesis_close_1.quadraticCurveTo(
		i + increment_1 + convexity, 
		h_svg_for_line/2,
		i + increment_1,
		(h_svg_for_line/2) - (vertical_distance/2)
	);

	svg_for_line_1.append("path")
	    .style("stroke", "#6b4691")
	    .style("stroke-width", parenthesis_width)
	    .attr("d", parenthesis_close_1)
	    .attr("fill", "none");
	
}


// Middle parentheses spanning located between the outer parentheses
// spanning the entire line
//
//
var parenthesis_middles_open_1 = d3.path();
var parenthesis_middles_close_1 = d3.path();

for (var i = 23 + distance_1/2; 
	i < 960 - distance_1; 
	i = i + distance_1) {
	parenthesis_middles_open_1.moveTo(
		i, 
		(h_svg_for_line/2) + (vertical_distance/3)
	);
	parenthesis_middles_open_1.quadraticCurveTo(
		i - convexity, 
		h_svg_for_line/2, 
		i, 
		(h_svg_for_line/2) - (vertical_distance/3)
	);
	
	svg_for_line_1.append("path")
	    .style("stroke", "#3a3a36")
	    .style("stroke-width", parenthesis_width)
	    .style("stroke-dasharray", "12 3")
	    .attr("d", parenthesis_middles_open_1)
	    .attr("fill", "none");
}	

for (var i = 23 + distance_1 + distance_1/2; 
	i < 960; 
	i = i + distance_1) {
	parenthesis_middles_close_1.moveTo(
		i - 2*(drawn_convexity + parenthesis_width), 
		(h_svg_for_line/2) + (vertical_distance/3)
	);
	parenthesis_middles_close_1.quadraticCurveTo(
		i - 2*(drawn_convexity + parenthesis_width) + convexity, 
		h_svg_for_line/2,
		i -2*(drawn_convexity + parenthesis_width),
		(h_svg_for_line/2) - (vertical_distance/3)
	);

	svg_for_line_1.append("path")
	    .style("stroke", "#3a3a36")
	    .style("stroke-width", parenthesis_width)
	    .style("stroke-dasharray", "12 3")
	    .attr("d", parenthesis_middles_close_1)
	    .attr("fill", "none");
}



// ---------------------------------------------------------------------------
// 12 intervals ---------------------------------------------------------------
var svg_for_line_2 = d3.select("#math2")
  .append("svg")
    .attr("viewBox", "0 0 " + w_svg_for_line + " " + h_svg_for_line);

svg_for_line_2.append("line")
    .style("stroke", "#759e16")
    .style("stroke-width", 5)
    .attr("x1", 0)
    .attr("y1", h_svg_for_line/2)
    .attr("x2", w_svg_for_line)
    .attr("y2", h_svg_for_line/2);


// Outer parentheses spanning the entire line
//
//
var parenthesis_open_2 = d3.path();
var parenthesis_close_2 = d3.path();

// Distance of right-most pixel of vertex of parenthesis to i is 18px 
// when convexity is 40

// The left-most pixel of the vertex of the parenthesis to i is 23px 
// when parenthesis_width is 5

// Given n is "number of intervals", increment is 
// (960 - [ n*( (2*parenthesis_width) + (2*drawn_convexity) ) ] )/n
var increment_2 = 34;

var distance_2 = increment_2 + (2*drawn_convexity) + (2*parenthesis_width);  

for (let i = 23; i < 960; i = i + distance_2) {
	parenthesis_open_2.moveTo(
		i, 
		(h_svg_for_line/2) + (vertical_distance/2)
	);
	parenthesis_open_2.quadraticCurveTo(
		i - convexity, 
		h_svg_for_line/2, 
		i, 
		(h_svg_for_line/2) - (vertical_distance/2)
	);
	
	svg_for_line_2.append("path")
	    .style("stroke", "#6b4691")
	    .style("stroke-width", parenthesis_width)
	    .attr("d", parenthesis_open_2)
	    .attr("fill", "none");

	parenthesis_close_2.moveTo(
		i + increment_2, 
		(h_svg_for_line/2) + (vertical_distance/2)
	);
	parenthesis_close_2.quadraticCurveTo(
		i + increment_2 + convexity, 
		h_svg_for_line/2,
		i + increment_2,
		(h_svg_for_line/2) - (vertical_distance/2)
	);

	svg_for_line_2.append("path")
	    .style("stroke", "#6b4691")
	    .style("stroke-width", parenthesis_width)
	    .attr("d", parenthesis_close_2)
	    .attr("fill", "none");
	
}


// Middle parentheses spanning located between the outer parentheses
// spanning the entire line
//
//
var parenthesis_middles_open_2 = d3.path();
var parenthesis_middles_close_2 = d3.path();

for (var i = 23 + distance_2/2; 
	i < 960 - distance_2; 
	i = i + distance_2) {
	parenthesis_middles_open_2.moveTo(
		i, 
		(h_svg_for_line/2) + (vertical_distance/3)
	);
	parenthesis_middles_open_2.quadraticCurveTo(
		i - convexity, 
		h_svg_for_line/2, 
		i, 
		(h_svg_for_line/2) - (vertical_distance/3)
	);
	
	svg_for_line_2.append("path")
	    .style("stroke", "#3a3a36")
	    .style("stroke-width", parenthesis_width)
	    .style("stroke-dasharray", "12 3")
	    .attr("d", parenthesis_middles_open_2)
	    .attr("fill", "none");
}	

for (var i = 23 + distance_2 + distance_2/2; 
	i < 960; 
	i = i + distance_2) {
	parenthesis_middles_close_2.moveTo(
		i - 2*(drawn_convexity + parenthesis_width), 
		(h_svg_for_line/2) + (vertical_distance/3)
	);
	parenthesis_middles_close_2.quadraticCurveTo(
		i - 2*(drawn_convexity + parenthesis_width) + convexity, 
		h_svg_for_line/2,
		i -2*(drawn_convexity + parenthesis_width),
		(h_svg_for_line/2) - (vertical_distance/3)
	);

	svg_for_line_2.append("path")
	    .style("stroke", "#3a3a36")
	    .style("stroke-width", parenthesis_width)
	    .style("stroke-dasharray", "12 3")
	    .attr("d", parenthesis_middles_close_2)
	    .attr("fill", "none");
}





// Ball of radius delta inside of ball of radius epsilon ---------------------
//
//
// ---------------------------------------------------------------------------
var width_epsilon_delta_svg = 960;
var height_epsilon_delta_svg = 600;

var epsilon_ball_radius = 290;
var delta_ball_radius = 120;

var epsilon_delta_svg = d3.select("#ball0")
  .append("svg")
    .attr("viewBox", 
	    "0 0 " 
	    + width_epsilon_delta_svg 
	    + " " 
	    + height_epsilon_delta_svg);

// The epsilon ball ----------------------------------------------------------
epsilon_delta_svg.append("circle")
    .style("stroke", "#6b4691")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3")
    .style("fill", "#6b4691")
    .attr("cx", width_epsilon_delta_svg/2)
    .attr("cy", height_epsilon_delta_svg/2)
    .attr("r", epsilon_ball_radius);

// The delta ball ------------------------------------------------------------
epsilon_delta_svg.append("circle")
    .style("stroke", "#6b4691")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3")
    .style("fill", "#f5ffde")
    .attr("cx", (width_epsilon_delta_svg/2) - 110)
    .attr("cy", (height_epsilon_delta_svg/2) - 90)
    .attr("r", delta_ball_radius);



// Radius line in esilon ball ------------------------------------------------
// We need a line extending from the middle of the ball
// (width_epsilon_delta_svg/2, height_epsilon_delta_svg/2)
// to a point on the circle enclosing the ball.
// (width_epsilon_delta_svg/2 + x, height_epsilon_delta_svg/2 + x)
// We establish this the easy way: Pythagorean Theorem with legs
// of equal length.
// So, we have that length as x = sqrt( ([epsilon_ball_radius]^2)/2 )
epsilon_delta_svg.append("line")
    .attr("x1", width_epsilon_delta_svg/2)
    .attr("y1", height_epsilon_delta_svg/2)
    .attr("x2", 
	    (width_epsilon_delta_svg/2) 
	    + Math.sqrt((epsilon_ball_radius**2)/2))
    .attr("y2", 
	    (height_epsilon_delta_svg/2)
	    + Math.sqrt((epsilon_ball_radius**2)/2))
    .style("stroke", "#f5ffde")
    .style("stroke-width", 5);

// Radius epsilon symbol ----------------------------------------------------- 
epsilon_delta_svg.append("text")
    .text("\u03B5")
    .attr("x", width_epsilon_delta_svg/2 + 115)
    .attr("y", height_epsilon_delta_svg/2 + 110)
    .attr("font-family", "sans-serif")
    .attr("font-size", "42px")
    .attr("fill", "#f5ffde");
    

// Radius line in delta ball -------------------------------------------------
// We need a line extending from the middle of the ball
// (width_epsilon_delta_svg/2 - 110, height_epsilon_delta_svg/2 - 90)
// to a point on the circle enclosing the ball.
// (width_epsilon_delta_svg/2 - 110 + x, height_epsilon_delta_svg/2 - 90 + x)
// We establish this the easy way: Pythagorean Theorem with legs
// of equal length.
// So, we have that length as x = sqrt( ([delta_ball_radius]^2)/2 )
epsilon_delta_svg.append("line")
    .attr("x1", width_epsilon_delta_svg/2 - 110)
    .attr("y1", height_epsilon_delta_svg/2 - 90)
    .attr("x2", 
	    (width_epsilon_delta_svg/2 - 110) 
	    - Math.sqrt((delta_ball_radius**2)/2))
    .attr("y2", 
	    (height_epsilon_delta_svg/2 - 90)
	    + Math.sqrt((delta_ball_radius**2)/2))
    .style("stroke", "#6b4691")
    .style("stroke-width", 5);

// Radius delta symbol -------------------------------------------------------
epsilon_delta_svg.append("text")
    .text("\u03B4")
    .attr("x", width_epsilon_delta_svg/2 - 110 - 85)
    .attr("y", height_epsilon_delta_svg/2 -90 + 55)
    .attr("font-family", "sans-serif")
    .attr("font-size", "42px")
    .attr("fill", "#6b4691");

// Point x in epsilon ball --------------------------------------------------- 
epsilon_delta_svg.append("text")
    .text("x")
    .attr("x", width_epsilon_delta_svg/2 + 10)
    .attr("y", height_epsilon_delta_svg/2)
    .attr("font-family", "sans-serif")
    .attr("font-size", "42px")
    .attr("fill", "#f5ffde");

epsilon_delta_svg.append("circle")
    .style("fill", "#f5ffde")
    .attr("cx", width_epsilon_delta_svg/2)
    .attr("cy", height_epsilon_delta_svg/2)
    .attr("r", 5);

// Point y in delta ball -----------------------------------------------------
epsilon_delta_svg.append("text")
    .text("y")
    .attr("x", width_epsilon_delta_svg/2 - 110 + 10)
    .attr("y", height_epsilon_delta_svg/2 - 90)
    .attr("font-family", "sans-serif")
    .attr("font-size", "42px")
    .attr("fill", "#6b4691");

epsilon_delta_svg.append("circle")
    .style("fill", "#6b4691")
    .attr("cx", width_epsilon_delta_svg/2 - 110)
    .attr("cy", height_epsilon_delta_svg/2 - 90)
    .attr("r", 5);

// Point z in delta ball -----------------------------------------------------
epsilon_delta_svg.append("circle")
    .style("fill", "#6b4691")
    .attr("cx", width_epsilon_delta_svg/2 - 90)
    .attr("cy", height_epsilon_delta_svg/2 - 170)
    .attr("r", 5);

epsilon_delta_svg.append("text")
    .text("z")
    .attr("x", width_epsilon_delta_svg/2 - 90 - 30)
    .attr("y", height_epsilon_delta_svg/2 - 170)
    .attr("font-family", "sans-serif")
    .attr("font-size", "42px")
    .attr("fill", "#6b4691");





// Two-dimensional Euclidean space filled with balls of radius r -------------
//
//
// ---------------------------------------------------------------------------
// Total area we wish to fill is 107521
// 107521 comes from the following
// For h_0=380, [(h_0/2)^2]*pi=107521
// If a total area larger than 107521 is desired, 
// h_0 may be increased
// radius r=128 for larger circle and radius r=34 for smaller circles

var w_0 = 960;
var h_0 = 380;


var color = "rgba(105, 106, 97, 0.6)";

var number_nodes_0 = 1;
var nodes_set_0 = d3.range(number_nodes_0).map(function(d, i) {
	return {
		satellite_circles: [
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{}
		],
		radii_0: 145};
});

var the_simulation_0 = d3.forceSimulation(nodes_set_0)
    .force("center", d3.forceCenter(w_0/2, h_0/2));

var svg_nodes_set_0 = d3.select(".featuredgallery0")
  .append("svg")
    .attr("viewBox", "0 0 " + w_0 + " " + h_0); 

// larger space in which the circles reside
svg_nodes_set_0.append("circle")
    .style("stroke", "#6b4691")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3")
    .style("fill", "none")
    .attr("cx", w_0/2)
    .attr("cy", h_0/2)
    .attr("r", 185)
    .attr("class", "larger_space");

var all_the_nodes_0 = svg_nodes_set_0.selectAll(".node")
    .data(nodes_set_0)
    .enter()
  .append("g")
    .attr("class", "node");

all_the_nodes_0.append("circle")
    .attr("r", function(d) {
        return d.radii_0;	    
    })
    .style("fill", function(d) {
	    return color;
    })
    .attr("class", "circle");

all_the_nodes_0.append("g")
    .selectAll(".circle_small")
    .data(d => d.satellite_circles)
    .enter()
    .append("circle")
    .attr("r", 38)
    .style("fill", "rgba(117, 158, 22, 0.3)")
    .attr("cx", function(d, i) {
	    const factor = (i/15)*(10/2)*5;
	    return 145*Math.cos(factor-(Math.PI*0.5));
    })
    .attr("cy", function(d, i) {
	    const factor = (i/15)*(10/2)*5;
	    return 145*Math.sin(factor-(Math.PI*0.5));
    })
    .attr("class", "circle_small");


the_simulation_0.on("tick", function() {
	all_the_nodes_0.attr("transform", d => 
		`translate(${d.x}, ${d.y})`);
});

// gap circle highlighting that the larger space is not entirely filled
svg_nodes_set_0.append("circle")
    .attr("r", 20)
    .style("stroke", "#e0620d")
    .style("stroke-width", 5)
    .style("fill", "none")
    .attr("cx", w_0/2 - 185)
    .attr("cy", h_0/2 )
    .attr("class", "gap_circle");




// ---------------------------------------------------------------------------
// radius r=10 for larger circles and radius r=2.66 for smaller circles
var w_1 = 960;
var h_1 = 380;


var color_scale = ["rgba(107, 70, 145, 0.6)", 
	"rgba(58, 58, 54, 0.6)"];

// smaller_circle_radii_1 = radii_1*(266/1000)
const smaller_circle_radii_1 = 2.66;

// collide_factor_1 = radii_1*(2/3)

var number_nodes_1 = 570;
var nodes_set_1 = d3.range(number_nodes_1).map(function(d, i) {
	return {
		satellite_circles: [
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{},
			{}
		],
		radii_1: 10, category: i%2, collide_factor_1: 6.66};
});


var the_simulation_1 = d3.forceSimulation(nodes_set_1)
    .force("charge", d3.forceManyBody().strength(1))
    .force("center", d3.forceCenter(w_1/2, h_1/2))
    .force("collision", d3.forceCollide().radius(function(d) {
	    return d.collide_factor_1;
    }));


var svg_nodes_set_1 = d3.select(".featuredgallery1")
  .append("svg")
    .attr("viewBox", "0 0 " + w_1 + " " + h_1); 

// larger space in which the circles reside
svg_nodes_set_1.append("circle")
    .style("stroke", "#6b4691")
    .style("stroke-width", 5)
    .style("stroke-dasharray", "12 3")
    .style("fill", "none")
    .attr("cx", w_1/2)
    .attr("cy", h_1/2)
    .attr("r", 185)
    .attr("class", "larger_space");

var all_the_nodes_1 = svg_nodes_set_1.selectAll(".node")
    .data(nodes_set_1)
    .enter()
  .append("g")
    .attr("class", "node");

all_the_nodes_1.append("circle")
    .attr("r", function(d) {
        return d.radii_1;	    
    })
    .style("fill", function(d) {
	    return color_scale[d.category];
    })
    .attr("class", "circle");

all_the_nodes_1.append("g")
    .selectAll(".circle_small")
    .data(d => d.satellite_circles)
    .enter()
    .append("circle")
    .attr("r", smaller_circle_radii_1)
    .style("fill", "rgba(117, 158, 22, 0.3)")
    .attr("cx", function(d, i) {
	    const factor = (i/15)*(10/2)*5;
	    return 10*Math.cos(factor-(Math.PI*0.5));
    })
    .attr("cy", function(d, i) {
	    const factor = (i/15)*(10/2)*5;
	    return 10*Math.sin(factor-(Math.PI*0.5));
    })
    .attr("class", "circle_small");


the_simulation_1.on("tick", function() {
	all_the_nodes_1.attr("transform", d => 
		`translate(${d.x}, ${d.y})`);
});

// gap circle highlighting that the larger space is not entirely filled
svg_nodes_set_1.append("circle")
    .attr("r", 20)
    .style("stroke", "#e0620d")
    .style("stroke-width", 5)
    .style("fill", "none")
    .attr("cx", w_1/2 - 185)
    .attr("cy", h_1/2 )
    .attr("class", "gap_circle");



