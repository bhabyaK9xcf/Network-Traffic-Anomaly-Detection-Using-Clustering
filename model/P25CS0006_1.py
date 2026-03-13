import glfw
from OpenGL.GL import *
import numpy as np
from PIL import Image

roll_number = "P25CS0006"


def save_screenshot(window, filename="P25CS0006_1.png"):
    width, height = glfw.get_framebuffer_size(window)

    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)

    image = np.frombuffer(data, dtype=np.uint8)
    image = image.reshape(height, width, 3)

    image = np.flipud(image)

    img = Image.fromarray(image, 'RGB')
    img.save(filename)
    print(f"Screenshot saved as {filename}")


def main():
    if not glfw.init():
        return

    window = glfw.create_window(500, 500, roll_number, None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(0.2, 0.4, 0.6, 1.0)

    screenshot_saved = False

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(-0.5, -0.5)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(0.5, -0.5)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(0.0, 0.5)
        glEnd()

        if not screenshot_saved:
            save_screenshot(window, "P25CS0006_1.png")
            screenshot_saved = True

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()