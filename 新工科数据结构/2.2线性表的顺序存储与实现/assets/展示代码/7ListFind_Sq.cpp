int ListFind_Sq(SqList L, ElemType e){
    int result = 0;
    for(int i = 0; i < L.size; i++){
        if(L.base[i] == e){
            result = i;
            break;
        }
    }
    return result;
}