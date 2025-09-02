class VideoText:
    def __init__(
            self,
    ):
        self.opening_animation_text()
        self.head_file_text()
        self.insert_animation_text()
        self.chapter_animation_text()
        self.erase_animation_text()
        self.find_animation_text()
        self.broaden_animation_text()
        self.end_animation_text()

    def opening_animation_text(self):
        self.START_TEX = r"""
            \begin{tabular}{p{8cm}}
            \hspace{1em}
            “形而上者谓之道，形而下者谓之器。”
            \end{tabular}
        """

        self.AUTHER_TEX = r"""
            \begin{tabular}{p{8cm}}
            \hspace{1em}
            ————《易经$\bullet$系辞》
            \end{tabular}
        """

        self.EXPLAIN_TEX = r"""
            \begin{tabular}{p{8cm}}
            \hspace{1em}
            详见课本19页，中华传统文化中的抽象思维。
            \end{tabular}
        """
    def head_file_text(self):
        self.TOTAL_TEX = [
            r"InitList(\&L)",
            r"DestroyList(\&L)",
            r"ListInsert(\&L, i, e)",
            r"ListErase(\&L, i, \&e)",
            r"ListClear(\&L)",
            r"ListAssign(L, i, value)",
            r"ListEmpty(L)",
            r"ListSize(L)",
            r"ListGetElem(L, i \&e)",
            r"ListFind(L, e)",
            r"ListTraverse(L, visit())"
        ]

        self.TITLE = r"线性表\\基本操作方法"

        self.CAPTION1 = r"""
            可暂停了解,\\
            详情见课本14页
        """

        self.CAPTION2 = r"""
            \&
        """
        self.CAPTION3 = r"""
            Sequential
        """
    def insert_animation_text(self):
        self.CAPTION4 = r"i = 1"
        self.CAPTION5 = r"i = 0"

        self.CAPTION6 = [
            r"L.size - 1",
            r" - ",
            r"i",
            r" = 0"
        ]

        self.CAPTION7 = [
            r"L.size - 1",
            r" - ",
            r"i",
            r" = 1"
        ]

        self.CAPTION8 = r"L.size - 1"

        self.CAPTION9 = r"position"

        self.CAPTION10 = r"i < 0 与 i >= L.size - 1"

    def chapter_animation_text(self):
        r"""
        \tiny:非常小
        \scriptsize:比 \tiny 大一点
        \footnotesize:脚注大小
        \small:较小
        \normalsize:正常大小(默认大小)
        \large:大号
        \Large:更大号
        \huge:非常大
        \Huge:最大号
        """
        self.chapter1 = r"{\Large 线性表的}\\{\Huge 顺序存储}"
        self.chapter2 = r"{\Large 线性表的}\\{\Huge 初始化}"
        self.chapter3 = r"{\Large 线性表的}\\{\Huge 销毁与清空}"
        self.chapter4 = r"{\Large 线性表的}\\{\Huge 插入}"
        self.chapter5 = r"{\Large 线性表的}\\{\Huge 删除}"
        self.chapter6 = r"{\Large 线性表的}\\{\Huge 查找定位}"
        self.chapter7 = r"{\Large 线性表的}\\{\Huge 遍历输出}"
        self.chapter8 = r"{\Huge 拓展}"

    def erase_animation_text(self):

        self.CAPTION11 = "Erase"
        self.CAPTION12 = r"return\hspace{1em}e"
        self.CAPTION13 = r"\&"
        self.CAPTION14 = r"并不是表尾, 而是表尾后的一个空间."

    def find_animation_text(self):
        
        self.CAPTION15 = r"""
                            \begin{tabular}{p{5 cm}}
                            \hspace{1em}
                            简单数据类型可使用“==”，抽象数据类型需重载“==”,比如Python或C++, 
                            而Java需重写.equals()方法.
                            \end{tabular}
                        """
    def broaden_animation_text(self):
        self.CAPTION16 = r"""
                            \begin{tabular}{p{9cm}}
                            \hspace{1em}
                            C++的标准库模版(STL)：STL是一个高效的C++程序库，当中包含了诸多常用数据结构（亦称容器）和算法的实现，
                            为C++程序员们提供了一个可拓展的应用框架，高度体现了软件的可复用性。
                            \end{tabular}
                        """
        
        self.BRACE_INFO = [
            r"v.size()",
            r"v.push\_back(e)",
            r"v.insert(v.begin()+k,e)",
            r"v.pop\_back()",
            r"v.erase(v.begin()+k)",
            r"v.clear()"
        ]
    def end_animation_text(self) :
        self.CAPTION17 = r"感谢观看！"