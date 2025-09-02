if(i < 0 || i > L.size){
    return ERROR;
}
if(L.size == L.capacity){
    L.base = (ElemType*)realloc(L.base, 2*L.capacity*sizeof(ElemType));
    if(!L.base) exit(OVERFLOW);
    L.capacity *= 2;
}