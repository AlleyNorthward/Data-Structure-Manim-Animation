from manim import *
from package.数据结构制作规划.SqListVideo import SqListVideo

class SecondChapterScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.chapter_animation()