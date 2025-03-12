<h1>CS 162: Intro to Computer Science II Final Project/Portfolio Assignment</h1>
<p><strong>Project Description</strong> : Create Fog of War Chess; also known as Dark Chess</p>
<ul>
  <li>No checks, checkmates, castling, <em>en passant</em>, or pawn promotion</li>
  <li>Create a class called ChessVar to implement</li>
  <li>Players can view their own pieces</li>
  <li>Opponent pieces are marked with an '*' and become visible when in range of a legal attack</li>
  <li>Must include an init method to initialize any data members</li>
  <li>Include a method called get_game_state that provides the current state of the game (UNFINISHED', 'WHITE_WON', 'BLACK_WON')</li>
  <li>Include a method called get_board</li>
  <ul>
    <li>Parameter: a string indicating the perspective from which to display the board</li>
    <li>Return: the respective player board or audience board</li>
  </ul>
  <li>Include a method called make_move</li>
  <ul>
    <li>Parameters: a string that represents the square moved from and another string of the square moved to</li>
    <li>Return: If the game was already won - return false, otherwise this updates the board</li>
  </ul>
</ul>
