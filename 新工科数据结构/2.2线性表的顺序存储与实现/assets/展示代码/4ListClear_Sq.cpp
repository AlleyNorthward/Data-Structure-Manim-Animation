Status ListClear_Sq(SqList &L){
    if(L.base){
        L.size = 0;
        return OK;
    }
    return ERROR;
}