'''139.单词拆分

给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。

你可以假设字典中没有重复的单词。

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''
def subString(s:str, wordDict: list):
    dp = [False]*(len(s)+1)
    dp[0] == True
    for i in range(1,len(dp)):
        for j in range(len(wordDict)): #应该直接遍历i again？more straightforward
            if len(wordDict[j])<=i: 
                word = wordDict[j]
                if s[i-len(word):i]==word and dp[i-len(word)]==True:
                    dp[i]==True
    return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] 表示字符串的前 i 个字符是否可以被拆分成单词
        dp[0] = True  # 初始状态，空字符串可以被拆分成单词

        for i in range(1, n + 1): # 遍历背包
            for j in range(i): # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True  # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    break

        return dp[n]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[0] = True
        # 遍历背包
        for j in range(1, len(s) + 1):
            # 遍历单词
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j]) # == line 34&35
        return dp[len(s)]


'''关于多重背包，你该了解这些！


有N种物品和一个容量为V 的背包。第i种物品最多有Mi件可用，每件耗费的空间是Ci ，价值是Wi 。求解将哪些物品装入背包可使这些物品的耗费的空间 总和不超过背包容量，且价值总和最大。

多重背包和01背包是非常像的， 为什么和01背包像呢？

每件物品最多有Mi件可用，把Mi件摊开，其实就是一个01背包问题了。

例如：

背包最大重量为10。

物品为：

重量	价值	数量
物品0	1	15	2
物品1	3	20	3
物品2	4	30	2
问背包能背的物品最大价值是多少？

和如下情况有区别么？

重量	价值	数量
物品0	1	15	1
物品0	1	15	1
物品1	3	20	1
物品1	3	20	1
物品1	3	20	1
物品2	4	30	1
物品2	4	30	1
毫无区别，这就转成了一个01背包问题了，且每个物品只用一次。
'''


'''背包问题总结篇

在讲解背包问题的时候，我们都是按照如下五部来逐步分析，相信大家也体会到，把这五部都搞透了，算是对动规来理解深入了。

确定dp数组（dp table）以及下标的含义
确定递推公式
dp数组如何初始化
确定遍历顺序
举例推导dp数组

问能否能装满背包（或者最多装多少）：dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]); ，对应题目如下：

动态规划：416.分割等和子集(opens new window)
动态规划：1049.最后一块石头的重量 II(opens new window)
问装满背包有几种方法：dp[j] += dp[j - nums[i]] ，对应题目如下：

动态规划：494.目标和(opens new window)
动态规划：518. 零钱兑换 II(opens new window)
动态规划：377.组合总和Ⅳ(opens new window)
动态规划：70. 爬楼梯进阶版（完全背包）(opens new window)
问背包装满最大价值：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]); ，对应题目如下：

动态规划：474.一和零(opens new window)
问装满背包所有物品的最小个数：dp[j] = min(dp[j - coins[i]] + 1, dp[j]); ，对应题目如下：

动态规划：322.零钱兑换(opens new window)
动态规划：279.完全平方数



在动态规划：关于01背包问题，你该了解这些！ (opens new window)中我们讲解二维dp数组01背包先遍历物品还是先遍历背包都是可以的，且第二层for循环是从小到大遍历。

和动态规划：关于01背包问题，你该了解这些！（滚动数组） (opens new window)中，我们讲解一维dp数组01背包只能先遍历物品再遍历背包容量，且第二层for循环是从大到小遍历。

一维dp数组的背包在遍历顺序上和二维dp数组实现的01背包其实是有很大差异的，大家需要注意！

#完全背包
说完01背包，再看看完全背包。

在动态规划：关于完全背包，你该了解这些！ (opens new window)中，讲解了纯完全背包的一维dp数组实现，先遍历物品还是先遍历背包都是可以的，且第二层for循环是从小到大遍历。

但是仅仅是纯完全背包的遍历顺序是这样的，题目稍有变化，两个for循环的先后顺序就不一样了。

如果求组合数就是外层for循环遍历物品，内层for遍历背包。

如果求排列数就是外层for遍历背包，内层for循环遍历物品。

相关题目如下：

求组合数：动态规划：518.零钱兑换II(opens new window)
求排列数：动态规划：377. 组合总和 Ⅳ (opens new window)、动态规划：70. 爬楼梯进阶版（完全背包）(opens new window)
如果求最小数，那么两层for循环的先后顺序就无所谓了，相关题目如下：

求最小数：动态规划：322. 零钱兑换 (opens new window)、动态规划：279.完全平方数(opens new window)
对于背包问题，其实递推公式算是容易的，难是难在遍历顺序上，如果把遍历顺序搞透，才算是真正理解了。


https://programmercarl.com/%E8%83%8C%E5%8C%85%E6%80%BB%E7%BB%93%E7%AF%87.html#%E6%80%BB%E7%BB%93
'''