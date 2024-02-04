def parse_fen(forsyth_edwards_notation: str):
    fen_parts = forsyth_edwards_notation.split()

    board_state = fen_parts[0]  
    active_color = fen_parts[1]  
    castling_availability = fen_parts[2]  
    en_passant_square = fen_parts[3]  
    halfmove_clock = int(fen_parts[4]) 
    fullmove_number = int(fen_parts[5])  

    fen_info = {
        "piece_placement": board_state,
        "active_color": active_color,
        "castling_availability": castling_availability,
        "en_passant_square": en_passant_square,
        "halfmove_clock": halfmove_clock,
        "fullmove_number": fullmove_number
    }

    return fen_info

def fen_to_chess_position(forsyth_edwards_notation: str) -> list[list[str]]:
  chess_position = [[" " for _ in range(8)] for _ in range(8)]

  fen_info = parse_fen(forsyth_edwards_notation)

  for i, row in enumerate(fen_info["piece_placement"].split("/")):
     count = 0
     for j,  cell in enumerate(row):
        try:
           cell = int(cell)
           count += cell - 1
        except:
           chess_position[i][j + count] = cell
  return chess_position