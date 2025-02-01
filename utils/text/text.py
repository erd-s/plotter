import os
import xml.etree.ElementTree as ElementTree
from config import DOC_WIDTH, DOC_HEIGHT, MARGIN

dir_path = os.path.dirname(os.path.realpath(__file__))
temp_svg_path = dir_path + "/tmp.svg"


def setup_document():
    tree = ElementTree.parse(temp_svg_path)
    root = tree.getroot()
    # Update document size to match config.py
    root.set("width", f"{DOC_WIDTH}in")
    root.set("height", f"{DOC_HEIGHT}in")
    root.set("viewBox", f"0 0 {DOC_HEIGHT}in {DOC_WIDTH}in")
    root[0].set("{http://www.inkscape.org/namespaces/inkscape}document-units", "in")
    remove_all_text(tree)
    tree.write(temp_svg_path)


def remove_all_text(tree: ElementTree):
    root = tree.getroot()
    for g in root.findall(".//{http://www.w3.org/2000/svg}g"):
        for child in g.findall(".//{http://www.w3.org/2000/svg}text"):
            g.remove(child)


def write_text_in_xml(text: str, x_origin: float, y_origin: float):
    tree = ElementTree.parse(temp_svg_path)
    root = tree.getroot()
    g = root.findall(".//{http://www.w3.org/2000/svg}g")[0]
    element = ElementTree.SubElement(g, "{http://www.w3.org/2000/svg}text")
    element.set("id", "text_layer_tmp")
    element.set("x", f"{x_origin}in")
    element.set("y", f"{y_origin}in")
    element.set("font-size", "18px")
    element.set("font-family", "sans-serif")
    element.set("fill", "black")
    element.set("text-anchor", "left")
    element.set(
        "style",
        "font-style:normal;font-weight:normal;font-size:10px;line-height:1.25;font-family:'Andale Mono';letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;-inkscape-font-specification:'Andale Mono, Normal';font-stretch:normal;font-variant:normal;font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-east-asian:normal"
    )
    element.text = text
    print(element.attrib)
    tree.write(temp_svg_path)


def create_text(text: str, x_origin: float, y_origin: float):
    effective_x_origin = x_origin
    effective_y_origin = y_origin

    setup_document()
    write_text_in_xml(
        text=text, x_origin=effective_x_origin, y_origin=effective_y_origin
    )
