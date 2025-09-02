from manim import *
from package.数据结构制作规划.SqListVideo import SqListVideo

class FirstScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.opening_animation()

class SecnodScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.head_file_animation()

class ThirdScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.define_list_Sq_animation()

class FourthScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.initList_Sq_animation()

class FifthScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.destroy_and_clear_animation()

class SixthScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.insert_animation()

class SevenScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.erase_animation()

class EightScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.find_animation()
        
class NineScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.traverse_animation()

class TenScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.broaden_animation()

class ElevenScene(Scene):
    def construct(self):
        s = SqListVideo(self)
        s.end_animation()