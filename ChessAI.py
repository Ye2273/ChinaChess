import copy
from ChessBoard import *

class Evaluate(object):
    # 棋子棋力得分
    single_chess_point = {
        'c': 989,   # 车
        'm': 439,   # 马
        'p': 442,   # 炮
        's': 226,   # 士
        'x': 210,   # 象
        'z': 55,    # 卒
        'j': 65536  # 将
    }
    # 红兵（卒）位置得分
    red_bin_pos_point = [
        [1, 3, 9, 10, 12, 10, 9, 3, 1],
        [18, 36, 56, 95, 118, 95, 56, 36, 18],
        [15, 28, 42, 73, 80, 73, 42, 28, 15],
        [13, 22, 30, 42, 52, 42, 30, 22, 13],
        [8, 17, 18, 21, 26, 21, 18, 17, 8],
        [3, 0, 7, 0, 8, 0, 7, 0, 3],
        [-1, 0, -3, 0, 3, 0, -3, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # 红车位置得分
    red_che_pos_point = [
        [185, 195, 190, 210, 220, 210, 190, 195, 185],
        [185, 203, 198, 230, 245, 230, 198, 203, 185],
        [180, 198, 190, 215, 225, 215, 190, 198, 180],
        [180, 200, 195, 220, 230, 220, 195, 200, 180],
        [180, 190, 180, 205, 225, 205, 180, 190, 180],
        [155, 185, 172, 215, 215, 215, 172, 185, 155],
        [110, 148, 135, 185, 190, 185, 135, 148, 110],
        [100, 115, 105, 140, 135, 140, 105, 115, 110],
        [115, 95, 100, 155, 115, 155, 100, 95, 115],
        [20, 120, 105, 140, 115, 150, 105, 120, 20]
    ]
    # 红马位置得分
    red_ma_pos_point = [
        [80, 105, 135, 120, 80, 120, 135, 105, 80],
        [80, 115, 200, 135, 105, 135, 200, 115, 80],
        [120, 125, 135, 150, 145, 150, 135, 125, 120],
        [105, 175, 145, 175, 150, 175, 145, 175, 105],
        [90, 135, 125, 145, 135, 145, 125, 135, 90],
        [80, 120, 135, 125, 120, 125, 135, 120, 80],
        [45, 90, 105, 190, 110, 90, 105, 90, 45],
        [80, 45, 105, 105, 80, 105, 105, 45, 80],
        [20, 45, 80, 80, -10, 80, 80, 45, 20],
        [20, -20, 20, 20, 20, 20, 20, -20, 20]
    ]
    # 红炮位置得分
    red_pao_pos_point = [
        [190, 180, 190, 70, 10, 70, 190, 180, 190],
        [70, 120, 100, 90, 150, 90, 100, 120, 70],
        [70, 90, 80, 90, 200, 90, 80, 90, 70],
        [60, 80, 60, 50, 210, 50, 60, 80, 60],
        [90, 50, 90, 70, 220, 70, 90, 50, 90],
        [120, 70, 100, 60, 230, 60, 100, 70, 120],
        [10, 30, 10, 30, 120, 30, 10, 30, 10],
        [30, -20, 30, 20, 200, 20, 30, -20, 30],
        [30, 10, 30, 30, -10, 30, 30, 10, 30],
        [20, 20, 20, 20, -10, 20, 20, 20, 20]
    ]
    # 红将位置得分
    red_jiang_pos_point = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9750, 9800, 9750, 0, 0, 0],
        [0, 0, 0, 9900, 9900, 9900, 0, 0, 0],
        [0, 0, 0, 10000, 10000, 10000, 0, 0, 0],
    ]
    # 红相或士位置得分
    red_xiang_shi_pos_point = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 60, 0, 0, 0, 60, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [80, 0, 0, 80, 90, 80, 0, 0, 80],
        [0, 0, 0, 0, 0, 120, 0, 0, 0],
        [0, 0, 70, 100, 0, 100, 70, 0, 0],
    ]

    red_pos_point = {
        'z': red_bin_pos_point,
        'm': red_ma_pos_point,
        'c': red_che_pos_point,
        'j': red_jiang_pos_point,
        'p': red_pao_pos_point,
        'x': red_xiang_shi_pos_point,
        's': red_xiang_shi_pos_point
    }

    def __init__(self, team):
        self.team = team

    def get_single_chess_point(self, chess: Chess):
        # 如果棋子是本方的，返回单个棋子分数
        if chess.team == self.team:
            return self.single_chess_point[chess.name]
        # 如果棋子不是本方的，返回单个棋子分数的相反数
        else:
            return -1 * self.single_chess_point[chess.name]

    def get_chess_pos_point(self, chess: Chess):
        # 获取棋子的位置得分表
        red_pos_point_table = self.red_pos_point[chess.name]
        # 如果棋子是红方的，获取该棋子在位置得分表中的得分
        if chess.team == 'r':
            pos_point = red_pos_point_table[chess.row][chess.col]
        # 如果棋子是黑方的，获取该棋子在位置得分表中的得分（需要将行数取反）
        else:
            pos_point = red_pos_point_table[9 - chess.row][chess.col]
        # 如果棋子不是本方的，将得分取反
        if chess.team != self.team:
            pos_point *= -1
        return pos_point

    def evaluate(self, chessboard: ChessBoard):
        point = 0
        for chess in chessboard.get_chess():
            point += self.get_single_chess_point(chess)
            point += self.get_chess_pos_point(chess)
        return point


class ChessMap(object):
    def __init__(self, chessboard: ChessBoard):
        self.chess_map = copy.deepcopy(chessboard.chessboard_map)


class ChessAI(object):
    def __init__(self, computer_team):
        self.team = computer_team
        self.max_depth = 4
        self.old_pos = [0, 0]
        self.new_pos = [0, 0]
        self.evaluate_class = Evaluate(self.team)

    def get_next_step(self, chessboard: ChessBoard):
        self.alpha_beta(1, float('-inf'), float('inf'),chessboard)
        return self.old_pos[0],self.old_pos[1],self.new_pos[0],self.new_pos[1]

    @staticmethod
    def get_nxt_player(player):
        # 根据当前玩家返回下一个玩家
        if player == 'r':
            return 'b'
        else:
            return 'r'

    # 返回一个新的棋盘，该棋盘是在原棋盘上移动了一个棋子后的结果
    @staticmethod
    def get_tmp_chessboard(chessboard, player_chess, new_row, new_col):# -> ChessBoard:
        tmp_chessboard = copy.deepcopy(chessboard)
        tmp_chess = tmp_chessboard.chessboard_map[player_chess.row][player_chess.col]
        tmp_chess.row, tmp_chess.col = new_row, new_col
        tmp_chessboard.chessboard_map[new_row][new_col] = tmp_chess
        tmp_chessboard.chessboard_map[player_chess.row][player_chess.col] = None
        return tmp_chessboard
    
    def alpha_beta(self, depth, alpha, beta,chessboard: ChessBoard):
        # 奇数层AI持棋，极大点，偶数层玩家持棋，极小点
        if depth == self.max_depth:
            return self.evaluate_class.evaluate(chessboard)
        
        # 返回现在棋盘
        chessMap = chessboard.get_chess();
        # 遍历所有棋子
        for chess in chessMap:
            # 如果是AI持棋，且是奇数层，或者是玩家持棋，且是偶数层
            if depth % 2 == 1 and chess.team == self.team or depth % 2 == 0 and chess.team != self.team:
                # 获取该棋子可以落子的位置
                # next_put_down_pos_list = chessboard.get_put_down_position(chess)
                for next_row, next_col in chessboard.get_put_down_position(chess):
                    # 记录该棋子原来的位置
                    old_row, old_col = chess.row, chess.col
                    # 记录新位置上的棋子
                    old_chess_in_new_pos = chessboard.chessboard_map[next_row][next_col]
                    # 将该棋子移动到新位置
                    chessboard.chessboard_map[next_row][next_col] = chessboard.chessboard_map[old_row][old_col]
                    chessboard.chessboard_map[next_row][next_col].update_position(next_row,next_col)
                    # 将原位置上的棋子清空
                    chessboard.chessboard_map[old_row][old_col] = None
                    # 递归调用alpha_beta函数
                    ret = self.alpha_beta(depth+1,alpha,beta,chessboard)
                    # 恢复棋盘状态
                    chessboard.chessboard_map[old_row][old_col] = chessboard.chessboard_map[next_row][next_col]
                    chessboard.chessboard_map[old_row][old_col].update_position(old_row, old_col)
                    chessboard.chessboard_map[next_row][next_col] = old_chess_in_new_pos
                    # 如果是奇数层，更新alpha值
                    if depth % 2 == 1:
                        # 如果当前值大于alpha或者self.old_pos为空，且当前层数为1，更新self.old_pos和self.new_pos
                        if(ret > alpha or not self.old_pos) and depth == 1:
                            self.old_pos = [chess.row, chess.col]
                            self.new_pos = [next_row, next_col]
                        alpha = max(alpha, ret)
                    # 如果是偶数层，更新beta值
                    else:
                        beta = min(beta, ret)
                    # 如果beta小于等于alpha，剪枝
                    if beta <= alpha:
                        return alpha if depth % 2 == 1 else beta
        return alpha if depth % 2 == 1 else beta
  
        
        


