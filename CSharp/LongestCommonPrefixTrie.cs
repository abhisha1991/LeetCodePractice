using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://leetcode.com/problems/longest-common-prefix/discuss/
    /// Didnt need a Trie for this
    /// </summary>
    class LongestCommonPrefixTrie
    {
        public string LongestCommonPrefixMain(string[] strs)
        {
            Trie2 t = new Trie2();
            Trie2 x = t;
            int minLength = 1000;
            for (int i = 0; i < strs.Length; i++)
            {
                if (strs[i] == "") return "";
                if (minLength > strs[i].Length)
                {
                    minLength = strs[i].Length;
                }
                InsertIntoTrie2(strs[i], ref t);
                t = x;
            }
            string prefix = "";

            int count = 0;
            while (count < minLength)
            {
                if (x.W.Keys.Count > 1)
                    return prefix;
                if (x.W.Keys.Count == 0)
                    return prefix;
                char key = x.W.Keys.First();
                prefix = prefix + key;
                x = x.W[key];
                count++;
            }

            return prefix;

        }

        public void InsertIntoTrie2(string w, ref Trie2 t)
        {
            if (w.Length == 0)
                return;
            if (w.Length == 1)
            {
                t.EndOfWord = true;
            }
            char first = w[0];
            if (!t.W.Keys.Contains(first))
            {
                t.W.Add(first, new Trie2());
            }
            t = t.W[first];
            InsertIntoTrie2(w.Substring(1, w.Length - 1), ref t);

        }

    }

    public class Trie2
    {
        public Dictionary<char, Trie2> W { get; set; }
        public bool EndOfWord { get; set; }

        public Trie2()
        {
            this.W = new Dictionary<char, Trie2>();
            this.EndOfWord = false;
        }
    }
}
