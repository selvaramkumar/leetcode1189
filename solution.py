from collections import Counter
import math
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict1=Counter(text)
        if dict1['l']>2 and dict1['o']>2 and dict1['b']>=1 and dict1['a'] >=1 and dict1['n']>=1:             
            return min(math.floor(dict1['l']/2),math.floor(dict1['o']/2))
        if dict1['l']==2 and dict1['o']==2 and dict1['b']>=1 and dict1['a'] >=1 and dict1['n']>=1:
            return 1
        else:
            return 0
            
s=Solution()
str1="krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
print(s.maxNumberOfBalloons(str1))                
        
                
                
        