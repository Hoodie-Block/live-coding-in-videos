#include <stdio.h>

// define functions for passing by value and passing by reference

void pass_by_value(int x){
    x = x * 2;
    printf("Inside pass_by_value %d\n", x);
}


void pass_by_reference(int* y){
    *y = *y * 2;
    printf("Inside pass_by_reference %d\n", *y);
}

// use the functions in main function

int main (){
    int example_value = 10;

    printf("initial value of example_value is %d\n", example_value);
    pass_by_value(example_value);
    printf("after calling pass_by_value  example_value is %d\n", example_value);

    printf("before calling pass_by_reference  example_value is %d\n", example_value);
    pass_by_reference(&example_value);
    printf("after calling pass_by_reference  example_value is %d", example_value);

    return 0;
}