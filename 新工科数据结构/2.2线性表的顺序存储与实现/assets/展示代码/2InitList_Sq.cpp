Status InitList_Sq(SqList &L){
    L.base = (ElemType *) malloc(LIST_INIT_SIZE * sizeof(ElemType));
    if(!L.base)
        exit(OVERFLOW);
    
    L.capacity = LIST_INIT_SIZE;
    L.size = 0;
    return OK;
}

