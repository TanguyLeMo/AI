package kalah;

import com.sun.source.tree.BreakTree;

public class MinMax {
    private int itterationCount = 0;
    public MinMax() {

    }
    public int BestMove(KalahBoard board, int depth) {
        itterationCount = 0;
        if(board.isFinished())
            return -1;
        int move = -1;
        double minMaxValue;
        if (board.getCurPlayer() == 'A')
            minMaxValue = Double.MAX_VALUE;
        else
            minMaxValue = Double.MIN_VALUE;
        for (var new_board : board.possibleActions()) {
            double ret = 0;
            ret = getBestMoveRec(new_board, depth);
            if (ret < minMaxValue) {
                minMaxValue = ret;
                move = board.getLastPlay();
            } else {
                minMaxValue = ret;
                move = new_board.getLastPlay();
            }
        }
        return move;
    }











    private double getBestMoveRec(KalahBoard board, int depth) {
        itterationCount++;
        if(board.isFinished())
            return board.getWertung();
        double minMaxValue = board.getCurPlayer() == 'A' ? Double.MAX_VALUE : Double.MIN_VALUE;
        for (var new_board : board.possibleActions()) {
            double ret = getBestMoveRec(board, depth-1);
            if (board.getCurPlayer() == new_board.getCurPlayer()) {
                minMaxValue = Math.min(minMaxValue, ret);
            } else {
                minMaxValue  = Math.max(minMaxValue, ret);
            }
        }
        return minMaxValue;
    }





    private double getBestMove(KalahBoard board, int depth, double alpha, double beta, boolean heuristic) {
        itterationCount++;
        if(board.isFinished())
            return board.getWertung();
        double minMaxValue = (board.getCurPlayer() == 'A' ? Double.MAX_VALUE : Double.MIN_VALUE);
        var actions = board.possibleActions();
        if (heuristic) {
            if (board.getCurPlayer() == 'A') {
                actions.sort((o1, o2) -> Double.compare(o1.getWertung(), o2.getWertung()));
            } else {
                actions.sort((o1, o2) -> Double.compare(o2.getWertung(), o1.getWertung()));
            }

        }

        for (var new_board : actions) {
            double ret = getBestMove(new_board, depth - 1, alpha, beta, heuristic);
            if (board.getCurPlayer() == 'A'){
                minMaxValue = Math.min(minMaxValue, ret);
                if (minMaxValue > alpha) {
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


