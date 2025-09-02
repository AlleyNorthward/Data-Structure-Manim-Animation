Status ListInsert_Sq(SqList &L, int i, ElemType e){
    if(i < 0 || i > L.size){
        return ERROR;
    }
    if(L.size == L.capacity){
        L.base = (ElemType*)realloc(L.base, 2*L.capacity*sizeof(ElemType));
        if(!L.base) exit(OVERFLOW);
        L.capacity *= 2;
    }
    int position = i;
    for (int j = L.size - 1; j >= position; j--){
        L.base[j + 1] = L.base[j];
    }
    L.base[position] = e;
    L.size ++;
    return OK;
}