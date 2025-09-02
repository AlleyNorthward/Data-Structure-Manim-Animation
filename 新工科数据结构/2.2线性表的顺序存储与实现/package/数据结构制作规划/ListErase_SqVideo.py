from manim import (
    VGroup, Tex, TexTemplateLibrary, SVGMobject, RoundedRectangle, Rectangle, ImageMobject,
    Create, FadeIn, FadeOut, Write, Wiggle, Succession, FocusOn, ReplacementTransform, Restore,
    BLACK, YELLOW_E, RED_E, ORANGE, MAROON_D, YELLOW_D, RED, BLUE_D, GREEN_E, GREEN, WHITE,
    UP, DOWN, ORIGIN, LEFT, RIGHT, 
    Scene,
)

from .VideoText import VideoText
from ..MovingCode import MovingCode
from ..ListNode import ListNode, ListNodeAnimation
from ..MyCurvedLine import MyCurvedLine
from ..MovingCode import MovingCode
from ..BulletedListBrace import BulletedListBrace

from pathlib import Path
ASSETS_DIR = Path(__file__).resolve().parent.parent.parent / "assets"

class InitBasicEraseMobject:
    # 这里本质上是先将Mobject绘制出来, 但是并未将
    # Mobject放到场景中. 所以是否会浪费时间呢?
    # 不清楚, 测试一下吧.  不用了, 分开了, 因为全部都初始化的话, 存在不知道哪个对象在哪更新的问题, 所以就分开吧.

    def __init__(
            self,
            scene: Scene,
            list_node_animation: ListNodeAnimation
    ):
        self.scene = scene
        self.list_node_animation = list_node_animation
        self.total_text = VideoText()
    
    def get_insert_nodes(self):

        """
            一开始不打算return, 但是如果想要整体移动, 发现只能一个一个地移动
            所以提供接口, 使其能够整体移动. 
            但是, 最好不要将return的对象分开操作, 本意不是这样的
            想单独访问某个对象, 只需要通过self.访问就好.
        """

        move_infos = ["1", "2", "3", "4", "5", "NULL"]
        nodes = ListNode.get_list_node_grps_with_index(self.scene, move_infos)

        self.insert_nodes = nodes[0]
        self.insert_pointer = nodes[1]
        self.insert_single_node = ListNode().set_info("6").set_node_color().next_to(self.insert_nodes, UP, 0.9)

        self.list_node_animation.save_nodes_state(self.insert_nodes)
        self.list_node_animation.save_nodes_state(self.insert_single_node)

        self.insert_curves_line1 = ListNode.get_nodes_curved_arrows(nodes[0], 4, 5)
        self.insert_curves_line2 = ListNode.get_nodes_curved_arrows(nodes[0], 3, 4)

        grps = VGroup(nodes, self.insert_single_node, self.insert_curves_line1, self.insert_curves_line2)

        return grps

    def get_erase_nodes(self, index):

        moving_infos = ["1", "2", "3", "4", "5", "6"]
        nodes = ListNode.get_list_node_grps_with_index(self.scene, moving_infos)
        self.erase_nodes = nodes[0]
        self.erase_pointer = nodes[1]

        self.erase_tex = Tex(self.total_text.CAPTION11, tex_template = TexTemplateLibrary.ctex)
        self.erase_tex.set_color(BLACK).scale(0.7)
        self.erase_tex.next_to(self.erase_nodes[index], DOWN, buff = 0.1)
        
        self.list_node_animation.save_nodes_state(self.erase_nodes)

        self.erase_curves_line1 = ListNode.get_nodes_curved_arrows(nodes[0], 3, 4, isflip=False)
        self.erase_curves_line2 = ListNode.get_nodes_curved_arrows(nodes[0], 4, 5, isflip=False)

        grps = VGroup(nodes, self.erase_tex, self.erase_curves_line1, self.erase_curves_line2)
        return grps
    
    def get_realloc_erase_code(self):
        PATH_REALLOC = ASSETS_DIR / "展示代码" / "6ListErase_Sq1.cpp"
        self.realloc_code = MovingCode(PATH_REALLOC)
        self.realloc_code.scale(0.7)
        self.realloc_code.move_to(ORIGIN)

    def get_normal_code(self):

        PATH_NORMAL = ASSETS_DIR / "展示代码" / "6ListErase_Sq2.cpp"
        self.normal_code = MovingCode(PATH_NORMAL)
        self.normal_code.scale(0.88)
        self.normal_code.move_to(ORIGIN)


        self.norm_return = Tex(self.total_text.CAPTION12, tex_template = TexTemplateLibrary.ctex)
        self.norm_return.set_color(YELLOW_E).scale(1.4)
        self.norm_return.to_edge(DOWN, buff = 1.3)

        self.reference = Tex(self.total_text.CAPTION13, tex_template = TexTemplateLibrary.ctex).scale(2).set_color(ORANGE)
        self.reference.move_to(self.norm_return)

    def get_warning_info(self):
        self.warning_tex = Tex(self.total_text.CAPTION14, tex_template = TexTemplateLibrary.ctex).set_color(RED_E).scale(0.6)
        PATH_WARNING = ASSETS_DIR / "思考疑问警告" / "警告.svg"
        self.warning = SVGMobject(PATH_WARNING)
        self.warning.set(height = self.warning_tex.height)
        self.warning.scale(1.6)
        self.warning.next_to(self.warning_tex, LEFT, buff = 0.27)

        grps = VGroup(self.warning_tex, self.warning)
        return grps

    def get_erase_nodes_again(self, index):
        # 还是选择当前最优, copy()代码, 哈哈, 有一定差异, 开始之前没想到的, copy代码也没问题

        moving_infos = ["1", "2", "3", "4", "5", "6"]
        nodes = ListNode.get_list_node_grps_with_index(self.scene, moving_infos)
        self.erase_nodes_again = nodes[0]
        self.erase_pointer_again = nodes[1]

        self.erase_tex_again = Tex(self.total_text.CAPTION11, tex_template = TexTemplateLibrary.ctex)
        self.erase_tex_again.set_color(MAROON_D).scale(0.8)
        self.erase_tex_again.next_to(self.erase_nodes_again[index], DOWN, buff = 0.1)
        
        self.list_node_animation.save_nodes_state(self.erase_nodes_again)

        self.erase_curves_line2_again = ListNode.get_nodes_curved_arrows(nodes[0], 3, 4, isflip=False)
        self.erase_curves_line3_again = ListNode.get_nodes_curved_arrows(nodes[0], 4, 5, isflip=False)
        self.erase_curves_line1_again = ListNode.get_nodes_curved_arrows(nodes[0], 2, 3, isflip = False)

        grps = VGroup(nodes, self.erase_tex_again, self.erase_curves_line1_again, self.erase_curves_line2_again, self.erase_curves_line3_again)
        return grps
    
    def get_thought_people(self):
        PATH_PEOPLE = ASSETS_DIR / "思考疑问警告" / "小人.svg"
        self.little_people = SVGMobject(PATH_PEOPLE)

        PATH_THOUGHT = ASSETS_DIR / "思考疑问警告" / "思考.svg"
        self.thought = SVGMobject(PATH_THOUGHT)
        self.thought.next_to(self.little_people, UP, buff = 0.12)
        self.thought.shift(RIGHT*1.12)

        thoughts = VGroup(self.little_people, self.thought)
        thoughts.scale(0.42)
        return thoughts
    
    def get_find_text(self):
        self.find_text = Tex(self.total_text.CAPTION15, tex_template = TexTemplateLibrary.ctex).set_color(BLACK)
        self.roundedrectangle = RoundedRectangle().set(width = self.find_text.width + 0.5).set_color(YELLOW_D).set_stroke(width=10)

        self.find_text_grps = VGroup(self.find_text, self.roundedrectangle)
        self.find_text_grps.scale(0.67)
        return self.find_text_grps
    
    def get_find_nodes(self):
        PATH_FIND = ASSETS_DIR / "展示代码" / "7ListFind_Sq.cpp"
        self.find_codes = MovingCode(PATH_FIND).scale(0.89)
        self.find_codes.move_to(ORIGIN)

    def get_find_curved_line(self):
        self.find_curved_line = MyCurvedLine(self.find_codes[2][3][22].get_center()+DOWN*0.07, self.find_text_grps.get_top()+UP*0.1, points=4)

    def get_travel_code(self):
        PATH_PRINT = ASSETS_DIR / "展示代码" / "8ListTraverse_Sq1.cpp"
        self.print_code = MovingCode(PATH_PRINT)

        PATH_TRAVEL = ASSETS_DIR / "展示代码" / "8ListTraverse_Sq2.cpp"
        self.travel_code = MovingCode(PATH_TRAVEL).scale(0.9)

        grps = VGroup(self.print_code, self.travel_code).arrange(DOWN)
        self.moving_print = self.print_code.get_rect(1)
        self.moving_print_svg = self.print_code.get_svg(1, 'E')

        self.moving_travel = self.travel_code.get_rect(1)
        self.moving_travel_svg = self.travel_code.get_svg(1, 'F')

        return grps
    
    def get_main_code(self):
        PATH_MAIN = ASSETS_DIR / "展示代码" / "8ListTraverse_Sq3.cpp"
        self.main_code = MovingCode(PATH_MAIN)
        self.main_code.move_to(self.print_code.get_center())
        self.main_code.scale(0.98)
        self.main_code.shift(UP*0.15)

    def get_broaden_text(self):
        self.broaden_text = Tex(self.total_text.CAPTION16, tex_template = TexTemplateLibrary.ctex).set_color(BLACK)
        self.broaden_text[0][:14].set_color(RED)
        self.broaden_text[0][47:49].set_color(RED)
        self.broaden_text.scale(0.8)

        self.roundedrectangle = RoundedRectangle().set(width = self.broaden_text.width + 0.5)
        self.roundedrectangle.set_stroke(width = 10)
        self.roundedrectangle.stretch_to_fit_height(self.broaden_text.height + 2)
        self.roundedrectangle.set_color(YELLOW_D)

        grps = VGroup(self.broaden_text, self.roundedrectangle)
        grps.to_edge(UP, buff = 0.17)

        self.reference_rec_broaden = Rectangle(height = 3.9,width = 14.2).set_color(RED)
        self.reference_rec_broaden.to_edge(DOWN, 0)

        return grps

    def get_list_brace(self):
        self.bbrace = BulletedListBrace(*self.total_text.BRACE_INFO, ).scale(0.67)
        self.bbrace.move_to(self.reference_rec_broaden.get_center())
        self.brace_title = self.bbrace.get_title(r"vector容器").set_color(BLUE_D)

        self.brace_grps = VGroup(self.bbrace, self.brace_title)
        self.brace_grps.shift(LEFT*1.89)

        text = r"详情见课本17页"
        self.brace_info = Tex(text, tex_template = TexTemplateLibrary.ctex).set_color(GREEN_E)
        self.brace_info.next_to(self.brace_grps, RIGHT, buff = 1.38)

        self.brace_curved_line = MyCurvedLine(self.brace_title.get_center()+RIGHT*1.12, self.brace_info.get_left()+LEFT*0.12, points=4)

    def get_end_info(self):
        PATH_IMAGE = ASSETS_DIR / "背景设计" / "两朵蝴蝶.jpg"
        self.image = ImageMobject(PATH_IMAGE)
        self.image.set(height = self.scene.camera.frame_height)

        self.rec = Rectangle(fill_opacity = 1, color = WHITE, width = 14.2, height = 14)

        self.end_tex = Tex(self.total_text.CAPTION17, tex_template = TexTemplateLibrary.ctex).set_color(ORANGE).scale(2)
        self.end_tex.shift(LEFT*2)

        
class ListErase_SqVideo:
    def __init__(
            self, 
            scene: Scene
    ):
        
        self.scene = scene
        self.list_node_animation = ListNodeAnimation()
        self.init = InitBasicEraseMobject(scene, self.list_node_animation)

    def first_scene(self):
        self.insert_nodes = self.init.get_insert_nodes()
        self.insert_nodes.shift(UP)

        self.erase_nodes = self.init.get_erase_nodes(1)
        self.erase_nodes.shift(DOWN*1.8)

        self.scene.play(
            Create(self.init.insert_single_node),
        )
        self.scene.play(
            FadeIn(self.init.insert_nodes)
        )

        self.scene.play(
            self.init.insert_single_node.animate.move_to([self.init.insert_nodes[0].get_center()[0], self.init.insert_single_node.get_center()[1], 0]),
            Create(self.init.erase_nodes)
        )
        self.scene.wait()
        self.scene.play(
            Write(self.init.erase_tex),
            self.init.insert_single_node.animate.move_to([self.init.insert_nodes[3].get_center()[0], self.init.insert_single_node.get_center()[1], 0])
        )
        self.scene.wait()

    def second_scene(self):
        
        self.scene.play(
            self.list_node_animation.transform_nodes(self.init.insert_nodes, 4, 5, self.init.insert_curves_line1, "NULL", "5")
        )

        self.scene.wait()

        self.scene.play(
            FadeOut(self.init.insert_curves_line1),
            self.list_node_animation.transform_nodes(self.init.insert_nodes, 3, 4, self.init.insert_curves_line2, "NULL", "4"),
            # self.list_node_animation.transform_nodes(self.init.erase_nodes, ),
            self.init.erase_tex.animate.move_to([self.init.erase_nodes[3].get_center()[0], self.init.erase_tex.get_center()[1], 0]),
        )


        self.scene.play(
            self.list_node_animation.transform_nodes(self.init.erase_nodes, 3, 4, self.init.erase_curves_line1, "5", "5")
        )

        self.scene.play(
            FadeOut(self.init.erase_curves_line1),
            FadeOut(self.init.insert_curves_line2),
            self.list_node_animation.insert_node(self.init.insert_nodes, 3, self.init.insert_single_node, "6"),
            self.list_node_animation.transform_nodes(self.init.erase_nodes, 4, 5, self.init.erase_curves_line2, "6", "6")
        )

        self.scene.play(
            FadeOut(self.init.erase_curves_line2)
        )
        self.scene.wait()

        self.scene.play(
            FadeOut(self.init.insert_nodes),
            FadeOut(self.init.erase_nodes),
            FadeOut(self.init.erase_tex),
        )
        self.scene.clear()
        self.init.list_node_animation.restore_nodes()
    
    def third_scene(self):
        self.init.get_realloc_erase_code()

        self.scene.play(
            FadeIn(self.init.realloc_code),
            FocusOn(self.init.realloc_code[2][4][29])
        )

        self.scene.play(
            FocusOn(self.init.realloc_code[2][0][5])
        )
        self.scene.wait(0.7)

        self.scene.play(
            FadeOut(self.init.realloc_code)
        )

        self.scene.wait(0.7)

    def fourth_scene(self):

        self.init.get_normal_code()
        self.scene.play(
            FadeIn(self.init.normal_code)
        )
        self.scene.wait()

        self.scene.play(
            FocusOn(self.init.normal_code[2][1][11])
        )

        self.scene.play(
            FocusOn(self.init.normal_code[2][1][11])
        )
        self.scene.play(
            FocusOn(self.init.normal_code[2][1][20])
        )

        self.scene.play(
            FocusOn(self.init.normal_code[2][8][13])
        )
        self.scene.play(
            FocusOn(self.init.normal_code[2][2][18])
        )

        self.scene.play(
            self.init.normal_code.animate.to_edge(UP, buff = 0.1)
        )

        self.scene.wait()

        self.scene.play(
            Write(self.init.norm_return)
        )
        self.scene.play(
            self.init.norm_return.animate.scale(0.88).set_color(GREEN).set_fill(opacity = 0.4)
        )
        self.scene.wait()

        self.scene.play(
            FocusOn(self.init.normal_code[2][0][48]),
            ReplacementTransform(self.init.norm_return, self.init.reference)
        )

        self.scene.wait()
        self.scene.play(
            FocusOn(self.init.normal_code[2][3][6])
        )
        self.scene.wait()

        self.scene.play(FadeOut(self.init.reference))

    def fifth_scene(self):
        # self.init.get_normal_code()
        grps = self.init.get_erase_nodes_again(4)
        grps.to_edge(DOWN, buff = 0.4)

        # self.init.normal_code.to_edge(UP, 0.1)
        # self.scene.add(self.init.normal_code)

        warning_grps = self.init.get_warning_info()
        warning_grps.next_to(self.init.normal_code, DOWN, buff = 0.8)

        thought_people = self.init.get_thought_people()
        thought_people.next_to(self.init.normal_code, DOWN, buff = 0.08)

        self.scene.play(
            FadeIn(self.init.erase_nodes_again),
        )
        self.scene.play(
            Write(self.init.erase_tex_again)
        )

        self.scene.play(
            self.init.erase_tex_again.animate.move_to([self.init.erase_nodes_again[2].get_center()[0], self.init.erase_tex_again.get_center()[1], 0])
        )

        self.scene.play(
            self.list_node_animation.transform_nodes(self.init.erase_nodes_again, 2, 3, self.init.erase_curves_line1_again, "4", "4")
        )
        self.scene.wait()
        self.scene.play(
            FadeOut(self.init.erase_curves_line1_again),
            self.list_node_animation.transform_nodes(self.init.erase_nodes_again, 3, 4, self.init.erase_curves_line2_again, "5", "5")
        )
        self.scene.wait()
        self.scene.play(
            FadeOut(self.init.erase_curves_line2_again),
            self.list_node_animation.transform_nodes(self.init.erase_nodes_again, 4, 5, self.init.erase_curves_line3_again, "6", "6")
        )
        self.scene.play(
            FadeOut(self.init.erase_curves_line3_again)
        )
        self.scene.wait(0.5)

        self.scene.wait(4.8)

        self.normal_rect = self.init.normal_code.get_rect(8)

        self.scene.play(
            FadeIn(self.normal_rect)
        )
        self.scene.play(
            FocusOn(self.init.normal_code[2][8][13]),
            FadeIn(self.init.warning)
        )
        self.scene.wait(0.5)
        self.scene.play(
           FocusOn(self.init.erase_nodes_again[5]),
           Write(self.init.warning_tex),
           Wiggle(self.init.warning)
        )
        self.scene.wait()

        self.scene.play(
            FadeOut(self.normal_rect),
            FadeOut(self.init.erase_tex_again),
            FadeOut(warning_grps)
        )


        self.scene.play(
            FadeIn(self.init.little_people)
        )
        self.scene.play(
            FadeIn(self.init.thought)
        )
        self.scene.wait(3)

        self.scene.play(
            FadeOut(self.init.erase_nodes_again), 
            FadeOut(self.init.little_people),
            FadeOut(self.init.thought)
        )
        self.scene.play(
            FadeOut(self.init.normal_code)
        )

        self.scene.wait()

    def sixth_scene(self):
        self.init.get_find_nodes()
        self.find_text = self.init.get_find_text()

        self.scene.play(
            FadeIn(self.init.find_codes)
        )
        self.scene.wait(2)

        self.scene.play(
            FocusOn(self.init.find_codes[2][2][15])
        )
        self.scene.wait(2)

        self.scene.play(
            FocusOn(self.init.find_codes[2][3][22])
        )        

        self.scene.wait(0.5)
        self.scene.play(
            FocusOn(self.init.find_codes[2][5][15])
        )

        self.scene.play(
            FocusOn(self.init.find_codes[2][8][15])
        )
        self.find_text.move_to(ORIGIN)
        self.find_text.to_edge(DOWN,buff = 0.67)

        self.scene.play(
            FadeIn(self.find_text),
            self.init.find_codes.animate.to_edge(UP, buff = 0.32)
        )

        self.init.get_find_curved_line()
        self.scene.play(
            self.init.find_curved_line.create()
        )
        self.scene.wait(3.5)

        self.scene.play(
            self.init.find_curved_line.fadeout()
        )

        self.scene.wait()
        self.scene.play(
            FadeOut(self.init.find_text_grps),
            FadeOut(self.init.find_codes)
        )

    def seven_scene(self):
        self.init.get_travel_code()

        self.scene.play(
            FadeIn(self.init.print_code)
        )
        self.scene.wait()
        self.scene.play(
            FadeIn(self.init.travel_code)
        )

        self.scene.play(
            FadeIn(self.init.moving_print),
            FadeIn(self.init.moving_print_svg)
        )
        self.scene.wait()

        self.scene.play(
            FadeIn(self.init.moving_travel),
            FadeIn(self.init.moving_travel_svg)
        )

        self.scene.wait()
        self.scene.play(
            FocusOn(self.init.travel_code[2][4][18])
        )

        self.scene.play(
            FadeOut(self.init.moving_print),
            FadeOut(self.init.moving_print_svg),
            self.init.travel_code.transform_both_svg_and_rectangle(self.init.moving_travel, self.init.moving_travel_svg, 1, 1)
        )
        self.scene.play(
            FocusOn(self.init.travel_code[2][0][41])
        )
        self.scene.wait()

        self.init.get_main_code()
        self.scene.play(
            ReplacementTransform(self.init.print_code, self.init.main_code)
        )
        self.scene.play(
            FocusOn(self.init.main_code[2][3][4])
        )

        self.scene.wait()

        self.scene.play(
            FadeOut(self.init.main_code),
            FadeOut(self.init.moving_travel),
            FadeOut(self.init.moving_travel_svg),
            FadeOut(self.init.travel_code)
        )

        self.scene.clear()
    
    def eight_scene(self):
        grps = self.init.get_broaden_text()
        self.init.get_list_brace()

        grps.save_state()
        grps.move_to(ORIGIN)

        self.scene.play(
            Succession(
                FadeIn(self.init.roundedrectangle),
                Write(self.init.broaden_text)
            )
        )
        self.scene.wait(5)
        self.scene.play(Restore(grps))
        self.scene.wait()

        self.scene.play(
            FadeIn(self.init.bbrace)
        )

        self.scene.play(
            FadeIn(self.init.brace_title)
        )
        self.scene.wait(2)

        self.scene.play(
            Write(self.init.brace_info)
        )

        self.scene.wait()
        self.scene.play(
            self.init.brace_curved_line.create()
        )

        self.scene.wait(4)

        self.scene.play(
            self.init.brace_curved_line.fadeout(),
            FadeOut(self.init.brace_curved_line.arrows)
        )
        self.scene.wait()
        self.scene.play(
            FadeOut(self.init.brace_info)
        )

        self.scene.play(
            FadeOut(self.init.brace_grps),
            FadeOut(grps)
        )

        self.scene.clear()

    def nine_scene(self):
        self.init.get_end_info()

        PATH_END = ASSETS_DIR / "音效" / "结束音效.mp3"
        self.scene.add_sound(PATH_END, gain = 1.32)
        
        self.scene.play(
            FadeIn(self.init.rec),
            FadeIn(self.init.image),
        )

        self.scene.play(
            Write(self.init.end_tex)
        )
        self.scene.wait(4)

