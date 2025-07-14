import copy
import tkinter as tk
from tkinter import ttk
import os
os.environ["TK_USE_INPUT_METHODS"] = "0"


class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.master.geometry("540x600")
        self.master.resizable(False, False)
        self.master.update_idletasks()
        self.master.minsize(self.master.winfo_width(), self.master.winfo_height())
        style = ttk.Style(self.master)
        style.theme_use("clam")
        style.configure("TButton", font=("Helvetica", 12), padding=5)
        style.configure("Title.TLabel", font=("Helvetica", 18, "bold"))
        self.board = []
        self.possibilities = []
        self.history = []
        self.move_history = []
        self.INITIAL_SUDOKU = [
            [int(c) for c in "060030780"],
            [int(c) for c in "800009050"],
            [int(c) for c in "005000104"],
            [int(c) for c in "009004810"],
            [int(c) for c in "501080960"],
            [int(c) for c in "006700400"],
            [int(c) for c in "008000070"],
            [int(c) for c in "000000500"],
            [int(c) for c in "100400000"],
        ]
        self._create_widgets()
        self.reset_game()

    def _create_widgets(self):
        main_frame = ttk.Frame(self.master, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        ttk.Label(main_frame, text="Sudoku Solver", style="Title.TLabel").pack(pady=10)
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(pady=(0, 15))
        ttk.Button(control_frame, text="Apply Basic Logic", command=self.run_basic_strategies).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Backtrack Step", command=self.backtrack_step).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Reset", command=self.reset_game).pack(side=tk.LEFT, padx=5)
        self.grid_frame = tk.Frame(main_frame, bg="#333")
        self.grid_frame.pack()
        self.cell_labels = [[None for _ in range(9)] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                pad_x = (5, 0) if c % 3 == 0 else (1, 0)
                pad_y = (5, 0) if r % 3 == 0 else (1, 0)
                cell_frame = tk.Frame(self.grid_frame, width=50, height=50, bg="white")
                cell_frame.grid(row=r, column=c, padx=pad_x, pady=pad_y)
                cell_frame.pack_propagate(False)
                label = tk.Label(cell_frame, text="", bg="white")
                label.pack(expand=True, fill=tk.BOTH)
                self.cell_labels[r][c] = label

    def reset_game(self):
        self.board = copy.deepcopy(self.INITIAL_SUDOKU)
        self.history = []
        self.move_history = []
        self.possibilities = [[[1] * 10 for _ in range(9)] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                self.possibilities[r][c][0] = 0
                if self.board[r][c] != 0:
                    self._update_possibilities(r, c, self.board[r][c])
        self._update_board_ui()

    def _update_possibilities(self, row, col, num):
        for k in range(1, 10):
            self.possibilities[row][col][k] = 0
        for i in range(9):
            self.possibilities[row][i][num] = 0
            self.possibilities[i][col][num] = 0
        box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_start_row, box_start_row + 3):
            for c in range(box_start_col, box_start_col + 3):
                self.possibilities[r][c][num] = 0

    def _update_board_ui(self):
        for r in range(9):
            for c in range(9):
                label = self.cell_labels[r][c]
                val = self.board[r][c]
                if val != 0:
                    is_original = self.INITIAL_SUDOKU[r][c] != 0
                    label.config(
                        text=str(val),
                        font=("Helvetica", 20, "bold" if is_original else "normal"),
                        fg="#333" if is_original else "blue",
                        bg="#eee" if is_original else "white",
                    )
                else:
                    candidates = [str(k) for k in range(1, 10) if self.possibilities[r][c][k]]
                    candidates_text = "".join(candidates)
                    if len(candidates_text) > 5:
                        candidates_text = (candidates_text[:5] + "\n" + candidates_text[5:])
                    label.config(text=candidates_text, font=("Courier New", 9), fg="#777", bg="white")

    def run_basic_strategies(self):
        while True:
            board_before = copy.deepcopy(self.board)
            self._apply_basic_rules()
            if self.board == board_before:
                break
        self._update_board_ui()

    def _apply_basic_rules(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0 and sum(self.possibilities[r][c]) == 1:
                    num = self.possibilities[r][c].index(1)
                    self.board[r][c] = num
                    self._update_possibilities(r, c, num)
        for num in range(1, 10):
            for r in range(9):
                possible_placements = [c for c in range(9) if self.board[r][c] == 0 and self.possibilities[r][c][num]]
                if len(possible_placements) == 1:
                    c = possible_placements[0]
                    self.board[r][c] = num
                    self._update_possibilities(r, c, num)
            for c in range(9):
                possible_placements = [r for r in range(9) if self.board[r][c] == 0 and self.possibilities[r][c][num]]
                if len(possible_placements) == 1:
                    r = possible_placements[0]
                    self.board[r][c] = num
                    self._update_possibilities(r, c, num)
            for box_idx in range(9):
                box_r, box_c = (box_idx // 3) * 3, (box_idx % 3) * 3
                possible_placements = []
                for r_off in range(3):
                    for c_off in range(3):
                        r, c = box_r + r_off, box_c + c_off
                        if self.board[r][c] == 0 and self.possibilities[r][c][num]:
                            possible_placements.append((r, c))
                if len(possible_placements) == 1:
                    r, c = possible_placements[0]
                    self.board[r][c] = num
                    self._update_possibilities(r, c, num)

    def is_board_valid(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0 and sum(self.possibilities[r][c]) == 0:
                    return False
        return True

    def backtrack_step(self):
        if not self.is_board_valid():
            if not self.history:
                print("Backtrack history is empty. Cannot go back further.")
                return
            self.board = self.history.pop()
            self.possibilities = self.history.pop()
            last_r, last_c, last_num = self.move_history.pop()
            for new_num in range(last_num + 1, 10):
                if self.possibilities[last_r][last_c][new_num]:
                    self._make_guess(last_r, last_c, new_num)
                    return
            self.backtrack_step()
        else:
            self._find_and_make_next_guess()

    def _find_and_make_next_guess(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    for num in range(1, 10):
                        if self.possibilities[r][c][num]:
                            self._make_guess(r, c, num)
                            return
        print("Sudoku solved or no empty cells left!")

    def _make_guess(self, r, c, num):
        self.history.append(copy.deepcopy(self.possibilities))
        self.history.append(copy.deepcopy(self.board))
        self.move_history.append((r, c, num))
        self.board[r][c] = num
        self._update_possibilities(r, c, num)
        self._update_board_ui()


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
