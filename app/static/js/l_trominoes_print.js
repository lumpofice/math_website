import * as saveSvgAsPng from "https://cdn.skypack.dev/save-svg-as-png@1.4.17";
import { jsPDF } from "https://cdn.skypack.dev/jspdf@2.3.1";

const svgBtn = document.getElementById("svg");
const pngBtn = document.getElementById("png");
const pdfBtn = document.getElementById("pdf");

svgBtn.addEventListener("click", () => {
  const element = document.getElementById("print_svg");
  const filename = "myfilename.svg";
  saveSvgAsPng.saveSvg(element, filename);
});

pngBtn.addEventListener("click", () => {
  const element = document.getElementById("print_svg");
  const filename = "myfilename.png";
  saveSvgAsPng.saveSvgAsPng(element, filename);
});

pdfBtn.addEventListener("click", () => {
  const element = document.getElementById("print_svg");
  const filename = "myfilename.pdf";

  saveSvgAsPng.svgAsPngUri(element).then((dataUrl) => {
    console.log(dataUrl)
    const doc = new jsPDF();
    doc.addImage(dataUrl, "PNG", 0, 0).save(filename);
  });
});

