using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    public class TrieNode
    {
        public Dictionary<char, TrieNode> t { get; set; }
        public bool endOfWord { get; set; }
        public bool visited { get; set; }

        public TrieNode()
        {
            this.t = new Dictionary<char, TrieNode>();
            this.endOfWord = false;
            this.visited = false;
        }
    }

    class AllTextSuggestions
    {
        static List<string> vocab = new List<string>();
        static TrieNode root = new TrieNode();
        public static void AllTextSuggestionsMain(string[] args)
        {
            bool next = true;
            while (next)
            {
                Console.WriteLine("Enter vocab");
                vocab.Add(Console.ReadLine());
                Console.WriteLine("Enter more? 1/0");
                int enter = Int32.Parse(Console.ReadLine());
                next = enter == 1 ? true : false;
            }

            InsertIntoTrie();
            Console.WriteLine("Enter word to be searched");
            string input = Console.ReadLine();
            var t = Search(input, ref root);
            var result = SuggestWords(input, t);
            Console.WriteLine("Suggested words are");
            foreach (var item in result)
            {
                Console.WriteLine(item);
            }
        }

        public static void InsertIntoTrie()
        {
            foreach (var item in vocab)
            {
                Insert(item, ref root);
            }
        }

        /// <summary>
        /// Inserts word into trie
        /// </summary>
        /// <param name="word"></param>
        /// <param name="root"></param>
        private static void Insert(string word, ref TrieNode root)
        {
            if (word.Length == 0) return;
            char first = word[0];
            if (!root.t.ContainsKey(first))
            {
                root.t.Add(first, new TrieNode());
            }
            if (word.Length == 1) root.t[first].endOfWord = true;
            var tNext = root.t[first];
            Insert(word.Substring(1, word.Length - 1), ref tNext);
        }

        /// <summary>
        /// Returns the node where we encounter the end of word
        /// </summary>
        /// <param name="word"></param>
        /// <param name="root"></param>
        /// <returns></returns>
        private static TrieNode Search(string word, ref TrieNode root)
        {
            if (word.Length == 0) return root;
            char first = word[0];
            if (!root.t.ContainsKey(first)) return null;

            var tNext = root.t[first];
            return Search(word.Substring(1, word.Length), ref tNext);
        }


        private static List<string> resultSuggstedWords = new List<string>();

        /// <summary>
        /// Suggests words based on user input
        /// </summary>
        /// <param name="userInput"></param>
        /// <param name="t"></param>
        /// <returns></returns>
        private static List<string> SuggestWords(string userInput, TrieNode t)
        {
            if (t == null) return new List<string>();
            // Mark current node as visited
            t.visited = true;
            resultSuggstedWords.Add(userInput);
            return null;

        }
        
    }
}
