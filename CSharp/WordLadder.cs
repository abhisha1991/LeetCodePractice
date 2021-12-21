using System;
using System.Collections.Generic;
using System.Linq;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/EDaACHNYHyH6qQFAL
    /// </summary>
    class WordLadder
    {
        public static int wordLadder2(string beginWord, string endWord, string[] wordList)
        {
            int res = 1;

            List<string> list = wordList.ToList();
            if (!list.Contains(endWord))
            {
                return 0;
            }

            while (beginWord != endWord)
            {
                list.Remove(beginWord);
                beginWord = ReturnNextWord(list.ToArray(), beginWord, endWord);
                Console.WriteLine(beginWord);
                if (beginWord == string.Empty)
                {
                    return res;
                }
                res++;
            }
            return res;
        }

        public static int wordLadder(string beginWord, string endWord, string[] wordList)
        {
            String start = beginWord;
            String end = endWord;
            List<string> dict = wordList.ToList();
            if (!dict.Contains(end)) return 0;
            var preVisitedStr = new List<string> { start };
            var level = 1;

            while (preVisitedStr.Count != 0)
            {
                var nextVisitedStr = new List<string>();
                foreach (var visited in preVisitedStr)
                {
                    if (MisMatchCount(end.Length, end, visited) == 1)
                    {
                        return level + 1;
                    }

                    for (var i = dict.Count() - 1; i >= 0; i--)
                    {
                        if (MisMatchCount(dict[i].Length, visited, dict[i]) != 1)
                        {
                            continue;
                        }

                        nextVisitedStr.Add(dict[i]);
                        dict.RemoveAt(i);
                    }
                }

                preVisitedStr = nextVisitedStr;
                level++;
            }

            return 0;
        }

        private static int MisMatchCount(int len, string word, string listMember)
        {
            int mismatch = 0;
            for (int i = 0; i < len; i++)
            {
                if (word[i] != listMember[i])
                {
                    mismatch++;
                    // If mismatch count is more than 1, we dont care
                    if (mismatch > 1)
                        return mismatch;
                }
            }

            return mismatch;
        }

        private static string ReturnNextWord(string[] wordList, string word, string endWord)
        {
            int len = word.Length;

            List<string> list = wordList.ToList();
            // If remaining words in list are all the same kind, prefer the end word to be parsed first
            int count = 0;
            foreach (var item in list)
            {
                if (item == endWord)
                    continue;

                if (MisMatchCount(endWord.Length, endWord, item) == 1)
                {
                    count++;
                }
            }

            if (count == list.Count - 1)
            {
                list.Remove(endWord);
                list.Add(endWord);
                list.Reverse();
            }

            foreach(var item in list)
            {
                if (item == word)
                    continue;

                if (MisMatchCount(len, word, item) == 1)
                {
                    return item;
                }
            }

            return string.Empty;
        }
        public static void wordLadderMain()
        {
            wordLadder("hit", "cog", new string[] { "hot", "dot", "dog", "lot", "log", "cog" });
        }
    }
}
