using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    using System.Collections.Generic;
    using System;
    using System.Linq;
    using System.Text;
    /// <summary>
    /// https://www.youtube.com/watch?v=AXjmTQ8LEoI&t=570s
    /// Delete operation is not complete
    /// </summary>
    class Trie
    {
        public Dictionary<char, Trie> Children { get; set; }
        public bool EndOfWord { get; set; }
        public Trie()
        {
            this.Children = new Dictionary<char, Trie>();
            this.EndOfWord = false;
        }
    }

    class TrieOperations
    {
        static List<string> words = new List<string>();
        static List<string> search = new List<string>();
        static List<string> delete = new List<string>();
        static Trie t = new Trie();
        public static void TrieMain(string[] args)
        {
            Console.WriteLine("Enter words to store in Trie:");
            while (true)
            {
                string x = Console.ReadLine();
                if (string.IsNullOrEmpty(x))
                {
                    break;
                }
                words.Add(x);
            }
            foreach (var item in words)
            {
                Insert(item, ref t);
            }

            Console.WriteLine("Enter prefix words to search in Trie:");
            while (true)
            {
                string x = Console.ReadLine();
                if (string.IsNullOrEmpty(x))
                {
                    break;
                }
                search.Add(x);
            }

            SearchWords(search, true);
            search = new List<string>();
            Console.WriteLine("Enter full words to search in Trie:");
            while (true)
            {
                string x = Console.ReadLine();
                if (string.IsNullOrEmpty(x))
                {
                    break;
                }
                search.Add(x);
            }

            SearchWords(search, false);
            Console.WriteLine("Enter words to delete in Trie:");
            while (true)
            {
                string x = Console.ReadLine();
                if (string.IsNullOrEmpty(x))
                {
                    break;
                }
                delete.Add(x);
            }
            foreach (var item in delete)
            {
                bool res = Delete(item, ref t);
                switch (res)
                {
                    case true:
                        Console.WriteLine(item + " was deleted");
                        break;
                    case false:
                        Console.WriteLine(item + " was NOT deleted");
                        break;
                }
            }
            SearchWords(delete, false);
        }

        public static void SearchWords(List<string> words, bool prefix)
        {
            foreach (var item in words)
            {
                bool res = Search(item, ref t, prefix);
                switch (res)
                {
                    case true:
                        Console.WriteLine(item + " was found");
                        break;
                    case false:
                        Console.WriteLine(item + " was NOT found");
                        break;
                }
            }
        }

        public static bool Search(string word, ref Trie tr, bool prefix)
        {
            // Console.WriteLine("Searching for " + word);
            char first = word[0];
            if (word.Length == 1)
            {
                if (prefix == false)
                {
                    if (tr.Children.Keys.Contains(first) && tr.Children[first].EndOfWord == true)
                        return true;
                    else return false;

                }

                if (tr.Children.Keys.Contains(first))
                    return true;
                else return false;
            }

            if (!tr.Children.Keys.Contains(first))
                return false;

            string w = "";
            for (int i = 1; i < word.Length; i++)
            {
                w = w + word[i];
            }
            var trie = tr.Children[first];
            return Search(w, ref trie, prefix);

        }

        public static bool Delete(string word, ref Trie tr)
        {
            bool res = Search(word, ref tr, false);
            if (res == false)
            {
                Console.WriteLine("Cannot delete " + word + " - it doesnt exist!");
                return false;
            }

            DeleteWord(word, ref tr);
            return true;
        }

        private static void DeleteWord(string word, ref Trie tr)
        {
            throw new NotImplementedException();
        }

        public static void Insert(string word, ref Trie tr)
        {
            char first = word[0];
            // Console.WriteLine("Entered insert for " + first);
            // Console.WriteLine("Value of word is " + word);
            if (word.Length == 1)
            {
                if (!tr.Children.Keys.Contains(first))
                    tr.Children.Add(first, new Trie());

                tr.Children[first].EndOfWord = true;
                return;
            }

            if (!tr.Children.Keys.Contains(first))
                tr.Children.Add(first, new Trie());

            string w = "";
            for (int i = 1; i < word.Length; i++)
            {
                w = w + word[i];
            }
            var trie = tr.Children[first];
            Insert(w, ref trie);

        }

    }
}
