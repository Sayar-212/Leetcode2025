int maxScore(char* s) {
    int i, j;
int max=0;
int left, right;
    
for (i=0; i<strlen(s)-1; i++) {
    left=0;
    right=0;
    for (j=0; j<=i; j++) if (s[j]=='0') left++;
    for (j=i+1; j<strlen(s); j++) if (s[j]=='1') right++;
    if (max < left+right) max=left+right;
   }
return max; 
}