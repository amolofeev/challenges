import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QVector2D
from PyQt5.QtWidgets import QWidget, QDialog, QApplication


class Boid:
    def __init__(self, position: QVector2D):
        self.position = position
        self.velocity = QVector2D(
            random.random() * random.choice([1, -1]),
            random.random() * random.choice([1, -1])
        )

    def update(self, boids, *,
               alignment_radius: int, cohesion_radius: int, separation_radius: int,
               alignment_strength: int, cohesion_strength: int, separation_strength: int,
               speed: float
               ):

        separation = QVector2D(0, 0)
        alignment = QVector2D(0, 0)
        cohesion = QVector2D(0, 0)
        c_count = 0
        s_count = 0
        a_count = 0
        for boid in boids:
            if boid is not self:
                distance = self.position.distanceToPoint(boid.position)
                if 0 < distance <= alignment_radius:
                    alignment += boid.velocity
                    a_count += 1
                if 0 < distance <= cohesion_radius:
                    cohesion += (boid.position - self.position)
                    c_count += 1
                if 0 < distance <= separation_radius:
                    separation += ((self.position - boid.position) * (1. / distance))
        if c_count:
            cohesion /= c_count
        if s_count:
            separation /= s_count
        if a_count:
            alignment /= a_count

        acceleration = (alignment.normalized() * alignment_strength)
        acceleration += (separation.normalized() * separation_strength)
        acceleration += (cohesion.normalized() * cohesion_strength)

        self.velocity += acceleration
        self.velocity.normalize()

        self.position += self.velocity * speed


class Settings(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('settings_dialog.ui', self)


class Main(QWidget):
    w = 640
    h = 240
    alignment_radius = 5
    cohesion_radius = 25
    separation_radius = 5
    alignment_strength = 1.
    cohesion_strength = .8
    separation_strength = 1.
    speed = 3.
    debug = False
    boids_count = 200

    def print_settings(self):
        print(
            dict(
                c_r=self.cohesion_radius,
                c_s=self.cohesion_strength,
                a_r=self.alignment_radius,
                a_s=self.alignment_strength,
                s_r=self.separation_radius,
                s_s=self.separation_strength,
                speed=self.speed,
                debug=self.debug,
                count=self.boids_count
            )
        )

    def __init__(self):
        super().__init__()
        self.resize(self.w, self.h)
        self.settings = Settings()
        self.settings.show()
        self.setup_connections()

        self.boids = [
            Boid(
                QVector2D(
                    random.randint(0, self.w),
                    random.randint(0, self.h),
                )
            )
            for _ in range(500)
        ]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(16)

    def setup_connections(self):
        self.settings.alignment_radius_slider.valueChanged.connect(self.alignment_radius_changed)
        self.settings.cohesion_radius_slider.valueChanged.connect(self.cohesion_radius_changed)
        self.settings.separation_radius_slider.valueChanged.connect(self.separation_radius_changed)
        self.settings.alignment_strength_spinbox.valueChanged.connect(self.alignment_strength_changed)
        self.settings.cohesion_strength_spinbox.valueChanged.connect(self.cohesion_strength_changed)
        self.settings.separation_strength_spinbox.valueChanged.connect(self.separation_strength_changed)
        self.settings.debug_checkbox.stateChanged.connect(self.debug_changed)
        self.settings.speed_spinbox.valueChanged.connect(self.speed_changed)
        self.settings.count_slider.valueChanged.connect(self.count_changed)

    def alignment_radius_changed(self, value):
        self.alignment_radius = value
        self.print_settings()

    def cohesion_radius_changed(self, value):
        self.cohesion_radius = value
        self.print_settings()

    def separation_radius_changed(self, value):
        self.separation_radius = value
        self.print_settings()

    def alignment_strength_changed(self, value):
        self.alignment_strength = value
        self.print_settings()

    def cohesion_strength_changed(self, value):
        self.cohesion_strength = value
        self.print_settings()

    def separation_strength_changed(self, value):
        self.separation_strength = value
        self.print_settings()

    def debug_changed(self, value):
        self.debug = value
        self.print_settings()

    def speed_changed(self, value):
        self.speed = value
        self.print_settings()

    def count_changed(self, value):
        self.boids_count = value
        self.print_settings()

    def update(self):
        for boid in self.boids[:self.boids_count]:
            boid.update(
                self.boids[:self.boids_count],
                alignment_radius=self.alignment_radius, cohesion_radius=self.cohesion_radius,
                separation_radius=self.separation_radius,
                alignment_strength=self.alignment_strength, cohesion_strength=self.cohesion_strength,
                separation_strength=self.separation_strength,
                speed=self.speed,
            )
            position = boid.position

            if position.x() > self.w:
                boid.position.setX(0)
            elif position.x() < 0:
                boid.position.setX(self.w)
            if position.y() > self.h:
                boid.position.setY(0)
            elif position.y() < 0:
                boid.position.setY(self.h)

        self.repaint()

    def resizeEvent(self, e):
        self.w, self.h = e.size().width(), e.size().height()
        return super().resizeEvent(e)

    def paintEvent(self, e):
        gc = QPainter()
        gc.begin(self)

        for boid in self.boids[:self.boids_count]:
            gc.drawPoint(boid.position.toPointF())
            if self.debug:
                gc.drawEllipse(boid.position.toPointF(), 1, 1)
                gc.drawLine(boid.position.toPointF(), boid.position.toPointF() + boid.velocity.toPointF() * 3)

        gc.end()


if __name__ == '__main__':
    app = QApplication([])
    w = Main()
    w.show()
    sys.exit(app.exec_())
