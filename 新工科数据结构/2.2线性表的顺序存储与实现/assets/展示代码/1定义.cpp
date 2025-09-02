#define LIST_INIT_SIZE 100
typedef int ElemType;
typedef struct SqList{
    ElemType *base;
    int capacity;
    int size;
}SqList ;