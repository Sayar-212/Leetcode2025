bool canConstruct(char* s, int k) {
    int freq[256] = {0};
    int single_count = 0;
    
    for (int i = 0; s[i] != '\0'; i++) {
        freq[s[i]]++;
    }

    for (int i = 0; i < 256; i++) {
        if (freq[i] % 2 == 1) {
            single_count++;
        }
    }

    return single_count <= k && k <= strlen(s);
}