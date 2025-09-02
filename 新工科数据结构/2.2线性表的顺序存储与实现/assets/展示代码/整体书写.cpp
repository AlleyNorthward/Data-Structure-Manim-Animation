#include<iostream>
#include<malloc.h>
#include<string>
using namespace std;

#define TRUE           1
#define FALSE          0
#define OK             1
#define ERROR          0
#define INFEASIBLE    -1
#define OVERFLOW      -2
// #define NULL           0  内部定义了

typedef int Status;

#define LIST_INIT_SIZE 100


typedef int ElemType;
typedef struct SqList{
    ElemType *base;
    int capacity;
    int size;
}SqList ;

// 一、顺序表的初始化
Status InitList_Sq(SqList &L){
    L.base = (ElemType*) malloc(LIST_INIT_SIZE * sizeof(ElemType));
    if(!L.base)
        exit(OVERFLOW);
    
    L.capacity = LIST_INIT_SIZE;
    L.size = 0;
    return OK;
}

// 二、顺序表的销毁
Status DestroyList_Sq(SqList &L){
    if(!L.base)
        return ERROR;
    free(L.base);
    L.base = NULL;
    L.size = 0;
    return OK;
}

// 三、顺序表的清空
Status ListClear_Sq(SqList &L){
    if(L.base){
        L.size = 0;
        return OK;
    }
    return ERROR;
}

// 四、顺序表的插入  情况1 假设i是从0开始的
Status ListInsert_Sq(SqList &L, int i, ElemType e){
    if(i < 0 || i > L.size){
        return ERROR;
    }
    if(L.size == L.capacity){
        L.base = (ElemType*)realloc(L.base, 2*L.capacity*sizeof(ElemType));
        if(!L.base) exit(OVERFLOW);
        L.capacity *= 2;
    }
    // 假设条件全部满足, 专注问题本身
    int position = i;
    // int move_length = L.size - i - 1;
    // 如果move_length = 0, 追加就行, 不用for循环
    // 
    for (int j = L.size - 1; j >= position; j--){
        L.base[j + 1] = L.base[j];
    }
    L.base[position] = e;
    L.size ++;
    return OK;
}

// 情况2 如果i是从1开始的
Status ListInsert_Sq2(SqList &L, int i, ElemType e){
    // 当然, 我们可以从0 重新分析, 不过有没有什么好的
    // 方法, 让我们不用重新分析呢?
    // 肯定有, 看我下面操作, 是否能懂呢?
    i = i - 1;
    if(ListInsert_Sq(L, i, e) == OK){
        return OK;
    }
    return ERROR;
}
// 五、顺序表的删除 情况1 i下标从0开始
Status ListErase_Sq(SqList &L, int i, ElemType &e){
    if(i < 0 || i > L.size)
        return ERROR;
    //假设条件都符合
    e = L.base[i];
    for (int j = i + 1; j < L.size; j++){
        L.base[j - 1] = L.base[j];
    }
    L.base[L.size - 1] = 0; // 这里是之后又添加进去的.
    L.size --;
    return OK;
}
// 情况2 i下标从1 开始
Status ListErase_Sq2(SqList &L, int i, ElemType &e){
    i = i - 1;
    if(ListErase_Sq(L, i, e) == OK)
        return OK;
    return ERROR;
}
//六 顺序表的查找与定位 直接返回下标.
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

// 七. 顺序表的遍历输出
Status PrintElem(ElemType e){
    cout<<e;
    return OK;
}
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
int main(){
    SqList s;

    if (InitList_Sq(s) == OK){
        cout<<"初始化成功!"<<endl;
    }
    else{
        cout<<"初始化失败!"<<endl;
    }

    s.base[0] = 1;
    s.size ++;
    ListInsert_Sq(s, 1, 2);
    ListInsert_Sq2(s, 1, 3);
    cout<<s.base[0]<<" "<<s.base[1]<<" "<<s.base[2]<<endl;
    int e;
    ListErase_Sq(s, 1, e);
    cout<<s.base[0]<<" "<<s.base[1]<<" "<<e<<endl;
    cout<<s.base[2]<<endl;
    ListTraverse_Sq(s, PrintElem);
    cout<<endl;
    ListInsert_Sq2(s, 2, 3);
    cout<<s.base[2]<<endl;
    ListErase_Sq2(s, 3, e);
    cout<<s.base[0]<<" "<<s.base[1]<<" "<<e<<endl;
    ListInsert_Sq(s, 2, 3);
    ListInsert_Sq2(s, 4, 4);
    int ee = ListFind_Sq(s, 4);
    cout<<ee<<endl;
    cout<<s.base[3]<<endl;
    ListTraverse_Sq(s, PrintElem);
    cout<<endl;
    cout<<s.base[4]<<s.base[5];
    cout<<endl;
    if(DestroyList_Sq(s) == OK){
        cout<<"销毁成功";
    }
    else{
        cout<<"销毁失败";
    }
    return 0;
}


