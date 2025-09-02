from manim import(
    VGroup, Line,
    Create, TransformFromCopy,
    ORIGIN, UP, DOWN,
    BLACK,
    Scene,
    config, linear, rotate_vector, DEFAULT_STROKE_WIDTH, DEGREES
)

class BigTree(VGroup):
    def __init__(
            self,
            scene:Scene,
            initial_length = 3,
            iterations = 15,
            tree_color = BLACK,
            run_time = 0,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.scene = scene
        self.tree_color = tree_color
        self.iterations = iterations
        self.run_time = run_time

        self.vector = UP
        self.points_path = [ORIGIN]
        self.level = 0
        self.INITIAL_LENGTH = initial_length


    def create_tree(self, scale_factor = 1, direction = DOWN, buff = 0.23):
        self.tree(self.INITIAL_LENGTH, iterations=self.iterations)

        self.height = config.frame_height - 1
        self.scale(scale_factor)
        self.move_to(ORIGIN)
        self.to_edge(edge=direction, buff = buff)
        self.scene.play(Create(self[0], rate_func = linear, run_time = 1))
        
        for i in range(len(self) - 1):
            branch_length = self[i][-1].get_length() + self.run_time
            self.scene.play(
                TransformFromCopy(
                    self[i],
                    self[i+1],
                    rate_func = linear,
                    run_time = 1.5*branch_length / self.INITIAL_LENGTH
                )
            )
    def tree(self, length, left=25, right=50, iterations=3):
        if iterations == 0:
            return
        if len(self) == self.level:
            self.add(VGroup())
        self.level +=1
        self.forward(length)
        self.right(left)
        self.tree(length*0.9, left, right, iterations-1)
        self.left(right)
        self.tree(length*0.9, left, right, iterations-1)
        self.right(left)
        self.backward()
        self.level -=1

    def left(self, angle):
        self.vector = rotate_vector(self.vector, angle * DEGREES)

    def right(self, angle):
        self.left(-angle)

    def forward(self, length):
        stroke_width = DEFAULT_STROKE_WIDTH * 0.8**(self.level)
        last_point = self.points_path[-1]
        self.points_path.append( last_point + self.vector * length )
        self[self.level-1].add(Line(*self.points_path[-2:], stroke_width=stroke_width, color = self.tree_color))
    
    def backward(self):
        self.points_path.pop() 