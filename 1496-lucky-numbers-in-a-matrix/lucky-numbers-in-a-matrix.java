class Solution {
    public boolean isMaxInCol(int l, int h, int[][] matrix) {
        int big = matrix[l][h];
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][h] > big) {
                return false;
            }
        }
        return true;
    }

    public boolean isMinInRow(int l, int h, int[][] matrix) {
        int small = matrix[l][h];
        for (int j = 0; j < matrix[l].length; j++) {
            if (matrix[l][j] < small) {
                return false;
            }
        }
        return true;
    }

    public List<Integer> luckyNumbers (int[][] matrix) {
        ArrayList<Integer> luckyNumbers = new ArrayList<>();
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (isMinInRow(i, j, matrix) && isMaxInCol(i, j, matrix)) {
                    luckyNumbers.add(matrix[i][j]);
                }
            }
        }
        return luckyNumbers;

    }
}