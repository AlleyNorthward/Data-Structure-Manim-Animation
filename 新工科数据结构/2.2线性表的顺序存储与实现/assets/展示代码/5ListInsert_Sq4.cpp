Status ListInsert_Sq(SqList &L, int i, ElemType e){
    if(i < 1 || i > L.size + 1){
        return ERROR;
    }
...
}