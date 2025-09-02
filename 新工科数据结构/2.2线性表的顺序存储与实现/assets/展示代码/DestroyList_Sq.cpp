Status DestroyList_Sq(SqList &L){
    if(!L.base)
        return ERROR;
    free(L.base);
    L.base = NULL;
    L.size = 0;
    return OK;
}