from manim import(
    VMobject, SVGMobject, TexTemplateLibrary, Tex, 
    BLACK,
    DOWN,
)

from pathlib import Path
ASSETS_DIR = Path(__file__).resolve().parent.parent /"assets"/"普通展示"

class FileMobject(VMobject):
    """
        下面是自己设计的雏形, 细节上存在许多问题, 所以最终还是选择了使用svg图

        r = RoundedRectangle(width = 2, height = 3, corner_radius=0.2, stroke_width = 10)
        dot1 = Dot(r.point_from_proportion(0.1)).set_color(YELLOW)
        dot2 = Dot(r.point_from_proportion(0.93)).set_color(YELLOW)
        r2 = r.get_subcurve(0.97, 0.17).set_color(YELLOW).flip(UP+LEFT)
        r3 = r.get_subcurve(0.17, 0.97).set_color(YELLOW)
        line = Line(r.point_from_proportion(0.1), r.point_from_proportion(0.93)).match_style(r).set_color(YELLOW)
        v = VGroup(r2, r3, line)
        VMobject().append_vectorized_mobject()
        self.add(v, dot1,dot2)
"""


    def __init__(
            self,
            color = BLACK,
            name = ".c",
            **kwargs
    ):
        super().__init__(color = color, **kwargs)
        self.color = color
        self._name = name
        self.tex = None
        
        self.svg = self._get_file_svg()
        self.tex = self.set_name(name)

    def _get_file_svg(self):
        SVG_PATH = ASSETS_DIR/"文件.svg"
        svg = SVGMobject(SVG_PATH).set_color(self.color)
        self.add(svg)
        return svg
    
    def set_name(self, name = ".c"):
        if self.tex in self.submobjects:
            self.remove(self.tex)

        tex = Tex(name, tex_template = TexTemplateLibrary.ctex)
        tex.set_color(self.color)
        tex.shift(DOWN*0.2)
        if name == '.c':
            tex.scale(2)
        elif name == ".cpp":
            tex.scale(1.3)

        self.add(tex)
        return tex
