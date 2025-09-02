Status ListInsert_Sq2(SqList &L, int i, ElemType e){
    i = i - 1;
    if(ListInsert_Sq(L, i, e) == OK){
        return OK;
    }
    return ERROR;
}