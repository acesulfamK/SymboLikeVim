import curses
from editor import Editor 

class UI:
    text = [""]
    mode = 'NORMAL'
    cursor_x = 0
    cursor_y = 0
    def __init__(self):
        editor = Editor()

    def main_loop(self, stdscr):
        curses.curs_set(1)
        stdscr.clear()
        stdscr.refresh()
        self.text = [""]
        
        while True:
            stdscr.clear()

            # モードとテキストの表示
            stdscr.addstr(0, 0, f"Mode: {self.mode}")
            for i, line in enumerate(self.text):
                stdscr.addstr(i + 1, 0, line)
    
            # カーソルの表示
            stdscr.move(self.cursor_y + 1, self.cursor_x)
            stdscr.refresh()
    
            key = stdscr.getch()
    
            if self.mode == 'NORMAL':
                if key == ord('i'):
                    self.mode = 'INSERT'
                    curses.curs_set(2)  # インサートモードではカーソルを表示
                elif key == ord('q'):
                    break  # 'q'で終了
                elif key in [ord('h'), ord('j'), ord('k'), ord('l')]:
                    self.move_cursor(key)
            elif self.mode == 'INSERT':
                if key == 27:  # Escキー
                    self.mode = 'NORMAL'
                    curses.curs_set(1)  # ノーマルモードではカーソルを非表示
                elif key == curses.KEY_ENTER or key == 10 or key == 13:
                    self.text.insert(self.cursor_y + 1, "")
                    self.cursor_y += 1
                    self.cursor_x = 0
                elif key == curses.KEY_BACKSPACE or key == 127:
                    if self.cursor_x > 0:
                        self.text[self.cursor_y] = self.text[self.cursor_y][:self.cursor_x - 1] + self.text[self.cursor_y][self.cursor_x:]
                        self.cursor_x -= 1
                    elif self.cursor_y > 0:
                        self.cursor_y -= 1
                        self.cursor_x = len(self.text[self.ursor_y])
                        self.text[self.cursor_y] += self.text.pop(self.cursor_y+ 1)
                elif (key == curses.KEY_LEFT or key == curses.KEY_RIGHT or 
                      key == curses.KEY_UP or key == curses.KEY_DOWN):
                    self.move_cursor(key)
                else:
                    self.text[self.cursor_y] = (self.text[self.cursor_y][:self.cursor_x] + 
                        chr(key) + self.text[self.cursor_y][self.cursor_x:])
                    self.cursor_x += 1
            
    def move_cursor(self, key):
        if key == ord('h'):
            if self.cursor_x > 0:
                self.cursor_x -= 1
        elif key == ord('l'):
            if self.cursor_x < len(self.text[self.cursor_y]):
                self.cursor_x += 1
        elif key == ord('k'):
            if self.cursor_y > 0:
                self.cursor_y -= 1
                self.cursor_x = min(self.cursor_x, len(self.text[self.cursor_y]))
        elif key == ord('j'):
            if self.cursor_y < len(self.text) - 1:
                self.cursor_y += 1
                self.cursor_x = min(self.cursor_x, len(self.text[self.cursor_y]))
        return 
 
    def run(self):
        curses.wrapper(self.main_loop)
    
    
    