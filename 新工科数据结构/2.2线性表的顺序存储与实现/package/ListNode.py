from cycler import cycle
from manim import(
    RoundedRectangle, MathTex,VGroup, SVGMobject, Tex, TexTemplateLibrary,
    Create, Succession, AnimationGroup, ReplacementTransform, Restore,
    RIGHT, DOWN, UP, LEFT, 
    BLACK, GREEN_D, TEAL, MAROON,
    Scene,
    PI,
)
from .MyCurvedLine import MyCurvedLine

from pathlib import Path
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

class ListNode(RoundedRectangle):
    cycle_color = cycle(["#FFE4E1 ","#DDA0DD","#7CFC00","#FFFF77","#33FFFF","#F08080","#5599FF","#FFAA33","#FFC0CB","#BC8F8F"])

    def __init__(
            self,
            corner_radius = 0.14,
            height = 1.4,
            width = 2.1,
            stroke_width = 10,
            **kwargs,
    ):
        super().__init__(
            corner_radius=corner_radius,
            width = width,
            height = height,
            stroke_width = stroke_width,
            **kwargs
        )
        self.node_normal_color = "#FFE4E1"
        self.stroke_width = stroke_width
        self.set_stroke(color = BLACK, opacity = 0.9)
        self.set_fill(color = self.node_normal_color, opacity=1)

        self.set_info(isinit=True)
        self.scale(0.7)
    def scale(self, scale_factor:float, **kwargs):
        self.remove(self.submobjects[0])
        self.set_stroke(width = scale_factor * self.stroke_width)
        self.add(self.tex)
        return super().scale(scale_factor, **kwargs)
    
    def get_cycle_color(self):
        # 追求的是颜色的专一性还是颜色的多样性?
        cycle_color = cycle(["#FFE4E1 ","#DDA0DD","#7CFC00","#FFFF77","#33FFFF","#F08080","#5599FF","#FFAA33","#FFC0CB","#BC8F8F"])
        color_name = {
            "#FFE4E1": "米色",
            "#DDA0DD": "浅紫色",
            "#7CFC00": "浅绿色",
            "#FFFF77": "浅黄色",
            "#33FFFF": "青蓝色",
            "#F08080": "浅红色",
            "#5599FF": "浅蓝色",
            "#FFAA33": "棕黄色",
            "#FFC0CB": "浅粉色",
            "#BC8F8F": "淡棕色"
        }
        return (cycle_color, list(color_name.values()))

    def set_info(self, info = "1",height = 0.3, width = None, isinit = False):
        """
            用来设置节点信息的.
            isinit:判断是否初始化, 
        """
        if not isinit:
            self.remove(self.submobjects[0])
        tex = MathTex(info)

        if height is not None:
            tex.set(height = height)
        if width is not None:
            tex.set(width = width)

        if tex.height > self.height:
            tex.set(height = self.height - 0.2)
        if tex.width > self.width:
            tex.set(width = self.width - 0.2)

        tex.move_to(self.get_center())
        tex.set_color(self.stroke_color)
        self.tex = tex

        self.add(tex)
        return self
    
    def change_info(self, change_info = "1", height = 0.3, width = None):
        # 更换节点信息
        self.set_info(change_info, height, width)

    def set_node_color(self):
        # 多样化设置节点颜色
        self.remove(self.submobjects[0])
        self.set_fill(color = next(ListNode.cycle_color))
        self.add(self.tex)
        return self
    
    def remove_node_color(self):
        # 恢复成默认节点颜色
        self.remove(self.submobjects[0])
        self.set_fill(color = self.node_normal_color)
        self.add(self.tex)
        return self
    
    @staticmethod
    def get_listnode_grps(infos: list, scene:Scene):
        # 得到节点组
        grps = VGroup(*[
            ListNode().set_info(info).set_node_color()
            for info in infos
        ]).arrange(RIGHT, buff = 0)
        grps.set(width = scene.camera.frame_width - 1)

        return grps
    
    @staticmethod    
    def get_array_index(list_node_grps, indexes):
        digits = VGroup(*[
            MathTex(f"{index}").next_to(node, DOWN, buff = 0.05).scale(0.4).set_color(GREEN_D)
            for index, node in zip(indexes, list_node_grps)
            if index != ""
        ])

        return digits
    
    
    @staticmethod
    def get_list_node_grps_with_index(
        scene: Scene, 
        node_infos: list, 
        index_infos: list = None, 
    ):
        # 这个方法是固定的, 独属于ListInsert, ListErase视频的, 其他情况最好不要使用
        list_grps = ListNode.get_listnode_grps(node_infos, scene)
        list_grps.set(width = scene.camera.frame_width - 5)

        tex = Tex(r"首地址\\L.base", tex_template = TexTemplateLibrary.ctex).scale(0.4).set_color(TEAL)

        PATH_POINTER = ASSETS_DIR / "ListNode" / "指针.svg"
        pointer = SVGMobject(PATH_POINTER)
        pointer.scale(0.37)
        pointer.rotate(-PI/2)
        pointer.next_to(list_grps[0], LEFT, buff = 0.15)
        pointer.shift(UP*0.3)
        tex.next_to(pointer, DOWN, buff = 0.1)
        tex.shift(LEFT*0.1)        
        pointer_with_tex = VGroup(pointer, tex)
        if index_infos is not None:
            index_digits = ListNode.get_array_index(list_grps, index_infos)
            grps = VGroup(list_grps, index_digits, pointer_with_tex)
        else:
            grps = VGroup(list_grps, pointer_with_tex)


        return grps
    
    @staticmethod
    def scale_single_node_infos(nodes: VGroup, index = 0, scale_factor = 0.4):
        # 这里默认的只是结点组, 而不是其他组的整合
        nodes[index].tex.scale(scale_factor)

    @staticmethod
    def scale_nodes_infos(nodes: VGroup, indexes:list, scale_factors:list):

        for index, scale_factor in zip(indexes, scale_factors,):
            ListNode.scale_single_node_infos(nodes, index, scale_factor)
    
    @staticmethod
    def get_nodes_curved_arrows(nodes, index1, index2, isflip = True, direction = UP*0.5):
        m = MyCurvedLine(nodes[index1].get_top(), nodes[index2].get_top()).get_curved_arrows(isflip = isflip, color = MAROON)

        if not isflip:
            m.flip(UP)
            m.flip(RIGHT)
        m.shift(direction)
        return m
            



class ListNodeAnimation:
    """
            这里本来想继承ListNode, 但是上面产生的是Mobject, 子类却是产生动画, 
        属性上不太相关. 而且我也只是想封装一些动画, 要是继承的话, 创建对象时还需要
        添加父类相关属性, 偏离的我实际想法.
            所以打算采用组合的方式专门为该对象封装其对应的动画, 从而能达到我自己
        想要的效果
            做这一点的原因是因为在写ListInsert动画的时候, 采取贪心思想, 每步选择当前最优
        随着代码量的提高, 我发现重复代码也升高了. 但是陷进去了, 写了几百行, 没法出来,
        只能硬着头皮继续写. 等写完复盘发现, 不如将这些功能封装起来, 减少代码量.
            我也没有开天眼, 也是第一次尝试去做, 并不确定后续是否会添加相同代码, 也
        算是经验积累吧.不过站在全局的角度来看, 我现在其实仍然是动态规划着来的, 要不然
        ListErase也一直重复写, 贪心到底了.
    """
    saved_mob = []
    def __init__(
        self,
    ):
        pass

    def save_nodes_state(self, nodes,):
        if isinstance(nodes, ListNode):
            nodes.save_state()
        else:
            for node in nodes:
                node.save_state()

    def transform_nodes(self, nodes, index1, index2,curved_line, change_info1:str, change_info2:str):
        ListNodeAnimation.saved_mob.append(nodes[index1])
        ListNodeAnimation.saved_mob.append(nodes[index2])

        return Succession(
            Create(curved_line),
            AnimationGroup(
                ReplacementTransform(nodes[index1].copy(), nodes[index2]),
                nodes[index1].animate.change_info(change_info1),
                nodes[index2].animate.change_info(change_info2),
            )
        )
    
    def insert_node(self, nodes, index, single_node, change_info: str):
        return AnimationGroup(
            ReplacementTransform(single_node, nodes[index]),
            nodes[index].animate.change_info(change_info)
        )

    def restore_nodes(self,):
        animations = []
        for mob in ListNodeAnimation.saved_mob:
            animations.append(Restore(mob))

        ListNodeAnimation.saved_mob.clear()
        return AnimationGroup(*animations)
    



    