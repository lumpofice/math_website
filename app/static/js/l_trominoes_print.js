import * as saveSvgAsPng from "https://cdn.skypack.dev/save-svg-as-png@1.4.17";

const svg_button = document.getElementById("svg");

svg_button.addEventListener("click", () => {
	const element = document.getElementById("print_svg");
	const filename = "l_tromino_board.svg";

	saveSvgAsPng.saveSvg(element, filename);
});

