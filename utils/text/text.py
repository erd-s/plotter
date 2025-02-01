import os
import xml.etree.ElementTree as etree
from config import DOC_WIDTH, DOC_HEIGHT, MARGIN

dir_path = os.path.dirname(os.path.realpath(__file__))
temp_svg_path = dir_path + "/tmp.svg"


def setup_document():
    tree = etree.parse(temp_svg_path)
    root = tree.getroot()
    # Update document size to match config.py
    root.set("width", f"{DOC_WIDTH}in")
    root.set("height", f"{DOC_HEIGHT}in")
    root[0].set("{http://www.inkscape.org/namespaces/inkscape}document-units", "in")
    remove_all_text(tree)
    tree.write(temp_svg_path)


def remove_all_text(tree: etree):
    root = tree.getroot()
    for g in root.findall(".//{http://www.w3.org/2000/svg}g"):
        for child in g.findall(".//{http://www.w3.org/2000/svg}text"):
            g.remove(child)


def write_text_in_xml(text: str, x_origin: float, y_origin: float):
    tree = etree.parse(temp_svg_path)
    root = tree.getroot()
    g = root.findall(".//{http://www.w3.org/2000/svg}g")[0]
    element = etree.SubElement(g, "{http://www.w3.org/2000/svg}text")
    element.set("id", "__pyinkscape_text_1")
    element.set("x", f"{x_origin}")
    element.set("y", f"{y_origin}")
    element.set("font-size", "18px")
    element.set("font-family", "sans-serif")
    element.set("fill", "black")
    element.set("text-anchor", "left")
    element.set(
        "style",
        "font-size:10px;font-family:sans-serif;font-style:normal;font-weight:normal;line-height:1.25;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none",
    )
    element.text = text
    tree.write(temp_svg_path)


def create_text(text: str, x_origin: float, y_origin: float):
    effective_x_origin = x_origin + MARGIN
    effective_y_origin = y_origin + MARGIN

    setup_document()
    write_text_in_xml(
        text=text, x_origin=effective_x_origin, y_origin=effective_y_origin
    )
