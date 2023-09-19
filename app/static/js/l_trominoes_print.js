import * as saveSvgAsPng from "https://cdn.skypack.dev/save-svg-as-png@1.4.17";
import { jsPDF } from "https://cdn.skypack.dev/jspdf@2.3.1";

const pdfBtn = document.getElementById("pdf");


pdfBtn.addEventListener("click", () => {
  const element = document.getElementById("print_svg");
  const filename = "l_trominoe_board.pdf";

  saveSvgAsPng.svgAsPngUri(element).then((dataUrl) => {
    console.log(dataUrl)
    const doc = new jsPDF();
    doc.addImage(dataUrl, "PNG", 0, 0).save(filename);
  });
});

