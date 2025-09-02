Status ListTraverse_Sq(SqList L, Status(*visit)(ElemType)){
    Status flag;
    for (int i = 0; i < L.size; i++){
        flag = visit(L.base[i]);
        if(flag != OK){
            return ERROR;
        }
    }
    return OK;
}