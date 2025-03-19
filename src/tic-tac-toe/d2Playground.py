import matplotlib.pyplot as plt


class D2Playground:
    def __init__(self):
        self.circle = [[], []]
        self.cross = [[], []]
        self.circle_point = []
        self.cross_point = []
        self.circle_color = "#f00"
        self.cross_color = "#00f"

        self.next_player = "cross"

    def Place(self, x, y):
        if self.next_player == "circle":
            self.circle_point.append([x, y])
            x -= 0.5
            y -= 0.5
            self.circle[0].append(x)
            self.circle[1].append(y)
            self.next_player = "cross"
        elif self.next_player == "cross":
            self.cross_point.append([x, y])
            x -= 0.5
            y -= 0.5
            self.cross[0].append(x)
            self.cross[1].append(y)
            self.next_player = "circle"
        else:
            pass

    def Reset(self):
        self.circle = [[], []]
        self.cross = [[], []]
        self.circle_point = []
        self.cross_point = []
        self.next_player = "cross"

    def CheckWinner(self):
        for i in range(1, 4):
            if (
                [i, 1] in self.circle_point
                and [i, 2] in self.circle_point
                and [i, 3] in self.circle_point
            ):
                return "circle"
            if (
                [i, 1] in self.cross_point
                and [i, 2] in self.cross_point
                and [i, 3] in self.cross_point
            ):
                return "cross"

        for i in range(1, 4):
            if (
                [1, i] in self.circle_point
                and [2, i] in self.circle_point
                and [3, i] in self.circle_point
            ):
                return "circle"
            if (
                [1, i] in self.cross_point
                and [2, i] in self.cross_point
                and [3, i] in self.cross_point
            ):
                return "cross"

        if (
            [1, 1] in self.circle_point
            and [2, 2] in self.circle_point
            and [3, 3] in self.circle_point
        ):
            return "circle"
        if (
            [1, 3] in self.circle_point
            and [2, 2] in self.circle_point
            and [3, 1] in self.circle_point
        ):
            return "circle"
        if (
            [1, 1] in self.cross_point
            and [2, 2] in self.cross_point
            and [3, 3] in self.cross_point
        ):
            return "cross"
        if (
            [1, 3] in self.cross_point
            and [2, 2] in self.cross_point
            and [3, 1] in self.cross_point
        ):
            return "cross"

        if len(self.circle_point) + len(self.cross_point) == 9:
            return "draw"

        return "none"

    def CheckPlaceable(self, x, y):
        if [x, y] in self.circle_point:
            return False
        if [x, y] in self.cross_point:
            return False
        return True

    def RenderPlayground(self, circle, cross):
        figure = plt.figure(figsize=(6, 6))
        ax = plt.subplot()
        ax.set_title("OOXX", fontsize=20)
        ax.set_xlabel(
            "$X$",
            fontdict={"size": 15, "color": "#f00", "family": "Times New Roman"},
            labelpad=10,
        )
        ax.set_ylabel(
            "$Y$",
            fontdict={"size": 15, "color": "#0f0", "family": "Times New Roman"},
            labelpad=10,
        )

        ax.tick_params(
            axis="x", which="major", pad=0, colors="#f00", labelsize=10, labelrotation=0
        )
        ax.tick_params(
            axis="y", which="major", pad=0, colors="#0f0", labelsize=10, labelrotation=0
        )

        ax.set_xticks([0, 1, 2, 3])
        ax.set_yticks([0, 1, 2, 3])

        ax.autoscale(False)
        ax.grid(linestyle="--", linewidth=1, alpha=0.5, color="grey")
        ax.scatter(circle[0], circle[1], s=500, color="#f00", marker="o")
        ax.scatter(cross[0], cross[1], s=500, color="#00f", marker="x")

        if __name__ == "__main__":
            plt.show()
        else:
            return figure


if __name__ == "__main__":
    pg = D2Playground()
    pg.circle = [[1.5, 0.5], [0.5, 0.5], [0.5, 2.5]]
    pg.cross = [[1.5, 0.5], [1.5, 1.5], [1.5, 2.5]]
    pg.RenderPlayground(pg.circle, pg.cross)
