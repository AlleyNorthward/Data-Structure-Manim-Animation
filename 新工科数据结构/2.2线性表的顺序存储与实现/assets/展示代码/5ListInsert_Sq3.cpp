Status ListInsert_Sq(SqList &L, int i, ElemType e){
    int position = i;
    for (int j = L.size - 1; j >= position; j--){
        L.base[j + 1] = L.base[j];
    }
    L.base[position] = e;
    L.size ++;
    return OK;
}
...