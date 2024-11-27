import random

def print_board(board):
    # ヘッダー（列番号）
    col_numbers = "   " + " ".join(f"{i:2}" for i in range(len(board)))
    print(col_numbers)
    for idx, row in enumerate(board):
        # 行番号を表示してボードを描画
        print(f"{idx:2} " + " ".join(row))
    print()

def check_winner(board, player):
    n = len(board)

    # 横
    for row in board:
        if "".join(row).find(player * 5) != -1:
            return True

    # 縦
    for col in range(n):
        column = [board[row][col] for row in range(n)]
        if "".join(column).find(player * 5) != -1:
            return True

    # 斜め（右下方向）
    for row in range(n - 4):
        for col in range(n - 4):
            if all(board[row + i][col + i] == player for i in range(5)):
                return True

    # 斜め（右上方向）
    for row in range(4, n):
        for col in range(n - 4):
            if all(board[row - i][col + i] == player for i in range(5)):
                return True

    return False

def get_computer_move(board):
    empty_cells = [(row, col) for row in range(len(board)) for col in range(len(board)) if board[row][col] == "."]
    return random.choice(empty_cells)

def main():
    n = 10  # ボードサイズ
    board = [["." for _ in range(n)] for _ in range(n)]

    print("五目並べゲームへようこそ！")
    print("座標は行と列の番号で指定してください（例: 3 4）。")
    print_board(board)

    human = "X"
    computer = "O"

    turn = "human"  # 最初は人間プレイヤーのターン

    while True:
        if turn == "human":
            print("あなたのターン（X）。")
            try:
                row, col = map(int, input("行と列をスペースで区切って入力してください (例: 3 4): ").split())
                if not (0 <= row < n and 0 <= col < n):
                    print(f"範囲外です。0 から {n - 1} の間で選んでください。")
                    continue
                if board[row][col] != ".":
                    print("そのマスは既に埋まっています。別のマスを選んでください。")
                    continue
                board[row][col] = human
            except (ValueError, IndexError):
                print("正しい形式で入力してください。")
                continue

            if check_winner(board, human):
                print_board(board)
                print("おめでとう！ あなたの勝利です！")
                break

            turn = "computer"
        else:
            print("コンピューターのターン（O）。")
            row, col = get_computer_move(board)
            board[row][col] = computer

            if check_winner(board, computer):
                print_board(board)
                print("残念！ コンピューターが勝ちました。")
                break

            turn = "human"

        print_board(board)

        # 引き分け判定（空きマスがない場合）
        if all(cell != "." for row in board for cell in row):
            print("引き分けです！")
            break

if __name__ == "__main__":
    main()

