class GameState():
  def __init__(self):
    self.board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                  [' ',  ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ',  ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ',  ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ',  ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
    
    self.white_to_move = True
    
    # Google en passant :)
    self.en_passant = None

    self.moves = None
    self.half_time = 0

    self.white_kingside_castle = True
    self.white_queenside_castle = True
    self.black_kingside_castle = True
    self.black_queenside_castle = True
  
  def is_valid(self, generated_moves):
    return [(r, c) for r, c in generated_moves if 0 <= r < 8 and 0 <= c < 8]
  
  def get_moves(self, piece, row, col):
    if piece == ' ' or (self.white_to_move and piece.islower()) or (not self.white_to_move and piece.isupper()):
      return []
    if piece.upper() == 'P':
      return self.calculate_pawn_moves(row, col)
    elif piece.upper() == 'R':
      return self.calculate_rook_moves(row, col)
    elif piece.upper() == 'N':
      return self.calculate_knight_moves(row, col)
    elif piece.upper() == 'B':
      return self.calculate_bisschop_moves(row, col)
    elif piece.upper() == 'Q':
      return self.calculate_queen_moves(row, col)
    elif piece.upper() == 'K':
      return self.calculate_king_moves(row, col)
    
  def calculate_moves(self):
    self.moves = []

    for row in range(8):
      for col in range(8):
        piece = self.board[row][col]
        self.moves.append(self.get_moves(piece, col, row))

    print(self.moves)

  def calculate_pawn_moves(self, row, col):
    pawn_moves = [(row + 1, col)] 
    return pawn_moves

  def calculate_rook_moves(self, row, col):
    rook_moves = self.is_valid([(r, col) for r in range(8) if r != row] + [(row, c) for c in range(8) if c != col])
    return rook_moves

  def calculate_knight_moves(self, row, col):
    knight_moves = self.is_valid([(row + i, col + j) for i, j in [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]])
    return knight_moves

  def calculate_bisschop_moves(self, row, col):
    bisschop_moves = self.is_valid([(row + i * k, col + j * k) for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)] for k in range(1, 8)]) 
    return bisschop_moves

  def calculate_queen_moves(self, row, col):
    return self.calculate_bisschop_moves(row, col) + self.calculate_rook_moves(row, col)

  def calculate_king_moves(self, row, col):
    king_moves = self.is_valid([(row + i, col + j) for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]])
    return king_moves

  def do_move(self, piece, row, col):
    pass

# Calculate the value of each position (min-max values) HARDEST
# Amount of pieces
# Amount of attacks
# Amount of pieces attacking your pieces (Is piece well defended?)
# Center control
# Algorithm to choose whichever position is best (mini-max algorithm with alpha beta pruning)  
