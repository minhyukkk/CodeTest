class Solution {
    public int[] solution(String[] wallpaper) {
        int x_max, y_max;
        int x_min, y_min;
        
        x_min = y_min = Integer.MAX_VALUE;
        x_max = y_max = Integer.MIN_VALUE; 
        
        for(int i =0; i<wallpaper.length; i++){
            for (int j =0; j < wallpaper[i].length(); j++) {
                if (wallpaper[i].charAt(j) == '#'){
                    x_min = Math.min(x_min, j);
                    y_min = Math.min(y_min, i);
                    x_max = Math.max(x_max, j);
                    y_max = Math.max(y_max, i);
                }
            }
        }
        return new int[] {y_min, x_min, y_max+1, x_max+1};
    }
}