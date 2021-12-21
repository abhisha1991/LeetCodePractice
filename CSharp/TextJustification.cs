using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/ibANT8ZGc3shACBRF
    /// </summary>
    class TextJustification
    {
        private static string[] textJustification(string[] words, int l)
        {
            List<string> result = new List<string>();
            if (words.Length == 0) return result.ToArray();
            
            for (int  i=0; i < words.Length;)
            {
                List<string> temp = new List<string>();
                int remainingChars = l;
                StringBuilder res = new StringBuilder();
                int spaces = 0;
                temp.Add(words[i]);
                remainingChars = l - words[i].Length ;
                if (remainingChars > 0)
                {
                    remainingChars--; // -1 considering atleast 1 space is there between 2 words
                    spaces++;
                }

                int pos = i + 1;
                while (remainingChars > 0 && pos < words.Length && remainingChars >= words[pos].Length)
                {
                    temp.Add(words[pos]);
                    remainingChars = remainingChars - words[pos].Length;
                    if (remainingChars >= 1)
                    {
                        remainingChars--;  // -1 considering atleast 1 space is there between 2 words
                        spaces++;
                    }

                    pos = pos + 1;
                }

                // Adjust spaces
                // 'This is an ' needs to become 'This    is    an' 
                spaces += remainingChars;
            
                if (temp.Count - 1 == 0)
                {
                    // A single word, then append spaces to the end
                    res.Append(temp[0]);
                    res.Append(GetEmptyString(spaces));
                }
                else
                {
                    List<int> indexSpace = new List<int>();
                    int index = 0;
                    while (spaces > 0)
                    {
                        if (spaces - (temp.Count - 1) >= 0)
                        {
                            spaces = spaces - (temp.Count - 1);
                            temp = temp.Select(x => x = x + " ").ToList();
                            temp[temp.Count - 1] = temp.Last().TrimEnd(' '); // Ignore spaces at the end of string
                        }
                        else
                        {
                            spaces--;
                            indexSpace.Add(index++);
                        }
                    }

                    foreach (var idx in indexSpace)
                    {
                        temp[idx] = temp[idx] + " ";
                    }

                    temp.ForEach(x => res.Append(x));
                }

                // Finally add the string to the list and reset all meta values
                result.Add(res.ToString());
                i = pos;
            }

            // Adjust last line to be left justified
            RegexOptions options = RegexOptions.None;
            Regex regex = new Regex("[ ]{2,}", options);
            result[result.Count - 1] = regex.Replace(result.Last(), " ");
            result[result.Count - 1] += GetEmptyString(l - result[result.Count - 1].Length);
            return result.ToArray();
        }

        public static string GetEmptyString(int len)
        {
            return "".PadRight(len);
        }

        public static void textJustificationMain()
        {
            textJustification(new string[] { "This", "is", "an", "example", "of", "text", "justification." }, 16);
            textJustification(new string[] { "Given", "an", "array", "of", "words", "and", "a", "length" }, 9);
            textJustification(new string[] { "Looks", "like", "it", "can", "be", "a", "tricky", "test" }, 25);
        }
    }
}
