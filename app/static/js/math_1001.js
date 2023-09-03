// Venn Diagram --------------------------------------------------------------
//
// Three circles Inclusion-Exclusion Principle--------------------------------
const i_e_w = 960;
const i_e_h = 500;

var i_e_svg = d3.select("#inclusion_exclusion")
  .append("svg")
    .attr("viewBox", "0 0 " + i_e_w + " " + i_e_h);

const i_e_w_by_3 = i_e_w/3;
const i_e_h_by_3 = i_e_h/4;

// Universe Box
//
// top line
i_e_svg.append("line")
    .attr("x1", i_e_w_by_3/2)
    .attr("y1", 0.01*i_e_h)
    .attr("x2", 2*i_e_w_by_3)
    .attr("y2", 0.01*i_e_h)
    .attr("stroke", "#696a61")
    .attr("stroke-width", 3);

// right line
i_e_svg.append("line")
    .attr("x1", 2*i_e_w_by_3)
    .attr("y1", 0.01*i_e_h)
    .attr("x2", 2*i_e_w_by_3)
    .attr("y2", 3*(i_e_h/4) - 10)
    .attr("stroke", "#696a61")
    .attr("stroke-width", 3);

// bottom line
i_e_svg.append("line")
    .attr("x1", 2*i_e_w_by_3)
    .attr("y1", 3*(i_e_h/4) - 10)
    .attr("x2", i_e_w_by_3/2)
    .attr("y2", 3*(i_e_h/4) - 10)
    .attr("stroke", "#696a61")
    .attr("stroke-width", 3);

// left line
i_e_svg.append("line")
    .attr("x1", i_e_w_by_3/2)
    .attr("y1", 3*(i_e_h/4) - 10)
    .attr("x2", i_e_w_by_3/2)
    .attr("y2", 0.01*i_e_h)
    .attr("stroke", "#696a61")
    .attr("stroke-width", 3);

// Universe label
i_e_svg.append("text")
    .text("Universe")
    .attr("x", i_e_w_by_3/2 + 20)
    .attr("y", 3*(i_e_h/4) - 30)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

const i_e_r = 115;

// Left Circle
i_e_svg.append("circle")
    .attr("cx", i_e_w_by_3)
    .attr("cy", i_e_h_by_3)
    .attr("r", i_e_r)
    .attr("fill", "none")
    .attr("stroke", "#696a61")
    .attr("stroke-width", 5)
    .attr("stroke-dasharray", "3 3");


// Distance between centers of left and right circles
const offset = 1.2*i_e_r;

// Right Circle
i_e_svg.append("circle")
    .attr("cx", i_e_w_by_3 + offset)
    .attr("cy", i_e_h_by_3)
    .attr("r", i_e_r)
    .attr("fill", "none")
    .attr("stroke", "#696a61")
    .attr("stroke-width", 5)
    .attr("stroke-dasharray", "3 3");

// Distance between top leg of equilateral triangle and center of 
// bottom circle
const bottom_circle_drop = i_e_h_by_3 + Math.sqrt(offset**2 - (offset/2)**2);

// Bottom Circle
i_e_svg.append("circle")
    .attr("cx", i_e_w_by_3 + (offset)/2)
    .attr("cy", bottom_circle_drop)
    .attr("r", i_e_r)
    .attr("fill", "none")
    .attr("stroke", "#696a61")
    .attr("stroke-width", 5)
    .attr("stroke-dasharray", "3 3");

// The following are lines and points to help aid in the construction of the 
// the points 0 through 8

// Points
// i_e_point_0 is the center of the left circle
// i_e_point_1 is the center of the bottom circle
// i_e_point_2 is the bottom left intersection of the left and bottom circles
// i_e_point_3 is the center of the right circle
// i_e_point_4 is bottom right intersection of the right and bottom circles
// i_e_point_5 is the bottom of triple intersection
// i_e_point_6 is the top right of triple intersection
// i_e_point_7 is the top left of the triple intersection
// i_e_point_8 is the top intersection of the left and right circles

// Height of the triangle with vertices at the centers of the three circles:
// center of the left circle (i_e_w_by_3, i_e_h_by_3)
// center of the right circle (i_e_w_by_3 + offset, i_e_h_by_3)
// center of the bottom circle 
// (i_e_w_by_3 + offset/2, i_e_h_by_3 + Math.sqrt(offset**2 - (offset/2))**2)

//i_e_point_0 = i_e_svg.append("circle")
//    .attr("cx", i_e_w_by_3)
//    .attr("cy", i_e_h_by_3)
//    .attr("r", 5)
//    .attr("fill", "#696a61");

//i_e_point_1 = i_e_svg.append("circle")
//    .attr("cx", i_e_w_by_3 + (offset)/2)
//    .attr("cy", bottom_circle_drop)
//    .attr("r", 5)
//    .attr("fill", "#696a61");

//i_e_point_3 = i_e_svg.append("circle")
//    .attr("cx", i_e_w_by_3 + (offset))
//    .attr("cy", i_e_h_by_3)
//    .attr("r", 5)
//    .attr("fill", "#696a61");

// top equilateral triangle leg
//----------------------------------------------------------------------------
//i_e_svg.append("line")
//    .attr("x1", i_e_w_by_3)
//    .attr("y1", i_e_h_by_3)
//    .attr("x2", i_e_w_by_3 + offset)
//    .attr("y2", i_e_h_by_3)
//    .attr("stroke", "black");

// right equilateral triangle leg
// ---------------------------------------------------------------------------
//i_e_svg.append("line")
//    .attr("x1", i_e_w_by_3 + offset)
//    .attr("y1", i_e_h_by_3)
//    .attr("x2", i_e_w_by_3 + (offset)/2)
//    .attr("y2", bottom_circle_drop)
//    .attr("stroke", "black");

// midpoint of right equaliteral triangle leg
// Let the center of the bottom circle be the origin point.
// The circle with edge containing the midpoint of the right equilateral
// triangle leg has radius offset/2. The angle in standard position
// is measure 60 degrees---we are using the right leg and its attending angles
// of the equilateral triangle to determine this. Finally, we find the 
// change in the x and y directions between the center of the bottom circle
// and the midpoint of the right equilateral triangle leg, which is contained
// along the edge of our circle. This gives us the coordinate at which the 
// the midpoint of our right equilateral triangle leg sits.
// ---------------------------------------------------------------------------
//i_e_svg.append("circle")
//    .attr("cx", i_e_w_by_3 + (offset)/2 + (offset/2)*Math.cos(Math.PI/3))
//    .attr("cy", 
//	    bottom_circle_drop - 
//	    (offset/2)*Math.sin(Math.PI/3))
//    .attr("r", 5)
//    .attr("fill", "#696a61");
// ---------------------------------------------------------------------------
// Given that the triangle is equilateral, the distance from the midpoint
// of the right leg of the equilateral triangle to the top left corner point 
// of the triple intersection is the same distance the top leg of the
// equilateral triangle is from the bottom corner point of the triple
// intersection. We address this in the variable triple_intersection_height
// below. Once we have that distance, we find the change in the x and y
// directions between the midpoint of the right leg of the equilateral 
// triangle and where the top left corner point of the triple intersection
// will be placed.


// left equilateral triangle leg
// ---------------------------------------------------------------------------
//i_e_svg.append("line")
//    .attr("x1", i_e_w_by_3)
//    .attr("y1", i_e_h_by_3)
//    .attr("x2", i_e_w_by_3 + (offset)/2)
//    .attr("y2", bottom_circle_drop)
//    .attr("stroke", "black");

// midpoint of left equilateral triangle leg
// ---------------------------------------------------------------------------
//i_e_svg.append("circle")
//    .attr("cx", i_e_w_by_3 + (offset)/2 - (offset/2)*Math.cos(Math.PI/3))
//    .attr("cy", 
//	    bottom_circle_drop - 
//	    (offset/2)*Math.sin(Math.PI/3))
//    .attr("r", 5)
//    .attr("fill", "#696a61");

// bottom right point of quadrilateral containing bottom right intersection
// point
// ---------------------------------------------------------------------------
//i_e_svg.append("circle")
//    .attr("cx", i_e_w_by_3 + (offset/2) + offset)
//    .attr("cy", bottom_circle_drop)
//    .attr("r", 5)
//    .attr("fill", "#696a61");


// To find the height of the triple intersection, we use half of the distance
// of the offset along the top leg of the equilateral triangle 
// as one leg of a right triangle and the
// radius of the left circle along the line connecting the center
// of the left circle with the bottom corner point of the triple intersection
// as the hypotenuse of that right triangle to find the other leg of that
// right triangle, which happens to be the height of the tiple intersection.

const triple_intersection_height = Math.sqrt((i_e_r)**2 - ((offset)/2)**2);

//i_e_point_5 = i_e_svg.append("circle")
//    .attr("cx", i_e_w_by_3 + (offset)/2)
//    .attr("cy", i_e_h_by_3 + triple_intersection_height)
//    .attr("r", 5)
//    .attr("fill", "#696a61");
//
//
//
//i_e_point_7 = i_e_svg.append("circle")
//    .attr("cx", 
//	    i_e_w_by_3 + 
//	    (offset)/2 + 
//	    (offset/2)*Math.cos(Math.PI/3) - 
//	    triple_intersection_height*Math.sin(Math.PI/3))
//    .attr("cy", 
//	    bottom_circle_drop - 
//	    (offset/2)*Math.sin(Math.PI/3) - 
//    	    triple_intersection_height*Math.cos(Math.PI/3))
//    .attr("r", 5)
//    .attr("fill", "#696a61");
//
//i_e_point_6 = i_e_svg.append("circle")
//    .attr("cx", 
//	    i_e_w_by_3 + 
//	    (offset)/2 - 
//	    (offset/2)*Math.cos(Math.PI/3) + 
//	    triple_intersection_height*Math.sin(Math.PI/3))
//    .attr("cy", 
//	    bottom_circle_drop - 
//	    (offset/2)*Math.sin(Math.PI/3) - 
//    	    triple_intersection_height*Math.cos(Math.PI/3))
//    .attr("r", 5)
//    .attr("fill", "#696a61");

// For point 8, we take a similar approach as the one we took for the
// tiple_intersection_height variable
//i_e_point_8 = i_e_svg.append("circle")
//    .attr("cx", i_e_w_by_3 + offset/2)
//    .attr("cy", i_e_h_by_3 - Math.sqrt((i_e_r)**2 - (offset/2)**2))
//    .attr("r", 5)
//    .attr("fill", "#696a61");

// We use a point at the bottom right corner point of the rhombus with leg
// between the centers of the left circle and right circle (top-most leg)
// between the centers of the left circle and bottom circle (left side leg)
// to help us find i_e_point_4. The distance between this point
// and i_e_point_4 is the same as the distance between i_e_point_1 and
// i_e_point_5. The distance between i_e_point_1 and this new point is offset,
// given that we are using the rhombus to identify this point. Once we
// identify the coordinates of this point, we use the distance between
// i_e_point_1 and i_e_point_5 along with the change in the x and y
// directions between this new point and where i_e_point_4 is expected
// to sit (at the bottom right intersection of the right and bottom circles)
// to find the coordinates of i_e_point_4.

const i_e_point_1_to_i_e_point_5_distance = 
	bottom_circle_drop - i_e_h_by_3 - triple_intersection_height;

//i_e_point_4 = i_e_svg.append("circle")
//    .attr("cx", 
//	    i_e_w_by_3 + 
//	    (offset/2) +
//	    offset - 
//	    i_e_point_1_to_i_e_point_5_distance*Math.cos(Math.PI/6))
//    .attr("cy",
//    	    bottom_circle_drop - 
//	    i_e_point_1_to_i_e_point_5_distance*Math.sin(Math.PI/6))
//    .attr("r", 5)
//    .attr("fill", "#696a61");
//
//i_e_point_2 = i_e_svg.append("circle")
//    .attr("cx", 
//	    i_e_w_by_3 + 
//	    (offset/2) -
//	    offset + 
//	    i_e_point_1_to_i_e_point_5_distance*Math.cos(Math.PI/6))
//    .attr("cy",
//    	    bottom_circle_drop - 
//	    i_e_point_1_to_i_e_point_5_distance*Math.sin(Math.PI/6))
//    .attr("r", 5)
//    .attr("fill", "#696a61");

// Here, we list the components of each point
// point 8 -------------------------------------------------------------------
const i_e_point_8_x = i_e_w_by_3 + offset/2;
const i_e_point_8_y = i_e_h_by_3 - Math.sqrt((i_e_r)**2 - (offset/2)**2);
// point 5 ------------------------------------------------------------------- 
const i_e_point_5_x = i_e_w_by_3 + offset/2;
const i_e_point_5_y = i_e_h_by_3 + triple_intersection_height;
// point 7 -------------------------------------------------------------------
const i_e_point_7_x =
	i_e_w_by_3 +
	(offset/2) +
	(offset/2)*Math.cos(Math.PI/3) - 
	triple_intersection_height*Math.sin(Math.PI/3);
const i_e_point_7_y = 
	bottom_circle_drop -
	(offset/2)*Math.sin(Math.PI/3) - 
	triple_intersection_height*Math.cos(Math.PI/3);
// point 6 -------------------------------------------------------------------
const i_e_point_6_x = 
	i_e_w_by_3 +
	(offset/2) -
	(offset/2)*Math.cos(Math.PI/3) +
	triple_intersection_height*Math.sin(Math.PI/3);
const i_e_point_6_y = 
   	bottom_circle_drop - 
    	(offset/2)*Math.sin(Math.PI/3) - 
	triple_intersection_height*Math.cos(Math.PI/3);
// point 4 -------------------------------------------------------------------
const i_e_point_4_x =
	i_e_w_by_3 +
	(offset/2) +
	offset -
	i_e_point_1_to_i_e_point_5_distance*Math.cos(Math.PI/6);
const i_e_point_4_y = 
	bottom_circle_drop -
	i_e_point_1_to_i_e_point_5_distance*Math.sin(Math.PI/6);
// point 2 -------------------------------------------------------------------
const i_e_point_2_x = 
	i_e_w_by_3 +
	(offset/2) -
	offset +
	i_e_point_1_to_i_e_point_5_distance*Math.cos(Math.PI/6);
const i_e_point_2_y = 
	bottom_circle_drop -
	i_e_point_1_to_i_e_point_5_distance*Math.sin(Math.PI/6);

// Here, we change from the above system of coordinate numbering to: 
// 8 --> 1
// 6 --> 5
// 7 --> 6
// 5 --> 4
// 4 --> 3
// 2 --> 2
// So, the map below takes in 
// i=1 and points to our point 8
// i=2 and points to our point 2
// i=3 and points to our point 4
// i=4 and points to our point 5
// i=5 and points to our point 6
// i=6 and points to our point 7
x_points = [
	i_e_point_8_x,
	i_e_point_2_x,
	i_e_point_4_x,
	i_e_point_5_x,
	i_e_point_6_x,
	i_e_point_7_x
];
y_points = [
	i_e_point_8_y,
	i_e_point_2_y,
	i_e_point_4_y,
	i_e_point_5_y,
	i_e_point_6_y,
	i_e_point_7_y
];

const make_universe = `M ${i_e_w_by_3/2} ${0.01*i_e_h}
		L ${2*i_e_w_by_3} ${0.01*i_e_h}
		L ${2*i_e_w_by_3} ${3*(i_e_h/4) - 10}
		L ${i_e_w_by_3/2} ${3*(i_e_h/4) - 10}
		Z`

const make_iron = ([x1, x2, x3, y1, y2, y3]) => {
	path = `M ${x1} ${y1}
		A ${i_e_r} ${i_e_r} 0 0 1 ${x2} ${y2}
		A ${i_e_r} ${i_e_r} 0 0 0 ${x3} ${y3}
		A ${i_e_r} ${i_e_r} 0 0 1 ${x1} ${y1}`
	return path;
}


const make_umbrella = ([x1, x2, x3, y1, y2, y3]) => {
	path = `M ${x1} ${y1}
		A ${i_e_r} ${i_e_r} 0 0 0 ${x2} ${y2}
		A ${i_e_r} ${i_e_r} 0 0 0 ${x3} ${y3}
		A ${i_e_r} ${i_e_r} 0 1 1 ${x1} ${y1}`
	return path;
}

const make_shield = ([x1, x2, x3, y1, y2, y3]) => {
	path = `M ${x1} ${y1}
		A ${i_e_r} ${i_e_r} 0 0 1 ${x2} ${y2}
		A ${i_e_r} ${i_e_r} 0 0 1 ${x3} ${y3}
		A ${i_e_r} ${i_e_r} 0 0 1 ${x1} ${y1}`
	return path;
}

iron_points = [
	[1, 5, 6],
	[3, 4, 5],
	[2, 6, 4]
];

umbrella_points = [
	[3, 5, 1],
	[2, 4, 3],
	[1, 6, 2]
];

shield_points = [
	[5, 4, 6]
];

i_e_svg.append("text")
    .attr("class", "menu_item")
    .text("Banana")
    .attr("x", 3*(i_e_w_by_3/4))
    .attr("y", i_e_h_by_3 - 40)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "menu_item")
    .text("Honey")
    .attr("x", i_e_w_by_3 + offset)
    .attr("y", i_e_h_by_3 - 40)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "menu_item")
    .text("Butter")
    .attr("text-anchor", "middle")
    .attr("x", i_e_w_by_3 + offset/2)
    .attr("y", 2*(i_e_h/3))
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

var universe = 100;
var left_umbrella = universe*0.25;
var right_umbrella = universe*0.20;
var bottom_umbrella = universe*0.15;
var top_iron = universe*0.10;
var left_iron = universe*0.12;
var right_iron = universe*0.13;
var shield = universe*0.03;
var neither = universe*0.02;

var banana = left_umbrella + top_iron + left_iron + shield;
var honey = right_umbrella + top_iron + right_iron + shield;
var butter = bottom_umbrella + left_iron + right_iron + shield;
var banana_honey = top_iron + shield;
var banana_butter = left_iron + shield;
var honey_butter = right_iron + shield;

i_e_svg.append("text")
    .attr("class", "conditions")
    .text("Total customer count " + universe)
    .attr("x", 0.01*i_e_w)
    .attr("y", 3*(i_e_h_by_3) + 40)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "conditions")
    .text("Those who like banana " + banana)
    .attr("x", 0.01*i_e_w)
    .attr("y", 3*(i_e_h_by_3) + 65)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "conditions")
    .text("Those who like honey " + honey)
    .attr("x", 0.01*i_e_w)
    .attr("y", 3*(i_e_h_by_3) + 90)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "conditions")
    .text("Those who like butter " + butter)
    .attr("x", 0.01*i_e_w)
    .attr("y", 3*(i_e_h_by_3) + 115)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "conditions")
    .text("Those who like banana and honey " + banana_honey)
    .attr("x", 0.45*i_e_w)
    .attr("y", 3*(i_e_h_by_3) + 40)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "conditions")
    .text("Those who like banana and butter " + banana_butter)
    .attr("x", 0.45*i_e_w)
    .attr("y", 3*i_e_h_by_3 + 65)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "conditions")
    .text("Those who like honey and butter " + honey_butter)
    .attr("x", 0.45*i_e_w)
    .attr("y", 3*i_e_h_by_3 + 90)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

i_e_svg.append("text")
    .attr("class", "conditions")
    .text("Those who like all three " + shield)
    .attr("x", 0.45*i_e_w)
    .attr("y", 3*i_e_h_by_3 + 115)
    .attr("font-family", "sans-serif")
    .attr("font-size", 30)
    .attr("fill", "#696a61");

// Neither count
i_e_svg.append("path")
    .attr("d", make_universe)
    .attr("class", "segment_neither")
    .attr("fill", "#f5ffde")
    .attr("opacity", 0.01);
i_e_svg.append("text")
    .attr("class", "segment_neither")
    .text(neither)
    .attr("x", (i_e_w_by_3/2) + 20)
    .attr("y", 3*(i_e_h/4) - 60)
    .attr("font-family", "sans-serif")
    .attr("font-size", 25)
    .attr("fill", "#696a61")
    .attr("opacity", 0.0);

for (const [n, point] of iron_points.entries()) {
	const point_cycle = point.map(i => x_points[i-1]).concat(
		point.map(i => y_points[i-1])
	);
	const shape = make_iron(point_cycle);

	var universe_array = [top_iron, right_iron, left_iron];

	var point_cycle_x = point.map(i => x_points[i-1]);
	var sum_x = 0;
	for (var j = 0; j < point_cycle_x.length; j++) {
		sum_x += point_cycle_x[j];
	}

	var point_cycle_y = point.map(i => y_points[i-1]);
	var sum_y = 0;
	for (var k = 0; k < point_cycle_y.length; k++) {
		sum_y += point_cycle_y[k];
	}

	if (n == 0) {
		i_e_svg.append("path")
		    .attr("d", shape)
		    .attr("class", "segment_8_6_7")
		    .attr("fill", "#759e16")
		    .attr("opacity", 0.4);
		i_e_svg.append("text")
		    .attr("class", "segment_8_6_7")
		    .text(universe_array[0])
		    .attr("text-anchor", "middle")
		    .attr("x", sum_x/3)
		    .attr("y", sum_y/3)
		    .attr("font-family", "sans-serif")
		    .attr("font-size", 25)
		    .attr("fill", "#696a61")
		    .attr("opacity", 0.0);
	} else if (n == 1) {
		i_e_svg.append("path")
		    .attr("d", shape)
		    .attr("class", "segment_4_5_6")
		    .attr("fill", "#759e16")
		    .attr("opacity", 0.4);
		i_e_svg.append("text")
		    .attr("class", "segment_4_5_6")
		    .text(universe_array[1])
		    .attr("text-anchor", "start")
		    .attr("x", sum_x/3)
		    .attr("y", sum_y/3 + 10)
		    .attr("font-family", "sans-serif")
		    .attr("font-size", 25)
		    .attr("fill", "#696a61")
		    .attr("opacity", 0.0);
	} else {
		i_e_svg.append("path")
		    .attr("d", shape)
		    .attr("class", "segment_2_7_5")
		    .attr("fill", "#759e16")
		    .attr("opacity", 0.4);
		i_e_svg.append("text")
		    .attr("class", "segment_2_7_5")
		    .text(universe_array[2])
		    .attr("text-anchor", "end")
		    .attr("x", sum_x/3)
		    .attr("y", sum_y/3 + 10)
		    .attr("font-family", "sans-serif")
		    .attr("font-size", 25)
		    .attr("fill", "#696a61")
		    .attr("opacity", 0.0);
	}
}

for (const [n, point] of umbrella_points.entries()) {
	const point_cycle = point.map(i => x_points[i-1]).concat(
		point.map(i => y_points[i-1])
	);
	const shape = make_umbrella(point_cycle);
	
	var universe_array = [right_umbrella, bottom_umbrella, left_umbrella];

	var point_cycle_x = point.map(i => x_points[i-1]);
	var sum_x = 0;
	for (var j = 0; j < point_cycle_x.length; j++) {
		sum_x += point_cycle_x[j];
	}

	var point_cycle_y = point.map(i => y_points[i-1]);
	var sum_y = 0;
	for (var k = 0; k < point_cycle_y.length; k++) {
		sum_y += point_cycle_y[k];
	}
	
	if (n == 0) {
		i_e_svg.append("path")
		    .attr("d", shape)
		    .attr("class", "segment_8_6_4")
		    .attr("fill", "#e0620d")
		    .attr("opacity", 0.4);

		const x_position = 1.2*(sum_x/3);
		const y_position = sum_y/3;

		i_e_svg.append("text")
		    .attr("class", "segment_8_6_4")
		    .text(universe_array[0])
		    .attr("text-anchor", "middle")
		    .attr("x", x_position)
		    .attr("y", y_position)
		    .attr("font-family", "sans-serif")
		    .attr("font-size", 25)
		    .attr("fill", "#696a61")
		    .attr("opacity", 0.0);
	} else if (n == 1) {
		i_e_svg.append("path")
		    .attr("d", shape)
		    .attr("class", "segment_4_5_2")
		    .attr("fill", "#e0620d")
		    .attr("opacity", 0.4);

		const x_position = sum_x/3;
		const y_position = 1.2*(sum_y/3);

		i_e_svg.append("text")
		    .attr("class", "segment_4_5_2")
		    .text(universe_array[1])
		    .attr("text-anchor", "middle")
		    .attr("x", x_position)
		    .attr("y", y_position)
		    .attr("font-family", "sans-serif")
		    .attr("font-size", 25)
		    .attr("fill", "#696a61")
		    .attr("opacity", 0.0);
	} else {
		i_e_svg.append("path")
		    .attr("d", shape)
		    .attr("class", "segment_2_7_8")
		    .attr("fill", "#e0620d")
		    .attr("opacity", 0.4);

		const x_position = sum_x/3 - 0.2*(sum_x/3);
		const y_position = sum_y/3;

		i_e_svg.append("text")
		    .attr("class", "segment_2_7_8")
		    .text(universe_array[2])
		    .attr("text-anchor", "middle")
		    .attr("x", x_position)
		    .attr("y", y_position)
		    .attr("font-family", "sans-serif")
		    .attr("font-size", 25)
		    .attr("fill", "#696a61")
		    .attr("opacity", 0.0);
	}
}

for (const [n, point] of shield_points.entries()) {
	const point_cycle = point.map(i => x_points[i-1]).concat(
		point.map(i => y_points[i-1])
	);
	const shape = make_shield(point_cycle);
	
	var universe_array = [shield];

	var point_cycle_x = point.map(i => x_points[i-1]);
	var sum_x = 0;
	for (var j = 0; j < point_cycle_x.length; j++) {
		sum_x += point_cycle_x[j];
	}

	var point_cycle_y = point.map(i => y_points[i-1]);
	var sum_y = 0;
	for (var k = 0; k < point_cycle_y.length; k++) {
		sum_y += point_cycle_y[k];
	}

	i_e_svg.append("path")
	    .attr("d", shape)
	    .attr("class", "segment_6_5_7")
	    .attr("fill", "#ffcd04")
	    .attr("opacity", 0.4);
	i_e_svg.append("text")
	    .attr("class", "segment_6_5_7")
	    .text(universe_array[0])
	    .attr("text-anchor", "middle")
	    .attr("x", sum_x/3)
	    .attr("y", sum_y/3)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 25)
	    .attr("fill", "#696a61")
	    .attr("opacity", 0.0);
}


d3.select("path.segment_8_6_4")
    .on("mouseover", function() {
	    i_e_svg.selectAll(".segment_8_6_4")
	        .transition()
	        .attr("opacity", 0.8)
	        .duration(500);
    })
    .on("mouseout", function() {
	    i_e_svg.selectAll(".segment_8_6_4")
	        .transition()
	        .attr("opacity", 0.4)
	        .duration(500);
    });
d3.select("path.segment_4_5_2")
    .on("mouseover", function() {
	    i_e_svg.selectAll(".segment_4_5_2")
	        .transition()
	        .attr("opacity", 0.8)
	        .duration(500);
    })
    .on("mouseout", function() {
	    i_e_svg.selectAll(".segment_4_5_2")
	        .transition()
	        .attr("opacity", 0.4)
	        .duration(500);
    });
d3.select("path.segment_2_7_8")
    .on("mouseover", function() {
	    i_e_svg.selectAll(".segment_2_7_8")
	        .transition()
	        .attr("opacity", 0.8)
	        .duration(500);
    })
    .on("mouseout", function() {
	    i_e_svg.selectAll(".segment_2_7_8")
	        .transition()
	        .attr("opacity", 0.4)
	        .duration(500);
    });
d3.select("path.segment_8_6_7")
    .on("mouseover", function() {
	    i_e_svg.selectAll(".segment_8_6_7")
	        .transition()
	        .attr("opacity", 0.8)
	        .duration(500);
    })
    .on("mouseout", function() {
	    i_e_svg.selectAll(".segment_8_6_7")
	        .transition()
	        .attr("opacity", 0.4)
	        .duration(500);
    });
d3.select("path.segment_4_5_6")
    .on("mouseover", function() {
	    i_e_svg.selectAll(".segment_4_5_6")
	        .transition()
	        .attr("opacity", 0.8)
	        .duration(500);
    })
    .on("mouseout", function() {
	    i_e_svg.selectAll(".segment_4_5_6")
	        .transition()
	        .attr("opacity", 0.4)
	        .duration(500);
    });
d3.select("path.segment_2_7_5")
    .on("mouseover", function() {
	    i_e_svg.selectAll(".segment_2_7_5")
	        .transition()
	        .attr("opacity", 0.8)
	        .duration(500);
    })
    .on("mouseout", function() {
	    i_e_svg.selectAll(".segment_2_7_5")
	        .transition()
	        .attr("opacity", 0.4)
	        .duration(500);
    });
d3.select("path.segment_6_5_7")
    .on("mouseover", function() {
	    i_e_svg.selectAll(".segment_6_5_7")
	        .transition()
	        .attr("opacity", 0.8)
	        .duration(500);
    })
    .on("mouseout", function() {
	    i_e_svg.selectAll(".segment_6_5_7")
	        .transition()
	        .attr("opacity", 0.4)
	        .duration(500);
    });
d3.select("path.segment_neither")
    .on("mouseover", function() {
	    i_e_svg.selectAll(".segment_neither")
	        .transition()
	        .attr("opacity", 0.8)
	        .duration(500);
    })
    .on("mouseout", function() {
	    i_e_svg.selectAll(".segment_neither")
	        .transition()
	        .attr("opacity", 0.01)
	        .duration(500);
    });


d3.select("#inclusion_exclusion_button")
    .on("click", function() {
	i_e_svg.select("text.segment_8_6_4")
	    .remove();
	i_e_svg.select("text.segment_4_5_2")
	    .remove();
	i_e_svg.select("text.segment_2_7_8")
	    .remove();
	i_e_svg.select("text.segment_8_6_7")
	    .remove();
	i_e_svg.select("text.segment_4_5_6")
	    .remove();
	i_e_svg.select("text.segment_2_7_5")
	    .remove();
	i_e_svg.select("text.segment_6_5_7")
	    .remove();
	i_e_svg.select("text.segment_neither")
	    .remove();

	i_e_svg.selectAll("text.conditions")
	    .remove();

	const universe_generator = [
		100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 
		1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 
		2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900,
		3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800
	];
	universe = universe_generator[Math.floor(Math.random()*38)];
	left_umbrella = universe*0.25;
	right_umbrella = universe*0.20;
	bottom_umbrella = universe*0.15;
	top_iron = universe*0.10;
	left_iron = universe*0.12;
	right_iron = universe*0.13;
	shield = universe*0.03;
	neither = universe*0.02;

	banana = left_umbrella + top_iron + left_iron + shield;
	honey = right_umbrella + top_iron + right_iron + shield;
	butter = bottom_umbrella + left_iron + right_iron + shield;
	banana_honey = top_iron + shield;
	banana_butter = left_iron + shield;
	honey_butter = right_iron + shield;

	i_e_svg.append("text")
	    .attr("class", "conditions")
	    .text("Total customer count " + universe)
	    .attr("x", 0.01*i_e_w)
	    .attr("y", 3*i_e_h_by_3 + 40)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 30)
	    .attr("fill", "#696a61");
	
	i_e_svg.append("text")
	    .attr("class", "conditions")
	    .text("Those who like banana " + banana)
	    .attr("x", 0.01*i_e_w)
	    .attr("y", 3*i_e_h_by_3 + 65)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 30)
	    .attr("fill", "#696a61");
	
	i_e_svg.append("text")
	    .attr("class", "conditions")
	    .text("Those who like honey " + honey)
	    .attr("x", 0.01*i_e_w)
	    .attr("y", 3*i_e_h_by_3 + 90)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 30)
	    .attr("fill", "#696a61");
	
	i_e_svg.append("text")
	    .attr("class", "conditions")
	    .text("Those who like butter " + butter)
	    .attr("x", 0.01*i_e_w)
	    .attr("y", 3*i_e_h_by_3 + 115)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 30)
	    .attr("fill", "#696a61");
	
	i_e_svg.append("text")
	    .attr("class", "conditions")
	    .text("Those who like banana and honey " + banana_honey)
	    .attr("x", 0.45*i_e_w)
	    .attr("y", 3*i_e_h_by_3 + 40)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 30)
	    .attr("fill", "#696a61");
	
	i_e_svg.append("text")
	    .attr("class", "conditions")
	    .text("Those who like banana and butter " + banana_butter)
	    .attr("x", 0.45*i_e_w)
	    .attr("y", 3*i_e_h_by_3 + 65)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 30)
	    .attr("fill", "#696a61");
	
	i_e_svg.append("text")
	    .attr("class", "conditions")
	    .text("Those who like honey and butter " + honey_butter)
	    .attr("x", 0.45*i_e_w)
	    .attr("y", 3*i_e_h_by_3 + 90)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 30)
	    .attr("fill", "#696a61");
	
	i_e_svg.append("text")
	    .attr("class", "conditions")
	    .text("Those who like all three " + shield)
	    .attr("x", 0.45*i_e_w)
	    .attr("y", 3*i_e_h_by_3 + 115)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 30)
	    .attr("fill", "#696a61");
	
	// Neither count
	i_e_svg.append("text")
	    .attr("class", "segment_neither")
	    .text(neither)
	    .attr("x", (i_e_w_by_3/2) + 20)
	    .attr("y", 3*(i_e_h/4) - 60)
	    .attr("font-family", "sans-serif")
	    .attr("font-size", 25)
	    .attr("fill", "#696a61")
	    .attr("opacity", 0.0);

	for (const [n, point] of iron_points.entries()) {
		const point_cycle = point.map(i => x_points[i-1]).concat(
			point.map(i => y_points[i-1])
		);
		const shape = make_iron(point_cycle);
	
		var universe_array = [top_iron, right_iron, left_iron];
	
		var point_cycle_x = point.map(i => x_points[i-1]);
		var sum_x = 0;
		for (var j = 0; j < point_cycle_x.length; j++) {
			sum_x += point_cycle_x[j];
		}
	
		var point_cycle_y = point.map(i => y_points[i-1]);
		var sum_y = 0;
		for (var k = 0; k < point_cycle_y.length; k++) {
			sum_y += point_cycle_y[k];
		}
	
		if (n == 0) {
			i_e_svg.append("text")
			    .attr("class", "segment_8_6_7")
			    .text(universe_array[0])
			    .attr("text-anchor", "middle")
			    .attr("x", sum_x/3)
			    .attr("y", sum_y/3)
			    .attr("font-family", "sans-serif")
			    .attr("font-size", 25)
			    .attr("fill", "#696a61")
			    .attr("opacity", 0.0);
		} else if (n == 1) {
			i_e_svg.append("text")
			    .attr("class", "segment_4_5_6")
			    .text(universe_array[1])
			    .attr("text-anchor", "start")
			    .attr("x", sum_x/3)
			    .attr("y", sum_y/3 + 10)
			    .attr("font-family", "sans-serif")
			    .attr("font-size", 25)
			    .attr("fill", "#696a61")
			    .attr("opacity", 0.0);
		} else {
			i_e_svg.append("text")
			    .attr("class", "segment_2_7_5")
			    .text(universe_array[2])
			    .attr("text-anchor", "end")
			    .attr("x", sum_x/3)
			    .attr("y", sum_y/3 + 10)
			    .attr("font-family", "sans-serif")
			    .attr("font-size", 25)
			    .attr("fill", "#696a61")
			    .attr("opacity", 0.0);
		}
	}
	
	for (const [n, point] of umbrella_points.entries()) {
		const point_cycle = point.map(i => x_points[i-1]).concat(
			point.map(i => y_points[i-1])
		);
		const shape = make_umbrella(point_cycle);
		
		var universe_array = [right_umbrella, bottom_umbrella, left_umbrella];
	
		var point_cycle_x = point.map(i => x_points[i-1]);
		var sum_x = 0;
		for (var j = 0; j < point_cycle_x.length; j++) {
			sum_x += point_cycle_x[j];
		}
	
		var point_cycle_y = point.map(i => y_points[i-1]);
		var sum_y = 0;
		for (var k = 0; k < point_cycle_y.length; k++) {
			sum_y += point_cycle_y[k];
		}
		
		if (n == 0) {
	
			const x_position = 1.2*(sum_x/3);
			const y_position = sum_y/3;
	
			i_e_svg.append("text")
			    .attr("class", "segment_8_6_4")
			    .text(universe_array[0])
			    .attr("text-anchor", "middle")
			    .attr("x", x_position)
			    .attr("y", y_position)
			    .attr("font-family", "sans-serif")
			    .attr("font-size", 25)
			    .attr("fill", "#696a61")
			    .attr("opacity", 0.0);
		} else if (n == 1) {
	
			const x_position = sum_x/3;
			const y_position = 1.2*(sum_y/3);
	
			i_e_svg.append("text")
			    .attr("class", "segment_4_5_2")
			    .text(universe_array[1])
			    .attr("text-anchor", "middle")
			    .attr("x", x_position)
			    .attr("y", y_position)
			    .attr("font-family", "sans-serif")
			    .attr("font-size", 25)
			    .attr("fill", "#696a61")
			    .attr("opacity", 0.0);
		} else {
	
			const x_position = sum_x/3 - 0.2*(sum_x/3);
			const y_position = sum_y/3;
	
			i_e_svg.append("text")
			    .attr("class", "segment_2_7_8")
			    .text(universe_array[2])
			    .attr("text-anchor", "middle")
			    .attr("x", x_position)
			    .attr("y", y_position)
			    .attr("font-family", "sans-serif")
			    .attr("font-size", 25)
			    .attr("fill", "#696a61")
			    .attr("opacity", 0.0);
		}
	}
	
	for (const [n, point] of shield_points.entries()) {
		const point_cycle = point.map(i => x_points[i-1]).concat(
			point.map(i => y_points[i-1])
		);
		const shape = make_shield(point_cycle);
		
		var universe_array = [shield];
	
		var point_cycle_x = point.map(i => x_points[i-1]);
		var sum_x = 0;
		for (var j = 0; j < point_cycle_x.length; j++) {
			sum_x += point_cycle_x[j];
		}
	
		var point_cycle_y = point.map(i => y_points[i-1]);
		var sum_y = 0;
		for (var k = 0; k < point_cycle_y.length; k++) {
			sum_y += point_cycle_y[k];
		}
	
		i_e_svg.append("text")
		    .attr("class", "segment_6_5_7")
		    .text(universe_array[0])
		    .attr("text-anchor", "middle")
		    .attr("x", sum_x/3)
		    .attr("y", sum_y/3)
		    .attr("font-family", "sans-serif")
		    .attr("font-size", 25)
		    .attr("fill", "#696a61")
		    .attr("opacity", 0.0);
	}
    });

