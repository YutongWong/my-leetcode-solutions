#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        f = np.zeros(s_len+1, dtype='bool')
        f[-1] = True
        for i in range(s_len):
            for w in wordDict:
                if s[i-len(w)+1:i+1] == w and f[i-len(w)]:
                    print(i, i-len(w), f[i-len(w)])
                    f[i] = True
        return f[s_len-1]
        
