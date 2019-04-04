/*
* 	Josie Nordrum
*	March 15, 2019
*
*		ref: https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
* 	Determine whether an input string comprised of '{', '}', '[', ']', '(', and ')'
* 	is balanced or unbalanced 
* 	
* 	First input line is number of cases, each following line is string to be evaluated
*
*	Example input:
* 	3
*	[({})]
*	[(}]
*	{{{}
---------------
		My solution utilizes the following ASCII codes:
		{,} : 0x7B, 0x7D
		[,] : 0x5B, 0x5D
		(,) : 0x28, 0x29
*/
#include <stdio.h>
#include <string.h>


int main() {
	// get number of test cases
	int t;
	scanf("%d", &t);

	// get the carriage return after getting test cases
	char chr = getchar();
	while(t--){

	    //allocate array for each type of parenthesis, set to 0
	    int bal[3] = {0};
	    do{
	        chr = getchar();		// take each parenthesis as it is input
	        if(chr<40||chr>125) break;
	        
	        // convert from parenthesis type using ACII code to get index:
	        	// () are 0, [] are 1, and {} are 2
	        int ind =  (int)(((chr>>4)-2)/2);
	        // adjust count using ASCII code to determine whether open or close
	        bal[ind]+= 2*((0xF&chr)%4==1) - 1;

	    }while((chr>39||chr<126));

	    // if any of the balances are NOT zero, the parenthesis are not balanced
	    (bal[0]||bal[1]||bal[2])? printf("not balanced\n"): printf("balanced\n");
	}
}