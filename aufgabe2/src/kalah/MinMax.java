package kalah;

import com.sun.source.tree.BreakTree;

public class MinMax {
    private int itterationCount = 0;
    public MinMax() {
    }
    public int getItterationCount() {
        return itterationCount;
    }

    public int BestMove(KalahBoard board, int depth, action current_action) {
        itterationCount = 0;
        if(board.isFinished())
            return -1;


        int move = -1;
        double minMaxValue = board.getCurPlayer() == 'A' ? Double.POSITIVE_INFINITY : Double.NEGATIVE_INFINITY;
        for (var new_board : board.possibleActions()) {
            double ret = 0;
            switch (current_action) {
                case action.PLAIN:
                    ret = getBestMoveRec(new_board, depth);
                    break;
                case action.ALPHABETAPRUNNING:
                    ret = getBestMoveRec(new_board, depth, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY, false);
                    break;
                case action.HEURISTIC:
                    ret = getBestMoveRec(new_board, depth, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY, true);
            }
            if (board.getCurPlayer() == 'A') {
                if (ret < minMaxValue) {
                    minMaxValue = ret;
                    move = new_board.getLastPlay();
                }
            } else {
                if (ret > minMaxValue) {
                    minMaxValue = ret;
                    move = new_board.getLastPlay();
                }
            }
        }
        return move;
    }

    private double getBestMoveRec(KalahBoard board, int depth) {
        itterationCount++;
        if(board.isFinished() || depth <= 0)
            return board.getWertung();

        double minMaxValue = board.getCurPlayer() == 'A' ? Double.POSITIVE_INFINITY : Double.NEGATIVE_INFINITY;



        for (var new_board : board.possibleActions()) {
            double ret = getBestMoveRec(new_board, depth - 1);
            if (board.getCurPlayer() == 'A') {
                minMaxValue = Math.min(minMaxValue, ret);
            } else {
                minMaxValue  = Math.max(minMaxValue, ret);
            }
        }
        return minMaxValue;
    }


    private double getBestMoveRec(KalahBoard board, int depth, double alpha, double beta, boolean heuristic) {
        itterationCount++;
        if(board.isFinished() || depth <= 0)
            return board.getWertung();

        double minMaxValue = (board.getCurPlayer() == 'A' ? Double.POSITIVE_INFINITY : Double.NEGATIVE_INFINITY);
        var actions = board.possibleActions();

        if (heuristic) {
            if (board.getCurPlayer() == 'A') {
                actions.sort((o1, o2) -> Double.compare(o1.getWertung(), o2.getWertung()));
            } else {
                actions.sort((o1, o2) -> Double.compare(o2.getWertung(), o1.getWertung()));
            }

        }
        for (var new_board : actions) {
            double ret = getBestMoveRec(new_board, depth - 1, alpha, beta, heuristic);
            if (board.getCurPlayer() == 'A'){
                minMaxValue = Math.min(minMaxValue, ret);
                if (minMaxValue <= alpha) {
                    return minMaxValue;
                }
                beta = Math.min(beta, minMaxValue);
            } else {
                minMaxValue = Math.max(minMaxValue, ret);
                if (minMaxValue >= beta){
                    return minMaxValue;
                }
                alpha = Math.max(alpha, minMaxValue);
            }
        }
        return minMaxValue;
    }
}


