bool isReachableAtTime(int sx, int sy, int fx, int fy, int t){
    if (sx == fx && sy == fy && t == 1){
        return false;
    }
    
    int farther = 0;
    int x = abs(sx - fx);
    int y = abs(sy - fy);
    if (x > y){
        farther = x;
    } else {
        farther = y;
    }

    if (farther > t){
        return false;
    } else {
        return true;
    }
}