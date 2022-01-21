import win32gui
import win32api
import win32con

class Rect:
    def __init__(self):
        self.left, self.top, self.right, self.bottom = 0, 0, 0, 0
    
    def set(self, rect):
        top, left, right, bottom = rect
        self.left, self.top, self.right, self.bottom = top, left, right, bottom

class Window:
    CLICK_TIME = 40
    MOUSE_MOVE_DELAY = 15
    
    def space_press():
        return win32api.GetAsyncKeyState(win32con.VK_SPACE)
    
    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.Sleep(Window.MOUSE_MOVE_DELAY)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.Sleep(Window.CLICK_TIME)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    
    def get_terraria_dim():
        terraria_rect = Rect()
        def found_terraria(hwnd, param):
            s = win32gui.GetWindowText(hwnd)
            if s.find('Terraria') == 0:
                terraria_rect.set(win32gui.GetWindowRect(hwnd))
        win32gui.EnumWindows(found_terraria, 0)
        return terraria_rect
    
def main():
    w = Window()
    w.get_terraria_dim()

if __name__ == '__main__':
    main()