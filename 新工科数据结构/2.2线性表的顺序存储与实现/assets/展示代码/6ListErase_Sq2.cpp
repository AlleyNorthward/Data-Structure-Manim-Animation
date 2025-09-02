Status ListErase_Sq(SqList &L, int i, ElemType &e){
    if(i < 0 || i > L.size - 1)
        return ERROR;
    e = L.base[i];
    for (int k = i + 1; k < L.size; k++){
        L.base[k - 1] = L.base[k];
    }
    L.size --;
    return OK;
}